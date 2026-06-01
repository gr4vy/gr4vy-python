"""The headline merchant story: checkout -> authorize -> capture -> refund, plus
a second transaction that is authorized then voided, plus sync. Asserts the
status transitions and amounts the way a real integrator would observe them."""

from utils import checkout_fields, poll, reach


def test_authorize_capture_refund(merchant):
    sdk = merchant.client

    # 1. Authorize via a checkout session + approving card.
    txn = checkout_fields.authorize(sdk, amount=1299, currency="USD")
    assert txn.id is not None
    assert txn.status == "authorization_succeeded"
    assert txn.amount == 1299

    # 2. Capture the full amount, then confirm it settles.
    sdk.transactions.capture(transaction_id=txn.id, amount=1299)
    captured = poll.until(
        lambda: sdk.transactions.get(transaction_id=txn.id),
        lambda t: t.captured_amount == 1299,
        description="transaction captured",
    )
    assert captured.captured_amount == 1299

    # 3. Refund it in full, then confirm the refund lands.
    full = sdk.transactions.refunds.all.create(
        transaction_id=txn.id, reason="customer request"
    )
    assert full is not None
    refunded = poll.until(
        lambda: sdk.transactions.get(transaction_id=txn.id),
        lambda t: t.refunded_amount == 1299,
        description="transaction refunded",
    )
    assert refunded.refunded_amount == 1299


def test_authorize_then_void(merchant):
    sdk = merchant.client

    txn = checkout_fields.authorize(sdk, amount=555, currency="USD")
    assert txn.status == "authorization_succeeded"

    # Void the (uncaptured) authorization.
    sdk.transactions.void(transaction_id=txn.id)
    voided = poll.until(
        lambda: sdk.transactions.get(transaction_id=txn.id),
        lambda t: "void" in t.status,
        description="transaction voided",
    )
    assert "void" in voided.status


def test_sync_is_reached(merchant):
    sdk = merchant.client

    txn = checkout_fields.authorize(sdk, amount=700, currency="USD")
    # The mock-card connector does not support sync, so the endpoint returns a
    # client error — assert it is reached rather than expecting a 2xx.
    reach.reaches(lambda: sdk.transactions.sync(transaction_id=txn.id), "transactions.sync")
