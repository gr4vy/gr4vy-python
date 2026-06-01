"""Refunds: a partial refund on a captured transaction (create -> get -> list),
plus the top-level refunds.get lookup."""

from utils import MISSING_ID, checkout_fields, poll, reach


def test_partial_refund_create_get_list(merchant):
    sdk = merchant.client

    # Authorize + capture so the transaction is refundable.
    txn = checkout_fields.authorize(sdk, amount=2000)
    sdk.transactions.capture(transaction_id=txn.id, amount=2000)
    poll.until(
        lambda: sdk.transactions.get(transaction_id=txn.id),
        lambda t: t.captured_amount == 2000,
        description="transaction captured before refund",
    )

    # Partial refund.
    refund = sdk.transactions.refunds.create(
        transaction_id=txn.id, amount=500, reason="partial"
    )
    assert refund.id is not None

    fetched = sdk.transactions.refunds.get(transaction_id=txn.id, refund_id=refund.id)
    assert fetched.id == refund.id

    listed = sdk.transactions.refunds.list(transaction_id=txn.id)
    assert listed is not None

    # Top-level refund lookup.
    top = sdk.refunds.get(refund_id=refund.id)
    assert top.id == refund.id


def test_refund_get_missing_is_reached(merchant):
    sdk = merchant.client
    reach.reaches(lambda: sdk.refunds.get(refund_id=MISSING_ID), "refunds.get")
