"""Payouts: list is a happy path; create/get need a payout-capable payment
service the mock env does not provide, so they are reached at the request level."""

from utils import MISSING_ID, fixtures, reach


def test_list_is_happy_path(merchant):
    sdk = merchant.client
    listed = sdk.payouts.list()
    assert listed is not None


def test_create_get_are_reached(merchant):
    sdk = merchant.client
    pm = sdk.payment_methods.create(request_body=fixtures.approving_card())

    reach.reaches(
        lambda: sdk.payouts.create(
            amount=1000,
            currency="USD",
            payment_service_id=MISSING_ID,
            payment_method={"method": "id", "id": pm.id},
        ),
        "payouts.create",
    )
    reach.reaches(lambda: sdk.payouts.get(payout_id=MISSING_ID), "payouts.get")
