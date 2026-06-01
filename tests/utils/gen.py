"""Lightweight, seeded generators for property-based ("uncertainty") testing.

The local analogue of Hypothesis / fast-check / FsCheck. We avoid an external
dependency so the suite stays hermetic; in exchange this is deliberately small: a
fixed seed (``FC_SEED``, default 1337) and a bounded run count keep property tests
reproducible and cheap against the live sandbox.
"""

import os
import random
from typing import Dict

# Number of cases each property explores. Kept low for live-E2E cost.
RUNS = 6


def _seed() -> int:
    # Don't use ``or`` — it would treat a valid FC_SEED=0 as falsey.
    raw = os.getenv("FC_SEED")
    return 1337 if raw is None or raw == "" else int(raw)


_rng = random.Random(_seed())


def amount() -> int:
    """Minor-unit amount in a range the mock-card connector accepts."""
    return _rng.randint(50, 100000)


def currency() -> str:
    """USD — the only currency the mock service accepts here."""
    return "USD"


def metadata() -> Dict[str, str]:
    """Metadata mixing camelCase and snake_case keys (exercises the key boundary)."""
    out: Dict[str, str] = {}
    for _ in range(_rng.randint(1, 3)):
        out[f"camelKey{_rng.randint(0, 9999)}"] = f"v{_rng.randint(0, 9999)}"
        out[f"snake_key_{_rng.randint(0, 9999)}"] = f"v{_rng.randint(0, 9999)}"
    return out


def display_name() -> str:
    words = ["Acme", "Globex", "Initech", "Umbrella", "Soylent", "Hooli", "Stark", "Wayne"]
    return f"{_rng.choice(words)} {_rng.randint(100, 999)}"
