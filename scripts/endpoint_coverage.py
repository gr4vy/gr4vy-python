"""Summarise endpoint reach for the PR comment.

Reach is computed from *observed HTTP calls*, not code coverage: the test HTTP
client (tests/utils/client.py, gated on ``GR4VY_TRACK_HTTP``) logs the method +
path of every request to ``coverage/http/*.jsonl``. We build the operation
catalogue from the generated resource modules (``src/gr4vy/*.py``) by reading each
synchronous ``self._build_request(method=..., path=...)`` call, then mark an
operation reached only if a matching request was actually sent — so an operation
that fails local validation before issuing a request does not count.

Writes ``coverage/endpoint-coverage.md`` (for the PR comment) and prints it.
Exits 0 always — this is a report, not a gate.
"""

import glob
import json
import os
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
COVERAGE_DIR = ROOT / "coverage"
SDK_DIR = ROOT / "src" / "gr4vy"

# Match a synchronous request build and capture its method + path. The async
# variant is `_build_request_async(`, which this pattern skips (it requires `(`
# immediately after `_build_request`).
_CALL_RE = re.compile(
    r"_build_request\((?P<args>.*?)\)", re.DOTALL
)
_METHOD_RE = re.compile(r'method\s*=\s*"([A-Z]+)"')
_PATH_RE = re.compile(r'path\s*=\s*"(/[^"]*)"')


def build_catalogue():
    """Return a list of {op, method, template, pattern} from the generated SDK."""
    catalogue = []
    seen = set()
    for file in sorted(glob.glob(str(SDK_DIR / "*.py"))):
        src = Path(file).read_text(encoding="utf-8")
        for match in _CALL_RE.finditer(src):
            args = match.group("args")
            method_match = _METHOD_RE.search(args)
            path_match = _PATH_RE.search(args)
            if not method_match or not path_match:
                continue
            method = method_match.group(1).upper()
            template = path_match.group(1)
            key = f"{method} {template}"
            if key in seen:
                continue
            seen.add(key)
            pattern = "^" + re.sub(r"\{[^/}]+\}", "[^/]+", template) + "$"
            catalogue.append(
                {
                    "op": key,
                    "method": method,
                    "template": template,
                    "pattern": re.compile(pattern),
                    "params": template.count("{"),
                }
            )
    return catalogue


def load_calls():
    calls = []
    for file in glob.glob(str(COVERAGE_DIR / "http" / "*.jsonl")):
        for line in Path(file).read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line:
                continue
            try:
                decoded = json.loads(line)
            except json.JSONDecodeError:
                continue
            if "method" in decoded and "pathname" in decoded:
                calls.append(decoded)
    return calls


def main():
    catalogue = build_catalogue()
    calls = load_calls()
    http_tracked = len(calls) > 0

    reached = set()
    if http_tracked:
        for call in calls:
            candidates = [
                op
                for op in catalogue
                if op["method"] == call["method"]
                and op["pattern"].match(call["pathname"])
            ]
            if not candidates:
                continue
            # Most-specific template wins (fewest path params, then longest
            # template) so /buyers/gift-cards is not miscredited to /buyers/{id}.
            candidates.sort(key=lambda op: (op["params"], -len(op["template"])))
            reached.add(candidates[0]["op"])

    missed = sorted(op["op"] for op in catalogue if op["op"] not in reached)

    total = len(catalogue)
    reached_count = len(reached)
    pct = f"{reached_count / total * 100:.1f}" if total else "0.0"

    lines = ["### 🧪 Test coverage", ""]
    if not http_tracked:
        lines += [
            "> ⚠️ HTTP call tracking was not enabled (set `GR4VY_TRACK_HTTP=1` for "
            "the test run), so endpoint reach could not be computed from observed "
            "requests.",
            "",
        ]
    value = (
        f"{reached_count} / {total} ({pct}%)"
        if http_tracked
        else f"n/a — tracking disabled ({total} operations in catalogue)"
    )
    lines += [
        "| Metric | Value |",
        "| --- | --- |",
        f"| **Endpoints reached (HTTP)** | {value} |",
        "",
    ]
    if http_tracked and missed:
        lines += [
            f"> ⚠️ **{len(missed)} endpoint operation(s) have no E2E test.** "
            "Newly generated endpoints show up here — consider adding tests for them.",
            "",
        ]
        lines += [f"- `{name}`" for name in missed]
    elif http_tracked:
        lines.append("✅ Every endpoint operation was reached by a real request.")
    lines.append("")

    repo = os.getenv("GITHUB_REPOSITORY", "")
    ref = os.getenv("GITHUB_SHA", "main")
    testing_link = (
        f"[TESTING.md](https://github.com/{repo}/blob/{ref}/TESTING.md)"
        if repo
        else "TESTING.md"
    )
    lines.append(
        "<sub>Endpoint reach is measured from HTTP requests actually sent by the "
        f"suite (see tests/utils/client.py). See {testing_link}.</sub>"
    )

    markdown = "\n".join(lines)
    COVERAGE_DIR.mkdir(parents=True, exist_ok=True)
    (COVERAGE_DIR / "endpoint-coverage.md").write_text(markdown + "\n", encoding="utf-8")
    print(markdown)


if __name__ == "__main__":
    main()
