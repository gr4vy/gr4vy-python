"""Buyer-centric story: create a buyer, store a card on it, add shipping details,
then reuse the stored method (via a checkout session) to authorize a payment."""

from utils import checkout_fields, fixtures


def test_buyer_with_stored_method_and_shipping(merchant):
    sdk = merchant.client
    ext = fixtures.unique_id("buyer", merchant.merchant_account_id)

    # Create the buyer.
    buyer = sdk.buyers.create(
        display_name="Jane Doe",
        external_identifier=ext,
        billing_details=fixtures.sample_billing_details(),
    )
    assert buyer.id is not None
    assert buyer.display_name == "Jane Doe"

    # Store a card against the buyer.
    pm = sdk.payment_methods.create(request_body=fixtures.approving_card(buyer_id=buyer.id))
    assert pm.id is not None

    # It shows up in the buyer's payment-method list.
    listed = sdk.buyers.payment_methods.list(buyer_id=buyer.id)
    assert listed is not None

    # Add shipping details.
    shipping = sdk.buyers.shipping_details.create(
        buyer_id=buyer.id,
        first_name="Jane",
        last_name="Doe",
        email_address="jane@example.com",
        address=fixtures.sample_address(),
    )
    assert shipping.first_name == "Jane"

    # Reuse the stored method through a checkout session to authorize a payment.
    session = sdk.checkout_sessions.create()
    checkout_fields.put_stored_method(session.id, pm.id)
    txn = sdk.transactions.create(
        amount=1299,
        currency="USD",
        payment_method={"method": "checkout-session", "id": session.id},
        buyer_id=buyer.id,
    )
    assert txn.status == "authorization_succeeded"
    assert txn.amount == 1299
