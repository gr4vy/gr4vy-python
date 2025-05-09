import pytest
import requests
from utils.setup import setup_environment, cleanup_environment

@pytest.fixture(scope="module", name='client')
def prepare_client():
    # Setup environment before tests
    client = setup_environment()
    yield client
    # Cleanup environment after tests
    cleanup_environment()

def test_process_payment_with_checkout_session(client):
    checkout_session = client.checkout_sessions.create()
    assert checkout_session.id is not None

    # Direct API call to update checkout session fields
    response = requests.put(
        f"https://api.sandbox.e2e.gr4vy.app/checkout/sessions/{checkout_session.id}/fields",
        headers={"content-type": "application/json"},
        timeout=5000,
        json={
            "payment_method": {
                "method": "card",
                "number": "4111111111111111",
                "expiration_date": "11/25",
                "security_code": "123",
            }
        },
    )
    assert response.status_code == 204

    # Create a transaction using the checkout session
    transaction = client.transactions.create({
        "amount": 1299,
        "currency": "USD",
        "paymentMethod": {
            "method": "checkout-session",
            "id": checkout_session.id,
        },
    })

    assert transaction.id is not None
    assert transaction.status == "authorization_succeeded"
    assert transaction.amount == 1299

# # def test_handle_error_on_missing_card_data(gr4vy):
# #     # Create a checkout session
# #     checkout_session = gr4vy.checkout_sessions.create()
# #     assert checkout_session.id is not None

# #     # Attempt to create a transaction with missing card data
# #     request = {
# #         "amount": 1299,
# #         "currency": "USD",
# #         "paymentMethod": {
# #             "method": "checkout-session",
# #             "id": checkout_session.id,
# #         },
# #     }
# #     with pytest.raises(Exception, match="Request failed validation"):
# #         gr4vy.transactions.create(request)

# # def test_handle_stored_payment_method(gr4vy):
# #     # Create a card payment method
# #     request = CardPaymentMethodCreate(
# #         method="card",
# #         number="4111111111111111",
# #         expirationDate="11/25",
# #         securityCode="123",
# #     )
# #     payment_method = gr4vy.paymentMethods.create(request)
# #     assert payment_method.id is not None

# #     # Create a checkout session
# #     checkout_session = gr4vy.checkout_sessions.create()
# #     assert checkout_session.id is not None

# #     # Direct API call to update checkout session fields
# #     response = requests.put(
# #         f"https://api.sandbox.e2e.gr4vy.app/checkout/sessions/{checkout_session.id}/fields",
# #         headers={"content-type": "application/json"},
# #         json={
# #             "payment_method": {
# #                 "method": "id",
# #                 "id": payment_method.id,
# #                 "security_code": "123",
# #             }
# #         },
# #     )
# #     assert response.status_code == 204

# #     # Create a transaction using the checkout session
# #     transaction = gr4vy.transactions.create({
# #         "amount": 1299,
# #         "currency": "USD",
# #         "paymentMethod": {
# #             "method": "checkout-session",
# #             "id": checkout_session.id,
# #         },
# #     })

# #     assert transaction.id is not None
# #     assert transaction.status == "authorization_succeeded"
# #     assert transaction.amount == 1299
