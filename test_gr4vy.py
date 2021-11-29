from gr4vy import Gr4vyClient, Gr4vyClientWithBaseUrl
from gr4vy.gr4vy_api.openapi_client.model.buyer_request import BuyerRequest
from gr4vy.gr4vy_api.openapi_client.model.buyer_update import BuyerUpdate
from gr4vy.gr4vy_api.openapi_client.model.payment_method import PaymentMethod
from gr4vy.gr4vy_api.openapi_client.model.payment_method_request import (
    PaymentMethodRequest,
)
from gr4vy.gr4vy_api.openapi_client.model.payment_service_request import (
    PaymentServiceRequest,
)
from gr4vy.gr4vy_api.openapi_client.model.payment_service_update import (
    PaymentServiceUpdate,
)
from gr4vy.gr4vy_api.openapi_client.model.payment_service_update_fields import (
    PaymentServiceUpdateFields,
)
from gr4vy.gr4vy_api.openapi_client.model.transaction_capture_request import (
    TransactionCaptureRequest,
)
from gr4vy.gr4vy_api.openapi_client.model.transaction_payment_method_request import (
    TransactionPaymentMethodRequest,
)
from gr4vy.gr4vy_api.openapi_client.model.transaction_refund_request import (
    TransactionRefundRequest,
)
from gr4vy.gr4vy_api.openapi_client.model.transaction_request import TransactionRequest

gr4vy_id = "example009"
private_key_location = "./private_key.pem"
environment = "sandbox"
client = Gr4vyClient(gr4vy_id, private_key_location, environment=environment)
client.configuration.debug = True

def testCreateClient():
    assert client

def testGr4vyClientWithBaseUrl():
    assert Gr4vyClientWithBaseUrl("https://{}.gr4vy.app".format(gr4vy_id), "private_key.pem", environment=environment)

def testprivate_key_file_to_string():
    assert client.private_key_file_to_string()

def testGenerateToken():
    assert client.GenerateToken()

def testGenerateEmbedToken():
    buyer_id = client.ListBuyers()["items"][0]["id"]
    embed = {
        "amount": 1299,
        "currency": "USD",
        "buyerId": buyer_id,
    }
    assert client.GenerateEmbedToken(embed)


def testListBuyers():
    assert client.ListBuyers()


def testAddBuyer():
    buyer_request = BuyerRequest(display_name="Test")
    buyer_id = client.AddBuyer(buyer_request)["id"]
    assert buyer_id


def testGetBuyer():
    for buyer in client.ListBuyers()["items"]:
        if buyer["display_name"] == "Test":
            buyer_id = buyer["id"]
    assert client.GetBuyer(buyer_id)


def testUpdateBuyer():
    for buyer in client.ListBuyers()["items"]:
        if buyer["display_name"] == "Test":
            buyer_id = buyer["id"]

    buyer_update = BuyerUpdate()
    assert client.UpdateBuyer(buyer_id, buyer_update)


def testListBuyerPaymentMethods():
    for buyer in client.ListBuyers()["items"]:
        if buyer["display_name"] == "Test":
            buyer_id = buyer["id"]

    assert client.ListBuyerPaymentMethods(buyer_id=buyer_id)


def testDeleteBuyer():
    for buyer in client.ListBuyers()["items"]:
        if buyer["display_name"] == "Test":
            buyer_id = buyer["id"]

    try:
        client.DeleteBuyer(buyer_id)
    except KeyError:
        print("No buyer's to delete")
        assert False


def testListPaymentMethods():
    assert client.ListPaymentMethods()


def testStorePaymentMethod():
    payment_method_request = PaymentMethodRequest(
        method="card",
        number="4111111111111111",
        expiration_date="11/25",
        security_code="123",
    )
    payment_method = client.StorePaymentMethod(payment_method_request)
    assert payment_method.id


def testGetPaymentMethod():
    payment_method_id = client.ListPaymentMethods()["items"][0]["id"]
    assert client.GetPaymentMethod(payment_method_id)


def testListPaymentMethodTokens():
    payment_method_request = PaymentMethodRequest(
        method="card",
        number="4111111111111111",
        expiration_date="11/25",
        security_code="123",
    )
    payment_method = client.StorePaymentMethod(payment_method_request)
    assert payment_method.id
    # print(payment_method.id)
    res = client.ListPaymentMethodTokens(payment_method.id)
    # print(res)
    assert res


def testDeletePaymentMethod():
    payment_method_id = client.ListPaymentMethods()["items"][0]["id"]
    assert client.DeletePaymentMethod(payment_method_id) == None


def testListPaymentOptions():
    req = client.ListPaymentOptions()
    assert req


def testGetPaymentServiceDefinition():
    payment_service_definitions = client.ListPaymentServiceDefintions(limit=1)
    assert client.GetPaymentServiceDefinition(
        payment_service_definitions["items"][0]["id"]
    )


def testListPaymentServiceDefintions():
    assert client.ListPaymentServiceDefintions()


def testListPaymentServices():
    assert client.ListPaymentServices()


def testAddPaymentService():
    api_key = PaymentServiceUpdateFields(key="api_key", value="12345678")
    merchant_account = PaymentServiceUpdateFields(
        key="merchant_account", value="12345678"
    )
    live_endpoint_prefix = PaymentServiceUpdateFields(
        key="live_endpoint_prefix", value="phillip"
    )
    payment_service_definition_id = "adyen-card"
    payment_service_request = PaymentServiceRequest(
        display_name="TestAddService",
        fields=[api_key, merchant_account, live_endpoint_prefix],
        accepted_countries=["US"],
        accepted_currencies=["USD"],
        payment_service_definition_id=payment_service_definition_id,
        three_d_secure_enabled=False,
    )
    payment_service_id = client.AddPaymentService(payment_service_request)["id"]
    assert payment_service_id


def testGetPaymentService():
    for payment_service in client.ListPaymentServices()["items"]:
        if payment_service["display_name"] == "TestAddService":
            payment_service_id = payment_service["id"]
    assert client.GetPaymentService(payment_service_id)


def testUpdatePaymentService():
    for payment_service in client.ListPaymentServices()["items"]:
        if payment_service["display_name"] == "TestAddService":
            payment_service_id = payment_service["id"]

    api_key = PaymentServiceUpdateFields(key="api_key", value="12345678")
    merchant_account = PaymentServiceUpdateFields(
        key="merchant_account", value="12345678"
    )
    live_endpoint_prefix = PaymentServiceUpdateFields(
        key="live_endpoint_prefix", value="testing"
    )

    payment_service_update = PaymentServiceUpdate(
        display_name="TestAddService",
        fields=[api_key, merchant_account, live_endpoint_prefix],
        accepted_countries=["US"],
        accepted_currencies=["USD"],
        three_d_secure_enabled=False,
    )

    assert client.UpdatePaymentService(
        payment_service_id=payment_service_id,
        payment_service_update=payment_service_update,
    )


def testDeletePaymentService():
    for payment_service in client.ListPaymentServices()["items"]:
        if payment_service["display_name"] == "TestAddService":
            payment_service_id = payment_service["id"]

    if client.DeletePaymentService(payment_service_id) == None:
        assert True
    else:
        assert False


def testListTransactions():
    assert client.ListTransactions()


def testAuthorizeNewTransaction():
    transaction_request = TransactionRequest(
        amount=1299,
        currency="USD",
        payment_method=TransactionPaymentMethodRequest(
            method="card",
            number="4111111111111111",
            expiration_date="11/25",
            security_code="123",
            redirect_url="https://example.com/callback",
        ),
    )
    transaction_id = client.AuthorizeNewTransaction(transaction_request)["id"]
    assert transaction_id


def testCaptureTransaction():
    transaction_request = TransactionRequest(
        amount=1299,
        currency="USD",
        payment_method=TransactionPaymentMethodRequest(
            method="card",
            number="4111111111111111",
            expiration_date="11/25",
            security_code="123",
            redirect_url="https://example.com/callback",
        ),
    )
    transaction_id = client.AuthorizeNewTransaction(transaction_request)["id"]

    transaction_capture_request = TransactionCaptureRequest(amount=1299)
    assert client.CaptureTransaction(transaction_id, transaction_capture_request)


def testGetTransaction():
    transaction_id = client.ListTransactions()["items"][0]["id"]
    assert client.GetTransaction(transaction_id)


def testRefundTransaction():
    transaction_request = TransactionRequest(
        amount=1299,
        currency="USD",
        payment_method=TransactionPaymentMethodRequest(
            method="card",
            number="4111111111111111",
            expiration_date="11/25",
            security_code="123",
            redirect_url="https://example.com/callback",
        ),
    )
    transaction = client.AuthorizeNewTransaction(transaction_request)

    print("===")
    print(transaction)
    print("===")
    transaction_refund_request = TransactionRefundRequest(amount=10)
    assert client.RefundTransaction(
        transaction.id, transaction_refund_request=transaction_refund_request
    )
