# openapi_client.TransactionsApi

All URIs are relative to *https://api.plantly.gr4vy.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**authorize_new_transaction**](TransactionsApi.md#authorize_new_transaction) | **POST** /transactions | New transaction
[**capture_transaction**](TransactionsApi.md#capture_transaction) | **POST** /transactions/{transaction_id}/capture | Capture transaction
[**get_transaction**](TransactionsApi.md#get_transaction) | **GET** /transactions/{transaction_id} | Get transaction
[**get_transaction_refund**](TransactionsApi.md#get_transaction_refund) | **GET** /transactions/{transaction_id}/refunds/{refund_id} | Get transaction refund
[**list_transaction_refunds**](TransactionsApi.md#list_transaction_refunds) | **GET** /transactions/{transaction_id}/refunds | List transaction refunds
[**list_transactions**](TransactionsApi.md#list_transactions) | **GET** /transactions | List transactions
[**refund_transaction**](TransactionsApi.md#refund_transaction) | **POST** /transactions/{transaction_id}/refunds | Refund transaction
[**refund_transaction_deprecated**](TransactionsApi.md#refund_transaction_deprecated) | **POST** /transactions/{transaction_id}/refund | Refund or void transactions
[**void_transaction**](TransactionsApi.md#void_transaction) | **POST** /transactions/{transaction_id}/void | Void transaction


# **authorize_new_transaction**
> Transaction authorize_new_transaction()

New transaction

Attempts to create an authorization for a payment method. In some cases it is not possible to create the authorization without redirecting the user for their authorization. In these cases the status is set to `buyer_approval_pending` and an `approval_url` is returned.  Additionally, this endpoint accepts a few additional fields that allow for simultaneous capturing and storage of the payment method.  * `store` - Use this field to store the payment method for future use. Not all payment methods support this feature. * `capture` - Use this method to also perform a capture of the transaction after it has been authorized. 

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import time
import openapi_client
from openapi_client.api import transactions_api
from openapi_client.model.error_generic import ErrorGeneric
from openapi_client.model.transaction import Transaction
from openapi_client.model.transaction_request import TransactionRequest
from openapi_client.model.error401_unauthorized import Error401Unauthorized
from pprint import pprint
# Defining the host is optional and defaults to https://api.plantly.gr4vy.app
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.plantly.gr4vy.app"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): BearerAuth
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = transactions_api.TransactionsApi(api_client)
    transaction_request = TransactionRequest(
        amount=1299,
        currency="USD",
        payment_method=TransactionPaymentMethodRequest(
            method=None,
            number="4111111111111111",
            expiration_date="11/15",
            security_code="123",
            external_identifier="user-789123",
            buyer_id="fe26475d-ec3e-4884-9553-f7356683f7f9",
            buyer_external_identifier="user-789123",
            redirect_url="https://example.com/callback",
            id="77a76f7e-d2de-4bbc-ada9-d6a0015e6bd5",
        ),
        store=True,
        intent="capture",
        external_identifier="user-789123",
        three_d_secure_data=ThreeDSecureDataV1V2(),
        merchant_initiated=True,
        payment_source="ecommerce",
        is_subsequent_payment=True,
        metadata={
            "key": "key_example",
        },
        statement_descriptor=None,
        cart_items=[
            CartItem(
                name="GoPro HERO9 Camcorder",
                quantity=1,
                unit_amount=37999,
                discount_amount=0,
                tax_amount=0,
                external_identifier="item-789123",
                sku="sku-789123",
                product_url="https://example.com/items/gopro",
                image_url="https://example.com/images/items/gopro.png",
                categories=[
                    "categories_example",
                ],
                product_type="physical",
            ),
        ],
        previous_scheme_transaction_id="123456789012345",
    ) # TransactionRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # New transaction
        api_response = api_instance.authorize_new_transaction(transaction_request=transaction_request)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TransactionsApi->authorize_new_transaction: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_request** | [**TransactionRequest**](TransactionRequest.md)|  | [optional]

### Return type

[**Transaction**](Transaction.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Returns the created transaction. |  -  |
**400** | Returns an error if the request was badly formatted or missing required fields. |  -  |
**401** | Returns an error if no valid authentication was provided. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **capture_transaction**
> Transaction capture_transaction(transaction_id)

Capture transaction

Captures a previously authorized transaction.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import time
import openapi_client
from openapi_client.api import transactions_api
from openapi_client.model.error_generic import ErrorGeneric
from openapi_client.model.transaction import Transaction
from openapi_client.model.transaction_capture_request import TransactionCaptureRequest
from openapi_client.model.error401_unauthorized import Error401Unauthorized
from pprint import pprint
# Defining the host is optional and defaults to https://api.plantly.gr4vy.app
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.plantly.gr4vy.app"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): BearerAuth
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = transactions_api.TransactionsApi(api_client)
    transaction_id = "fe26475d-ec3e-4884-9553-f7356683f7f9" # str | The ID for the transaction to get the information for.
    transaction_capture_request = TransactionCaptureRequest(
        amount=1299,
    ) # TransactionCaptureRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Capture transaction
        api_response = api_instance.capture_transaction(transaction_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TransactionsApi->capture_transaction: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Capture transaction
        api_response = api_instance.capture_transaction(transaction_id, transaction_capture_request=transaction_capture_request)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TransactionsApi->capture_transaction: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_id** | **str**| The ID for the transaction to get the information for. |
 **transaction_capture_request** | [**TransactionCaptureRequest**](TransactionCaptureRequest.md)|  | [optional]

### Return type

[**Transaction**](Transaction.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the captured transaction. |  -  |
**400** | Returns an error if the request was badly formatted or missing required fields. |  -  |
**401** | Returns an error if no valid authentication was provided. |  -  |
**404** | Returns an error if the resource can not be found or has not yet been created. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transaction**
> Transaction get_transaction(transaction_id)

Get transaction

Get information about a transaction.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import time
import openapi_client
from openapi_client.api import transactions_api
from openapi_client.model.error_generic import ErrorGeneric
from openapi_client.model.transaction import Transaction
from openapi_client.model.error401_unauthorized import Error401Unauthorized
from pprint import pprint
# Defining the host is optional and defaults to https://api.plantly.gr4vy.app
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.plantly.gr4vy.app"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): BearerAuth
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = transactions_api.TransactionsApi(api_client)
    transaction_id = "fe26475d-ec3e-4884-9553-f7356683f7f9" # str | The ID for the transaction to get the information for.

    # example passing only required values which don't have defaults set
    try:
        # Get transaction
        api_response = api_instance.get_transaction(transaction_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TransactionsApi->get_transaction: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_id** | **str**| The ID for the transaction to get the information for. |

### Return type

[**Transaction**](Transaction.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a transaction resource. |  -  |
**401** | Returns an error if no valid authentication was provided. |  -  |
**404** | Returns an error if the resource can not be found or has not yet been created. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transaction_refund**
> Refund get_transaction_refund(transaction_id, refund_id)

Get transaction refund

Gets information about a refund associated with a certain transaction.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import time
import openapi_client
from openapi_client.api import transactions_api
from openapi_client.model.error404_not_found import Error404NotFound
from openapi_client.model.refund import Refund
from openapi_client.model.error401_unauthorized import Error401Unauthorized
from pprint import pprint
# Defining the host is optional and defaults to https://api.plantly.gr4vy.app
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.plantly.gr4vy.app"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): BearerAuth
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = transactions_api.TransactionsApi(api_client)
    transaction_id = "fe26475d-ec3e-4884-9553-f7356683f7f9" # str | The ID for the transaction to get the information for.
    refund_id = "8724fd24-5489-4a5d-90fd-0604df7d3b83" # str | The unique ID of the refund.

    # example passing only required values which don't have defaults set
    try:
        # Get transaction refund
        api_response = api_instance.get_transaction_refund(transaction_id, refund_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TransactionsApi->get_transaction_refund: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_id** | **str**| The ID for the transaction to get the information for. |
 **refund_id** | **str**| The unique ID of the refund. |

### Return type

[**Refund**](Refund.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a refund. |  -  |
**401** | Returns an error if no valid authentication was provided. |  -  |
**404** | Returns an error if the resource can not be found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_transaction_refunds**
> Refunds list_transaction_refunds(transaction_id)

List transaction refunds

Lists all refunds associated with a certain transaction.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import time
import openapi_client
from openapi_client.api import transactions_api
from openapi_client.model.error404_not_found import Error404NotFound
from openapi_client.model.refunds import Refunds
from openapi_client.model.error401_unauthorized import Error401Unauthorized
from pprint import pprint
# Defining the host is optional and defaults to https://api.plantly.gr4vy.app
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.plantly.gr4vy.app"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): BearerAuth
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = transactions_api.TransactionsApi(api_client)
    transaction_id = "fe26475d-ec3e-4884-9553-f7356683f7f9" # str | The ID for the transaction to get the information for.
    limit = 1 # int | Defines the maximum number of items to return for this request. (optional) if omitted the server will use the default value of 20
    cursor = "ZXhhbXBsZTE" # str | A cursor that identifies the page of results to return. This is used to paginate the results of this API.  For the first page of results, this parameter can be left out. For additional pages, use the value returned by the API in the `next_cursor` field. Similarly the `previous_cursor` can be used to reverse backwards in the list. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List transaction refunds
        api_response = api_instance.list_transaction_refunds(transaction_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TransactionsApi->list_transaction_refunds: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List transaction refunds
        api_response = api_instance.list_transaction_refunds(transaction_id, limit=limit, cursor=cursor)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TransactionsApi->list_transaction_refunds: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_id** | **str**| The ID for the transaction to get the information for. |
 **limit** | **int**| Defines the maximum number of items to return for this request. | [optional] if omitted the server will use the default value of 20
 **cursor** | **str**| A cursor that identifies the page of results to return. This is used to paginate the results of this API.  For the first page of results, this parameter can be left out. For additional pages, use the value returned by the API in the &#x60;next_cursor&#x60; field. Similarly the &#x60;previous_cursor&#x60; can be used to reverse backwards in the list. | [optional]

### Return type

[**Refunds**](Refunds.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a list of refunds. |  -  |
**401** | Returns an error if no valid authentication was provided. |  -  |
**404** | Returns an error if the resource can not be found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_transactions**
> Transactions list_transactions()

List transactions

Lists all transactions for an account. Sorted by last `updated_at` status.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import time
import openapi_client
from openapi_client.api import transactions_api
from openapi_client.model.transactions import Transactions
from openapi_client.model.error401_unauthorized import Error401Unauthorized
from pprint import pprint
# Defining the host is optional and defaults to https://api.plantly.gr4vy.app
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.plantly.gr4vy.app"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): BearerAuth
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = transactions_api.TransactionsApi(api_client)
    search = "be828248-56de-481e-a580-44b6e1d4df81" # str | Filters the transactions to only the items for which the `id` or `external_identifier` matches this value. This field allows for a partial match, matching any transaction for which either of the fields partially or completely matches. (optional)
    transaction_status = "capture_succeeded" # str | Filters the results to only the transactions for which the `status` matches this value. (optional)
    buyer_id = "8724fd24-5489-4a5d-90fd-0604df7d3b83" # str | Filters the results to only the items for which the `buyer` has an `id` that matches this value. (optional)
    buyer_external_identifier = "user-12345" # str | Filters the results to only the items for which the `buyer` has an `external_identifier` that matches this value. (optional)
    before_created_at = "2012-12-12T10:53:43+00:00" # str | Filters the results to only transactions created before this ISO date-time string. (optional)
    after_created_at = "2012-12-12T10:53:43+00:00" # str | Filters the results to only transactions created after this ISO date-time string. (optional)
    before_updated_at = "2012-12-12T10:53:43+00:00" # str | Filters the results to only transactions last updated before this ISO date-time string. (optional)
    after_updated_at = "2012-12-12T10:53:43+00:00" # str | Filters the results to only transactions last updated after this ISO date-time string. (optional)
    limit = 1 # int | Defines the maximum number of items to return for this request. (optional) if omitted the server will use the default value of 20
    cursor = "ZXhhbXBsZTE" # str | A cursor that identifies the page of results to return. This is used to paginate the results of this API.  For the first page of results, this parameter can be left out. For additional pages, use the value returned by the API in the `next_cursor` field. Similarly the `previous_cursor` can be used to reverse backwards in the list. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List transactions
        api_response = api_instance.list_transactions(search=search, transaction_status=transaction_status, buyer_id=buyer_id, buyer_external_identifier=buyer_external_identifier, before_created_at=before_created_at, after_created_at=after_created_at, before_updated_at=before_updated_at, after_updated_at=after_updated_at, limit=limit, cursor=cursor)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TransactionsApi->list_transactions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| Filters the transactions to only the items for which the &#x60;id&#x60; or &#x60;external_identifier&#x60; matches this value. This field allows for a partial match, matching any transaction for which either of the fields partially or completely matches. | [optional]
 **transaction_status** | **str**| Filters the results to only the transactions for which the &#x60;status&#x60; matches this value. | [optional]
 **buyer_id** | **str**| Filters the results to only the items for which the &#x60;buyer&#x60; has an &#x60;id&#x60; that matches this value. | [optional]
 **buyer_external_identifier** | **str**| Filters the results to only the items for which the &#x60;buyer&#x60; has an &#x60;external_identifier&#x60; that matches this value. | [optional]
 **before_created_at** | **str**| Filters the results to only transactions created before this ISO date-time string. | [optional]
 **after_created_at** | **str**| Filters the results to only transactions created after this ISO date-time string. | [optional]
 **before_updated_at** | **str**| Filters the results to only transactions last updated before this ISO date-time string. | [optional]
 **after_updated_at** | **str**| Filters the results to only transactions last updated after this ISO date-time string. | [optional]
 **limit** | **int**| Defines the maximum number of items to return for this request. | [optional] if omitted the server will use the default value of 20
 **cursor** | **str**| A cursor that identifies the page of results to return. This is used to paginate the results of this API.  For the first page of results, this parameter can be left out. For additional pages, use the value returned by the API in the &#x60;next_cursor&#x60; field. Similarly the &#x60;previous_cursor&#x60; can be used to reverse backwards in the list. | [optional]

### Return type

[**Transactions**](Transactions.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a paginated list of transactions for an account. |  -  |
**401** | Returns an error if no valid authentication was provided. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **refund_transaction**
> Refund refund_transaction(transaction_id)

Refund transaction

Refunds a transaction, fully or partially.  If the transaction was not yet successfully captured, the refund will not be processed. Authorized transactions can be [voided](#operation/void-transaction) instead.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import time
import openapi_client
from openapi_client.api import transactions_api
from openapi_client.model.transaction_refund_request import TransactionRefundRequest
from openapi_client.model.error404_not_found import Error404NotFound
from openapi_client.model.refund import Refund
from openapi_client.model.error_generic import ErrorGeneric
from openapi_client.model.error401_unauthorized import Error401Unauthorized
from pprint import pprint
# Defining the host is optional and defaults to https://api.plantly.gr4vy.app
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.plantly.gr4vy.app"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): BearerAuth
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = transactions_api.TransactionsApi(api_client)
    transaction_id = "fe26475d-ec3e-4884-9553-f7356683f7f9" # str | The ID for the transaction to get the information for.
    transaction_refund_request = TransactionRefundRequest(
        amount=1299,
    ) # TransactionRefundRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Refund transaction
        api_response = api_instance.refund_transaction(transaction_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TransactionsApi->refund_transaction: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Refund transaction
        api_response = api_instance.refund_transaction(transaction_id, transaction_refund_request=transaction_refund_request)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TransactionsApi->refund_transaction: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_id** | **str**| The ID for the transaction to get the information for. |
 **transaction_refund_request** | [**TransactionRefundRequest**](TransactionRefundRequest.md)|  | [optional]

### Return type

[**Refund**](Refund.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Returns the created refund. |  -  |
**400** | Returns an error if the request was badly formatted or missing required fields. |  -  |
**401** | Returns an error if no valid authentication was provided. |  -  |
**404** | Returns an error if the resource can not be found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **refund_transaction_deprecated**
> Transaction refund_transaction_deprecated(transaction_id)

Refund or void transactions

Refunds or voids transaction. If this transaction was already captured, it will issue a refund. If the transaction was not yet captured the authorization will instead be voided.  **Warning**: this endpoint will be removed eventually, use [Refund transaction](#operation/refund-transaction) or [Void transaction](#operation/void-transaction) endpoints instead.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import time
import openapi_client
from openapi_client.api import transactions_api
from openapi_client.model.transaction_refund_request_deprecated import TransactionRefundRequestDeprecated
from openapi_client.model.error_generic import ErrorGeneric
from openapi_client.model.transaction import Transaction
from openapi_client.model.error401_unauthorized import Error401Unauthorized
from pprint import pprint
# Defining the host is optional and defaults to https://api.plantly.gr4vy.app
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.plantly.gr4vy.app"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): BearerAuth
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = transactions_api.TransactionsApi(api_client)
    transaction_id = "fe26475d-ec3e-4884-9553-f7356683f7f9" # str | The ID for the transaction to get the information for.
    transaction_refund_request_deprecated = TransactionRefundRequestDeprecated(
        amount=1299,
    ) # TransactionRefundRequestDeprecated |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Refund or void transactions
        api_response = api_instance.refund_transaction_deprecated(transaction_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TransactionsApi->refund_transaction_deprecated: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Refund or void transactions
        api_response = api_instance.refund_transaction_deprecated(transaction_id, transaction_refund_request_deprecated=transaction_refund_request_deprecated)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TransactionsApi->refund_transaction_deprecated: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_id** | **str**| The ID for the transaction to get the information for. |
 **transaction_refund_request_deprecated** | [**TransactionRefundRequestDeprecated**](TransactionRefundRequestDeprecated.md)|  | [optional]

### Return type

[**Transaction**](Transaction.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns cancelled transaction. |  -  |
**401** | Returns an error if no valid authentication was provided. |  -  |
**404** | Returns an error if the resource can not be found or has not yet been created. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **void_transaction**
> Transaction void_transaction(transaction_id)

Void transaction

Voids a transaction.  If the transaction was not yet successfully authorized, or was already captured, the void will not be processed. Captured transactions can be [refunded](#operation/refund-transaction) instead.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import time
import openapi_client
from openapi_client.api import transactions_api
from openapi_client.model.error404_not_found import Error404NotFound
from openapi_client.model.error_generic import ErrorGeneric
from openapi_client.model.transaction import Transaction
from openapi_client.model.error401_unauthorized import Error401Unauthorized
from pprint import pprint
# Defining the host is optional and defaults to https://api.plantly.gr4vy.app
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.plantly.gr4vy.app"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): BearerAuth
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = transactions_api.TransactionsApi(api_client)
    transaction_id = "fe26475d-ec3e-4884-9553-f7356683f7f9" # str | The ID for the transaction to get the information for.

    # example passing only required values which don't have defaults set
    try:
        # Void transaction
        api_response = api_instance.void_transaction(transaction_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TransactionsApi->void_transaction: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_id** | **str**| The ID for the transaction to get the information for. |

### Return type

[**Transaction**](Transaction.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the voided transaction. |  -  |
**400** | Returns an error if the request was badly formatted or missing required fields. |  -  |
**401** | Returns an error if no valid authentication was provided. |  -  |
**404** | Returns an error if the resource can not be found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

