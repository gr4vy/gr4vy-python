"""API key pairs: list is a happy path; create/get/update/delete are reached at
the request level. Creating a key pair requires a real, existing role whose
scopes are a subset of the caller's — the mock env has no such role to assign, so
create is rejected with a 4xx (endpoint still reached), and get/update/delete
target a MISSING_ID that returns a 4xx as well."""

from utils import MISSING_ID, reach
from utils.environment import create_client


def test_list_is_happy_path(merchant):
    # API key pairs are an account-level resource (a pair can span every merchant
    # account), so drive them with an unscoped (admin) client, like
    # merchant_accounts — not the merchant-scoped merchant.client.
    sdk = create_client(merchant.private_key)
    listed = sdk.api_key_pairs.list()
    assert listed is not None


def test_create_get_update_delete_are_reached(merchant):
    sdk = create_client(merchant.private_key)

    # create needs a valid role_id whose scopes are a subset of the caller's;
    # MISSING_ID is not a real role, so the API rejects it with a 4xx. The
    # endpoint is still reached.
    reach.reaches(
        lambda: sdk.api_key_pairs.create(
            display_name="e2e-test-key-pair",
            role_ids=[MISSING_ID],
        ),
        "api_key_pairs.create",
    )
    reach.reaches(
        lambda: sdk.api_key_pairs.get(api_key_pair_id=MISSING_ID),
        "api_key_pairs.get",
    )
    reach.reaches(
        lambda: sdk.api_key_pairs.update(
            api_key_pair_id=MISSING_ID, display_name="renamed"
        ),
        "api_key_pairs.update",
    )
    reach.reaches(
        lambda: sdk.api_key_pairs.delete(api_key_pair_id=MISSING_ID),
        "api_key_pairs.delete",
    )
