"""Digital wallets. Registering a real wallet needs provider credentials the mock
env lacks, so create/get/update/delete + domains + sessions are reached at the
request level; list is a real happy path (empty page)."""

from utils import MISSING_ID, reach


def test_list_is_happy_path(merchant):
    sdk = merchant.client
    listed = sdk.digital_wallets.list()
    assert listed is not None


def test_crud_is_reached(merchant):
    sdk = merchant.client

    reach.reaches(
        lambda: sdk.digital_wallets.create(
            provider="google", merchant_name="Acme", accept_terms_and_conditions=True
        ),
        "digital_wallets.create",
    )
    reach.reaches(
        lambda: sdk.digital_wallets.get(digital_wallet_id=MISSING_ID),
        "digital_wallets.get",
    )
    reach.reaches(
        lambda: sdk.digital_wallets.update(digital_wallet_id=MISSING_ID, merchant_name="Acme"),
        "digital_wallets.update",
    )
    reach.reaches(
        lambda: sdk.digital_wallets.delete(digital_wallet_id=MISSING_ID),
        "digital_wallets.delete",
    )


def test_domains_are_reached(merchant):
    sdk = merchant.client
    reach.reaches(
        lambda: sdk.digital_wallets.domains.create(
            digital_wallet_id=MISSING_ID, domain_name="example.com"
        ),
        "digital_wallets.domains.create",
    )
    reach.reaches(
        lambda: sdk.digital_wallets.domains.delete(
            digital_wallet_id=MISSING_ID, domain_name="example.com"
        ),
        "digital_wallets.domains.delete",
    )


def test_sessions_are_reached(merchant):
    sdk = merchant.client
    reach.reaches(
        lambda: sdk.digital_wallets.sessions.apple_pay(
            validation_url="https://apple.example/validate", domain_name="example.com"
        ),
        "digital_wallets.sessions.apple_pay",
    )
    reach.reaches(
        lambda: sdk.digital_wallets.sessions.google_pay(origin_domain="example.com"),
        "digital_wallets.sessions.google_pay",
    )
    reach.reaches(
        lambda: sdk.digital_wallets.sessions.click_to_pay(checkout_session_id=MISSING_ID),
        "digital_wallets.sessions.click_to_pay",
    )


def test_paze_sessions_are_reached(merchant):
    sdk = merchant.client

    reach.reaches(
        lambda: sdk.digital_wallets.sessions.paze(domain_name="example.com"),
        "digital_wallets.sessions.paze",
    )
    reach.reaches(
        lambda: sdk.digital_wallets.sessions.paze_mobile_session_create(
            client={"id": "test"},
            session_id=MISSING_ID,
            access_token="token",
            callback_url_scheme="app",
            intent="checkout",
        ),
        "digital_wallets.sessions.paze_mobile_session_create",
    )
    reach.reaches(
        lambda: sdk.digital_wallets.sessions.paze_mobile_session_review(
            session_id=MISSING_ID, code="code", access_token="token"
        ),
        "digital_wallets.sessions.paze_mobile_session_review",
    )
    reach.reaches(
        lambda: sdk.digital_wallets.sessions.paze_mobile_session_complete(
            session_id=MISSING_ID, code="code", access_token="token", transaction_type="purchase"
        ),
        "digital_wallets.sessions.paze_mobile_session_complete",
    )
