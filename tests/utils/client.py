"""HTTP client wrapper used by the E2E suite.

Wraps an ``httpx.Client`` with two pieces of test instrumentation:

  (a) **forward-compatibility** — injects a random unknown field into every JSON
      *object* response, proving the SDK tolerates forward-compatible payloads.
      Disable with ``GR4VY_NO_INJECT``.
  (b) **endpoint-reach tracking** — when ``GR4VY_TRACK_HTTP`` is set, records the
      method + path of every request that completed an HTTP exchange to
      ``coverage/http/*.jsonl`` so ``scripts/endpoint_coverage.py`` can measure
      reach from real requests (not code coverage).

Injection only ever touches JSON *objects*: adding a string key to a top-level
JSON array would turn it into an object on re-encode and break deserialization.
"""

import json
import os
import secrets
from pathlib import Path
from typing import Any, Optional, Union

import httpx

from gr4vy.httpclient import HttpClient


def _flag(name: str) -> bool:
    value = os.getenv(name)
    return value is not None and value != ""


class JsonInterceptorClient(HttpClient):
    """An ``HttpClient`` that records reach and injects forward-compat fields."""

    _client: httpx.Client
    _track: bool
    _inject: bool
    _call_file: Optional[Path]

    def __init__(self, client: httpx.Client):
        self._client = client
        self._track = _flag("GR4VY_TRACK_HTTP")
        self._inject = not _flag("GR4VY_NO_INJECT")
        self._call_file = None

    def send(
        self,
        request: httpx.Request,
        *,
        stream: bool = False,
        auth: Union[
            httpx._types.AuthTypes, httpx._client.UseClientDefault, None
        ] = httpx.USE_CLIENT_DEFAULT,
        follow_redirects: Union[
            bool, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
    ) -> httpx.Response:
        response = self._client.send(
            request, stream=stream, auth=auth, follow_redirects=follow_redirects
        )

        # Record only after a real HTTP exchange completes, so a request that
        # never reached the server (DNS/TCP/TLS failure raises before this line)
        # is not counted as "reached".
        if self._track:
            self._record(request)

        if not self._inject:
            return response

        content_type = response.headers.get("content-type", "")
        if "application/json" not in content_type:
            return response

        try:
            response.read()
            body = response.content
            # Distinguish an object from a list by the first non-space byte:
            # json.loads("{}") and json.loads("[]") both decode to truthy values,
            # but only objects can safely take an extra key.
            stripped = body.lstrip()
            data = json.loads(body)
            if not stripped.startswith(b"{") or not isinstance(data, dict):
                return httpx.Response(
                    status_code=response.status_code,
                    headers=response.headers,
                    content=body,
                    request=request,
                )
            data[f"unexpected_field_{secrets.token_hex(4)}"] = (
                "this is an injected test value"
            )
            return httpx.Response(
                status_code=response.status_code,
                headers=response.headers,
                content=json.dumps(data).encode("utf-8"),
                request=request,
            )
        except (json.JSONDecodeError, UnicodeDecodeError):
            return httpx.Response(
                status_code=response.status_code,
                headers=response.headers,
                content=response.content,
                request=request,
            )

    def _record(self, request: httpx.Request) -> None:
        try:
            if self._call_file is None:
                directory = (
                    Path(__file__).resolve().parents[2] / "coverage" / "http"
                )
                directory.mkdir(parents=True, exist_ok=True)
                self._call_file = directory / f"calls-{os.getpid()}-{secrets.token_hex(4)}.jsonl"
            line = json.dumps(
                {"method": request.method, "pathname": request.url.path}
            )
            with open(self._call_file, "a", encoding="utf-8") as handle:
                handle.write(line + "\n")
        except OSError:
            # Best-effort: never fail a test because of instrumentation I/O.
            pass

    def build_request(
        self,
        method: str,
        url: httpx._types.URLTypes,
        *,
        content: Optional[httpx._types.RequestContent] = None,
        data: Optional[httpx._types.RequestData] = None,
        files: Optional[httpx._types.RequestFiles] = None,
        json: Optional[Any] = None,  # pylint: disable=redefined-outer-name
        params: Optional[httpx._types.QueryParamTypes] = None,
        headers: Optional[httpx._types.HeaderTypes] = None,
        cookies: Optional[httpx._types.CookieTypes] = None,
        timeout: Union[
            httpx._types.TimeoutTypes, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
        extensions: Optional[httpx._types.RequestExtensions] = None,
    ) -> httpx.Request:
        return self._client.build_request(
            method,
            url,
            content=content,
            data=data,
            files=files,
            json=json,
            params=params,
            headers=headers,
            cookies=cookies,
            timeout=timeout,
            extensions=extensions,
        )
