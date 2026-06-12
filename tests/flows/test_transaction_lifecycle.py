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


def test_capture_list_and_get(merchant):
    sdk = merchant.client

    # Authorize, then capture the full amount.
    txn = checkout_fields.authorize(sdk, amount=4500, currency="USD")
    assert txn.status == "authorization_succeeded"

    sdk.transactions.capture(transaction_id=txn.id, amount=4500)
    poll.until(
        lambda: sdk.transactions.get(transaction_id=txn.id),
        lambda t: t.captured_amount == 4500,
        description="transaction captured",
    )

    # List captures, then read one back by id.
    captures = sdk.transactions.captures.list(transaction_id=txn.id)
    assert len(captures.items) >= 1

    capture_id = captures.items[0].id
    fetched = sdk.transactions.captures.get(
        transaction_id=txn.id, capture_id=capture_id
    )
    assert fetched.id == capture_id


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
