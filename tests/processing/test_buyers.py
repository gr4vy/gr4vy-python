"""Buyers: CRUD with a partial-update invariant, list, the shipping-details
sub-resource CRUD, and the gift-cards / payment-methods list sub-resources."""

from utils import fixtures


def test_crud_with_partial_update(merchant):
    sdk = merchant.client
    ext = fixtures.unique_id("buyer", merchant.merchant_account_id)

    buyer = sdk.buyers.create(display_name="Original Name", external_identifier=ext)
    assert buyer.id is not None

    fetched = sdk.buyers.get(buyer_id=buyer.id)
    assert fetched.id == buyer.id

    # Partial update: change only display_name.
    updated = sdk.buyers.update(buyer_id=buyer.id, display_name="Renamed Buyer")
    assert updated.display_name == "Renamed Buyer"
    # external_identifier (untouched) is preserved.
    assert updated.external_identifier == ext

    listed = sdk.buyers.list()
    assert listed is not None

    sdk.buyers.delete(buyer_id=buyer.id)


def test_shipping_details_crud(merchant):
    sdk = merchant.client
    buyer = sdk.buyers.create(display_name="Ships A Lot")

    created = sdk.buyers.shipping_details.create(
        buyer_id=buyer.id,
        first_name="Ada",
        last_name="Lovelace",
        address=fixtures.sample_address(),
    )
    assert created.first_name == "Ada"

    fetched = sdk.buyers.shipping_details.get(
        buyer_id=buyer.id, shipping_details_id=created.id
    )
    assert fetched.id == created.id

    listed = sdk.buyers.shipping_details.list(buyer_id=buyer.id)
    assert listed is not None

    # Partial update: change only last_name.
    updated = sdk.buyers.shipping_details.update(
        buyer_id=buyer.id, shipping_details_id=created.id, last_name="Byron"
    )
    assert updated.last_name == "Byron"
    assert updated.first_name == "Ada"

    sdk.buyers.shipping_details.delete(buyer_id=buyer.id, shipping_details_id=created.id)


def test_buyer_list_subresources(merchant):
    sdk = merchant.client
    buyer = sdk.buyers.create(display_name="List Owner")

    gift_cards = sdk.buyers.gift_cards.list(buyer_id=buyer.id)
    assert gift_cards is not None

    payment_methods = sdk.buyers.payment_methods.list(buyer_id=buyer.id)
    assert payment_methods is not None
