"""Reach assertion for operations that cannot reach a 2xx in the mock sandbox.

Some operations (live wallet provisioning, real network tokens, a payout-capable
PSP, a configured 3DS or gift-card service) can't be driven to a happy path in the
mock-card env. We still want the endpoint *reached* — a real HTTP request sent —
so the endpoint-coverage report does not flag it as untested, but we accept a
documented client (4xx) error instead of a 2xx.

A **5xx** fails the test: that means we sent something the API could not handle,
which is a real defect to surface. A failure that never hit the wire (a local
validation/serialization error, a connection failure) also fails — the point of
``reaches`` is to prove the request reached the server.
"""

from typing import Callable

from gr4vy.errors import Gr4vyError


def reaches(action: Callable[[], object], description: str) -> None:
    """Assert that ``action`` reaches the server (2xx, or a clean 4xx)."""
    try:
        action()
        return  # reached + succeeded (2xx)
    except Gr4vyError as error:
        status = error.status_code
        if 400 <= status < 500:
            print(f"[reach] {description}: API error {status}")
            return
        if status >= 500:
            raise AssertionError(
                f"[reach] {description}: server error ({status}): {error}"
            ) from error
        # A response came back (1xx–3xx) that the SDK could not fully handle
        # (e.g. an unexpected content type / response-validation error). The
        # endpoint was still reached.
        print(f"[reach] {description}: reached (status {status}; SDK could not parse the response)")
        return
    except Exception as error:  # pylint: disable=broad-exception-caught
        raise AssertionError(
            f"[reach] {description}: the call failed before reaching the server: "
            f"{type(error).__name__} — {error}"
        ) from error
