"""Canonical inputs for the mock-card connector and reusable request shapes.

The mock connector approves ``4111…`` with a future expiry; other inputs drive
decline/error paths (documented inline where used). Request bodies are plain
dicts (the SDK accepts the generated ``*TypedDict`` shapes), which keeps the
fixtures terse and avoids importing a model per shape.
"""

import itertools
from typing import Any, Dict, Optional

# Approving test card for the mock-card service. Far-future expiry so the suite
# does not start failing once a year ticks over.
APPROVING_CARD_NUMBER = "4111111111111111"
CARD_EXPIRATION_DATE = "12/35"
CARD_SECURITY_CODE = "123"

_counter = itertools.count(1)


def unique_id(prefix: str, scope: str) -> str:
    """Low-collision id: a caller-supplied scope (typically the per-module random
    merchant id) plus a monotonic per-process counter."""
    return f"{prefix}-{scope[:8]}-{next(_counter)}"


def approving_card(
    external_identifier: Optional[str] = None, buyer_id: Optional[str] = None
) -> Dict[str, Any]:
    """A ``CardPaymentMethodCreate`` body for the approving mock card."""
    body: Dict[str, Any] = {
        "method": "card",
        "number": APPROVING_CARD_NUMBER,
        "expiration_date": CARD_EXPIRATION_DATE,
        "security_code": CARD_SECURITY_CODE,
    }
    if external_identifier is not None:
        body["external_identifier"] = external_identifier
    if buyer_id is not None:
        body["buyer_id"] = buyer_id
    return body


def sample_address() -> Dict[str, Any]:
    return {
        "city": "London",
        "country": "GB",
        "postal_code": "789",
        "state": "London",
        "house_number_or_name": "10",
        "line1": "Oxford Street",
    }


def sample_billing_details() -> Dict[str, Any]:
    return {
        "first_name": "John",
        "last_name": "Lunn",
        "email_address": "john@example.com",
        "address": sample_address(),
    }


def sample_cart_item(name: str = "T-Shirt") -> Dict[str, Any]:
    return {"name": name, "quantity": 1, "unit_amount": 1299}
