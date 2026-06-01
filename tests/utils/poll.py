"""Bounded polling for eventually-consistent reads.

Capture settling, report execution finishing, payout/settlement appearing — all
take a moment after the write returns. Hard-capped so a stuck state fails fast
rather than hanging a worker.
"""

import time
from typing import Callable, Optional, TypeVar

T = TypeVar("T")


def until(
    fetch: Callable[[], T],
    predicate: Callable[[T], bool],
    timeout_s: float = 20.0,
    interval_s: float = 1.0,
    description: Optional[str] = None,
) -> T:
    """Repeatedly call ``fetch`` until ``predicate`` holds or the timeout elapses."""
    deadline = time.monotonic() + timeout_s
    last = fetch()
    while True:
        if predicate(last):
            return last
        if time.monotonic() >= deadline:
            raise TimeoutError(
                f"poll.until timed out after {timeout_s}s"
                + (f" waiting for: {description}" if description else "")
            )
        time.sleep(interval_s)
        last = fetch()
