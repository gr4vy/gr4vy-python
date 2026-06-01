"""Test-only utilities for the E2E suite. Not part of the generated SDK."""

# A non-existent UUID for "reach the endpoint, expect a 404" probes.
MISSING_ID = "11111111-1111-1111-1111-111111111111"


def first_of(page):
    """Return the first item of a paginated list response, or ``None`` if empty."""
    items = getattr(page, "items", None)
    return items[0] if items else None
