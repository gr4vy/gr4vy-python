import pytest
import requests
from gr4vy import models
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
    transaction: models.Transaction = client.transactions.create(
        amount=1299,
        currency="USD",
        payment_method={
            "method": "checkout-session",
            "id": checkout_session.id,
        }
    )

    assert transaction.id is not None
    assert transaction.status == "authorization_succeeded"
    assert transaction.amount == 1299

def test_handle_error_on_missing_card_data(client):
    # Create a checkout session
    checkout_session = client.checkout_sessions.create()
    assert checkout_session.id is not None

    # Attempt to create a transaction with missing card data
    with pytest.raises(Exception, match="Request failed validation"):
        client.transactions.create(
            amount=1299,
            currency="USD",
            payment_method={
               "method": "checkout-session",
               "id": checkout_session.id,
            }
        )

def test_handle_stored_payment_method(client):
    # Create a card payment method
    request = models.CardPaymentMethodCreate(
        number="4111111111111111",
        expiration_date="11/25",
        security_code="123",
    )
    payment_method = client.payment_methods.create(request_body=request)
    assert payment_method.id is not None

    # Create a checkout session
    checkout_session = client.checkout_sessions.create()
    assert checkout_session.id is not None

    # Direct API call to update checkout session fields
    response = requests.put(
        f"https://api.sandbox.e2e.gr4vy.app/checkout/sessions/{checkout_session.id}/fields",
        headers={"content-type": "application/json"},
        timeout=5000,
        json={
            "payment_method": {
                "method": "id",
                "id": payment_method.id,
                "security_code": "123",
            }
        },
    )
    assert response.status_code == 204

    # Create a transaction using the checkout session
    transaction = client.transactions.create(
        amount=1299,
        currency="USD",
        payment_method={
            "method": "checkout-session",
            "id": checkout_session.id,
        },
    )

    assert transaction.id is not None
    assert transaction.status == "authorization_succeeded"
    assert transaction.amount == 1299
