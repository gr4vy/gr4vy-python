"""Helpers for the embed-only ``PUT /checkout/sessions/{id}/fields`` endpoint.

This endpoint is not modelled by the SDK (it is a non-public, embed-only field
service), so the tests drive it with a raw HTTP call exactly as a front-end SDK
would. Kept here so the lifecycle flows can attach a card (or a stored method) to
a session before authorizing.
"""

from typing import Any, Dict, Optional

import requests

from gr4vy import Gr4vy

from utils import fixtures
from utils.environment import API_BASE_URL


def _put(session_id: str, body: Dict[str, Any]) -> None:
    response = requests.put(
        f"{API_BASE_URL}/checkout/sessions/{session_id}/fields",
        headers={"content-type": "application/json"},
        json=body,
        timeout=10,
    )
    response.raise_for_status()


def put_card(session_id: str, card: Optional[Dict[str, Any]] = None) -> None:
    """Attach raw approving-card details to a checkout session."""
    payment_method = {
        "method": "card",
        "number": fixtures.APPROVING_CARD_NUMBER,
        "expiration_date": fixtures.CARD_EXPIRATION_DATE,
        "security_code": fixtures.CARD_SECURITY_CODE,
    }
    if card:
        payment_method.update(card)
    _put(session_id, {"payment_method": payment_method})


def put_stored_method(
    session_id: str,
    payment_method_id: str,
    security_code: str = fixtures.CARD_SECURITY_CODE,
) -> None:
    """Attach a stored payment-method id to a checkout session."""
    _put(
        session_id,
        {
            "payment_method": {
                "method": "id",
                "id": payment_method_id,
                "security_code": security_code,
            }
        },
    )


def authorize(sdk: Gr4vy, amount: int = 1299, currency: str = "USD"):
    """Create a checkout session, attach an approving card, authorize a transaction.

    Returns the created transaction.
    """
    session = sdk.checkout_sessions.create()
    put_card(session.id)
    return sdk.transactions.create(
        amount=amount,
        currency=currency,
        payment_method={"method": "checkout-session", "id": session.id},
    )
