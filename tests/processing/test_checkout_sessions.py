"""Checkout sessions: full CRUD (create/get/update/delete) plus the two headline
field-attachment flows — raw card details and a stored payment method — each
driven through to an authorized transaction."""

from utils import checkout_fields, fixtures


def test_crud(merchant):
    sdk = merchant.client

    session = sdk.checkout_sessions.create()
    assert session.id is not None

    fetched = sdk.checkout_sessions.get(session_id=session.id)
    assert fetched.id == session.id

    updated = sdk.checkout_sessions.update(session_id=session.id, metadata={"source": "e2e"})
    assert updated.id == session.id

    sdk.checkout_sessions.delete(session_id=session.id)


def test_authorize_with_raw_card(merchant):
    sdk = merchant.client
    txn = checkout_fields.authorize(sdk, amount=1299)
    assert txn.status == "authorization_succeeded"
    assert txn.amount == 1299


def test_authorize_with_stored_method(merchant):
    sdk = merchant.client

    pm = sdk.payment_methods.create(request_body=fixtures.approving_card())
    session = sdk.checkout_sessions.create()
    checkout_fields.put_stored_method(session.id, pm.id)

    txn = sdk.transactions.create(
        amount=1299,
        currency="USD",
        payment_method={"method": "checkout-session", "id": session.id},
    )
    assert txn.status == "authorization_succeeded"
