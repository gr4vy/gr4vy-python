"""Payment methods: full CRUD with a partial-update invariant, list, plus the
network-token and payment-service-token sub-resources (reached at the request
level — they need async network tokens / a live PSP which the mock env lacks)."""

from utils import MISSING_ID, fixtures, reach


def test_crud_with_partial_update(merchant):
    sdk = merchant.client
    ext = fixtures.unique_id("pm", merchant.merchant_account_id)

    created = sdk.payment_methods.create(
        request_body=fixtures.approving_card(external_identifier=ext)
    )
    assert created.id is not None
    assert created.method == "card"

    fetched = sdk.payment_methods.get(payment_method_id=created.id)
    assert fetched.id == created.id

    # Partial update: change only the expiration date.
    updated = sdk.payment_methods.update(
        payment_method_id=created.id, expiration_date="10/40"
    )
    assert updated.expiration_date == "10/40"
    # Untouched fields are preserved.
    assert updated.id == created.id
    assert updated.method == "card"

    listed = sdk.payment_methods.list()
    assert listed is not None

    sdk.payment_methods.delete(payment_method_id=created.id)


def test_network_tokens_are_reached(merchant):
    sdk = merchant.client
    pm = sdk.payment_methods.create(request_body=fixtures.approving_card())

    reach.reaches(
        lambda: sdk.payment_methods.network_tokens.create(
            payment_method_id=pm.id, merchant_initiated=False, is_subsequent_payment=False
        ),
        "payment_methods.network_tokens.create",
    )
    reach.reaches(
        lambda: sdk.payment_methods.network_tokens.list(payment_method_id=pm.id),
        "payment_methods.network_tokens.list",
    )
    reach.reaches(
        lambda: sdk.payment_methods.network_tokens.suspend(
            payment_method_id=pm.id, network_token_id=MISSING_ID
        ),
        "payment_methods.network_tokens.suspend",
    )
    reach.reaches(
        lambda: sdk.payment_methods.network_tokens.resume(
            payment_method_id=pm.id, network_token_id=MISSING_ID
        ),
        "payment_methods.network_tokens.resume",
    )
    reach.reaches(
        lambda: sdk.payment_methods.network_tokens.delete(
            payment_method_id=pm.id, network_token_id=MISSING_ID
        ),
        "payment_methods.network_tokens.delete",
    )
    reach.reaches(
        lambda: sdk.payment_methods.network_tokens.cryptogram.create(
            payment_method_id=pm.id, network_token_id=MISSING_ID, merchant_initiated=False
        ),
        "payment_methods.network_tokens.cryptogram.create",
    )


def test_payment_service_tokens_are_reached(merchant):
    sdk = merchant.client
    pm = sdk.payment_methods.create(request_body=fixtures.approving_card())

    reach.reaches(
        lambda: sdk.payment_methods.payment_service_tokens.create(
            payment_method_id=pm.id,
            payment_service_id=MISSING_ID,
            redirect_url="https://example.com/return",
        ),
        "payment_methods.payment_service_tokens.create",
    )
    reach.reaches(
        lambda: sdk.payment_methods.payment_service_tokens.list(payment_method_id=pm.id),
        "payment_methods.payment_service_tokens.list",
    )
    reach.reaches(
        lambda: sdk.payment_methods.payment_service_tokens.delete(
            payment_method_id=pm.id, payment_service_token_id=MISSING_ID
        ),
        "payment_methods.payment_service_tokens.delete",
    )
