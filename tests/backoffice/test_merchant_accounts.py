"""Merchant accounts: create/get/update(partial)/list, plus the 3DS-configuration
sub-resource (create/update/delete reached at the request level — a real
configuration needs scheme acquirer credentials; list is a happy path)."""

import secrets

from utils import MISSING_ID, reach
from utils.environment import create_client


def test_crud_with_partial_update(merchant):
    # Merchant-account operations are account-level, not merchant-scoped, so
    # drive them with an unscoped (admin) client.
    sdk = create_client(merchant.private_key)
    account_id = secrets.token_hex(8)

    created = sdk.merchant_accounts.create(id=account_id, display_name="Original")
    assert created.id == account_id

    fetched = sdk.merchant_accounts.get(merchant_account_id=account_id)
    assert fetched.id == account_id

    # Partial update: change only display_name.
    updated = sdk.merchant_accounts.update(
        merchant_account_id=account_id, display_name="Renamed"
    )
    assert updated.display_name == "Renamed"
    assert updated.id == account_id

    listed = sdk.merchant_accounts.list()
    assert listed is not None


def test_three_ds_configuration(merchant):
    sdk = merchant.client
    mid = merchant.merchant_account_id

    # list is a happy path (empty until configured).
    listed = sdk.merchant_accounts.three_ds_configuration.list(merchant_account_id=mid)
    assert listed is not None

    reach.reaches(
        lambda: sdk.merchant_accounts.three_ds_configuration.create(
            merchant_account_id=mid,
            merchant_acquirer_bin="411111",
            merchant_acquirer_id="acq-1",
            merchant_name="Acme",
            merchant_country_code="US",
            merchant_category_code="5712",
            merchant_url="https://example.com",
            scheme="visa",
            metadata={},
        ),
        "merchant_accounts.three_ds_configuration.create",
    )
    reach.reaches(
        lambda: sdk.merchant_accounts.three_ds_configuration.update(
            merchant_account_id=mid, three_ds_configuration_id=MISSING_ID
        ),
        "merchant_accounts.three_ds_configuration.update",
    )
    reach.reaches(
        lambda: sdk.merchant_accounts.three_ds_configuration.delete(
            merchant_account_id=mid, three_ds_configuration_id=MISSING_ID
        ),
        "merchant_accounts.three_ds_configuration.delete",
    )
