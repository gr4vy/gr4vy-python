from gr4vy_api.openapi_client.model.buyer_request import BuyerRequest
from gr4vy_api.openapi_client.model.buyer_update import BuyerUpdate
from gr4vy_api.openapi_client.model.payment_method import PaymentMethod
from gr4vy_api.openapi_client.model.payment_service_request import PaymentServiceRequest
from gr4vy_api.openapi_client.model.payment_service_update import PaymentServiceUpdate
from gr4vy_api.openapi_client.model.transaction_capture_request import TransactionCaptureRequest
from gr4vy_api.openapi_client.model.transaction_refund_request import TransactionRefundRequest
from gr4vy_api.openapi_client.model.transaction_request import TransactionRequest
from gr4vy_python import Gr4vyClient
from gr4vy_python import Gr4vyClientWithBaseUrl

gr4vy_id = "YOURGR4VYID"
private_key_location = "PRIVATE_KEY_LOCATION"

client = Gr4vyClient(gr4vy_id,private_key_location)

buyer_request = BuyerRequest(display_name="Testing")
buyer_id = client.AddBuyer(buyer_request).id

method = {
  "method": "card",
  "number": "4111111111111111",
  "expiration_date": "11/25",
  "security_code": "123"
}
payment_method = PaymentMethod(**method)
payment_method_id = client.StorePaymentMethod(payment_method).id

payment_service = {
"id": "faaad066-30b4-4997-a438-242b0752d7e1",
"type": "payment-service",
"payment_service_definition_id": "stripe",
"method": "card",
"display_name": "Stripe",
"status": "pending",
"accepted_currencies": [
"EUR"
],
"accepted_countries": [
"DE"
],
"environment": "production"
}

payment_service_request = PaymentServiceRequest(**payment_service
)

payment_service_request = PaymentServiceRequest(**payment_service)
payment_service_id = client.AddPaymentService(payment_service_request).id


transaction_request = {
  "amount": 1299,
  "currency": "USD",
  "payment_method": {
    "method": "card",
    "number": "4111111111111111",
    "expiration_date": "11/25",
    "security_code": "123",
    "redirect_url": "https://example.com/callback"
  }
}

transaction_request = TransactionRequest(**transaction_request)
transaction_id = client.AuthorizeNewTransaction(transaction_request).id


def testCreateClient():
    assert client

def testprivate_key_file_to_string():
    assert Gr4vyClient.private_key_file_to_string()

def testGenerateToken():
    assert client.GenerateToken()

def testGenerateEmbedToken():
    embed = {"amount": 1299,
            "currency": "USD",
            "buyerId": buyer_id,
            } 
    assert client.GenerateEmbedToken(embed)

def testGetBuyer():
    assert client.GetBuyer(buyer_id)

def testListBuyers():
    client.ListBuyers()

def testAddBuyer():
    buyer_request = BuyerRequest(display_name="Test")
    assert client.AddBuyer(buyer_request)

def testUpdateBuyer():
    buyer_update = BuyerUpdate(buyer_id,display_name="Test")
    assert client.UpdateBuyer(buyer_id, buyer_update)
'''
def testGetPaymentMethod():
    assert client.GetPaymentMethod(payment_method_id)

def testListBuyerPaymentMethods():
    assert client.ListBuyerPaymentMethods(buyer_id)

def testListPaymentMethods():
    assert client.ListPaymentMethods()

def testStorePaymentMethod():
    assert client.StorePaymentMethod(payment_method)

def testDeletePaymentMethod():
    assert client.DeletePaymentMethod(payment_method_id)
'''
def testListPaymentMethodTokens():
    assert client.listPaymentMethodTokens(payment_method_id)


def testListPaymentOptions():
    assert client.ListPaymentOptions()

def testGetPaymentServiceDefinition():
    payment_service_definition_id = client.ListPaymentServiceDefintions(limit=1)["items"][0]["id"]
    assert client.GetPaymentServiceDefinition(payment_service_definition_id)

def testListPaymentServiceDefintions():
    assert client.ListPaymentServiceDefintions()

def testListPaymentServices():
    assert client.ListPaymentServices()

def testAddPaymentService():
    assert client.AddPaymentService(payment_service_request)

def testGetPaymentService():
    assert client.GetPaymentService(payment_service_id)

def testUpdatePaymentService():
    payment_service_update = PaymentServiceUpdate(payment_service)
    assert client.UpdatePaymentService(payment_service_update)

def testAuthorizeNewTransaction():
    assert client.AuthorizeNewTransaction(transaction_request)

def testCaptureTransaction():
    transaction_capture = {
        "amount": 1299,
        "currency": "USD"
    }
    transaction_capture_request = TransactionCaptureRequest(**transaction_capture)
    assert client.CaptureTransaction(transaction_id, transaction_capture_request)

def testGetTransaction():
    assert client.GetTransaction(transaction_id)

def testListTransactions():
    assert client.ListTransactions()

def RefundTransaction():
    assert client.RefundTransaction(transaction_id)

class testGr4vyClientWithBaseUrl(Gr4vyClient):
    assert Gr4vyClientWithBaseUrl("https://spider.gr4vy.app", "private_key.pem")

def testDeleteBuyer():
    assert client.DeleteBuyer(buyer_id)

def testDeletePaymentService():
    assert client.DeletePaymentService(payment_service_id)

'''
def testDeletePaymentMethod():
    assert client.DeletePaymentMethod(payment_method_id)
'''