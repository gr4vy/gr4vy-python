"""Transactions resource: create/get/list/update plus the read sub-resources
(actions, events, settlements, refund settlements) and the cancel action. Capture / void / refund /
sync are covered as a story in flows/test_transaction_lifecycle.py."""

from utils import MISSING_ID, checkout_fields, fixtures, reach


def test_create_get_list(merchant):
    sdk = merchant.client
    txn = checkout_fields.authorize(sdk)

    fetched = sdk.transactions.get(transaction_id=txn.id)
    assert fetched.id == txn.id

    listed = sdk.transactions.list()
    assert listed is not None


def test_update_metadata_is_partial(merchant):
    sdk = merchant.client
    txn = checkout_fields.authorize(sdk)
    ext = fixtures.unique_id("txn", merchant.merchant_account_id)

    updated = sdk.transactions.update(
        transaction_id=txn.id,
        external_identifier=ext,
        metadata={"source": "e2e", "tier": "gold"},
    )

    # The changed field took effect; the amount (untouched) is unchanged.
    assert updated.external_identifier == ext
    assert updated.amount == txn.amount


def test_read_subresources(merchant):
    sdk = merchant.client
    txn = checkout_fields.authorize(sdk)

    actions = sdk.transactions.actions.list(transaction_id=txn.id)
    assert actions is not None

    events = sdk.transactions.events.list(transaction_id=txn.id)
    assert events is not None

    settlements = sdk.transactions.settlements.list(transaction_id=txn.id)
    assert settlements is not None

    # A specific settlement needs a settled transaction we cannot force here.
    reach.reaches(
        lambda: sdk.transactions.settlements.get(
            transaction_id=txn.id, settlement_id=MISSING_ID
        ),
        "transactions.settlements.get",
    )

    refund_settlements = sdk.transactions.refund_settlements.list(
        transaction_id=txn.id
    )
    assert refund_settlements is not None

    # A specific refund settlement needs a settled transaction we cannot force here.
    reach.reaches(
        lambda: sdk.transactions.refund_settlements.get(
            transaction_id=txn.id, settlement_id=MISSING_ID
        ),
        "transactions.refund_settlements.get",
    )


def test_cancel_is_reached(merchant):
    sdk = merchant.client
    # Cancelling a not-found transaction still exercises the endpoint.
    reach.reaches(
        lambda: sdk.transactions.cancel(transaction_id=MISSING_ID),
        "transactions.cancel",
    )
