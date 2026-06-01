"""Gift cards. The mock merchant has no gift-card service configured, so create /
get / delete / balances are reached at the request level (they cleanly 4xx); list
is a real happy path (it returns an empty page)."""

from utils import MISSING_ID, reach


def test_list_is_happy_path(merchant):
    sdk = merchant.client
    listed = sdk.gift_cards.list()
    assert listed is not None


def test_create_get_delete_balances_are_reached(merchant):
    sdk = merchant.client

    reach.reaches(
        lambda: sdk.gift_cards.create(number="4111111111111111", pin="1234"),
        "gift_cards.create",
    )
    reach.reaches(lambda: sdk.gift_cards.get(gift_card_id=MISSING_ID), "gift_cards.get")
    reach.reaches(lambda: sdk.gift_cards.delete(gift_card_id=MISSING_ID), "gift_cards.delete")
    reach.reaches(
        lambda: sdk.gift_cards.balances.list(
            items=[{"number": "4111111111111111", "pin": "1234"}]
        ),
        "gift_cards.balances.list",
    )
