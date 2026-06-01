"""Property-based ("uncertainty") tests — the local analogue of Hypothesis /
fast-check. Each property explores ``gen.RUNS`` generated cases from a fixed seed
(``FC_SEED``), so failures are reproducible. Bounded run counts keep the cost
against the live sandbox low."""

from utils import checkout_fields, gen


def test_amount_and_currency_are_echoed(merchant):
    sdk = merchant.client
    for i in range(gen.RUNS):
        amount = gen.amount()
        currency = gen.currency()
        txn = checkout_fields.authorize(sdk, amount=amount, currency=currency)
        assert txn.amount == amount, f"amount echo (run {i})"
        assert txn.currency == currency, f"currency echo (run {i})"
        assert txn.status == "authorization_succeeded"


def test_metadata_round_trips(merchant):
    sdk = merchant.client
    txn = checkout_fields.authorize(sdk)

    for i in range(gen.RUNS):
        metadata = gen.metadata()
        updated = sdk.transactions.update(transaction_id=txn.id, metadata=metadata)
        for key, value in metadata.items():
            assert key in (updated.metadata or {}), f"metadata key '{key}' (run {i})"
            assert (updated.metadata or {})[key] == value, f"metadata value for '{key}' (run {i})"
