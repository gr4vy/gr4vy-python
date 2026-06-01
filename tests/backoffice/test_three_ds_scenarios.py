"""3DS scenarios: create -> list -> update -> delete. Creation requires a 3DS
service configured on the merchant; the mock env has none, so create / update /
delete are reached at the request level and list is a happy path."""

from utils import MISSING_ID, reach


def test_list_is_happy_path(merchant):
    sdk = merchant.client
    listed = sdk.three_ds_scenarios.list()
    assert listed is not None


def test_create_update_delete_are_reached(merchant):
    sdk = merchant.client

    reach.reaches(
        lambda: sdk.three_ds_scenarios.create(
            conditions={"amount": 1000},
            outcome={"authentication": {"transaction_status": "Y"}},
        ),
        "three_ds_scenarios.create",
    )
    reach.reaches(
        lambda: sdk.three_ds_scenarios.update(three_ds_scenario_id=MISSING_ID),
        "three_ds_scenarios.update",
    )
    reach.reaches(
        lambda: sdk.three_ds_scenarios.delete(three_ds_scenario_id=MISSING_ID),
        "three_ds_scenarios.delete",
    )
