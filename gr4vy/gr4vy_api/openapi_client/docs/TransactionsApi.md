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
        country="US",
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
        browser_info=None,
        shipping_details_id="47da6902-5eae-4b4b-88fd-856802d627d6",
        connection_options=None,
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
    buyer_external_identifier = "user-12345" # str | Filters the results to only the items for which the `buyer` has an `external_identifier` that matches this value. (optional)
    buyer_id = "8724fd24-5489-4a5d-90fd-0604df7d3b83" # str | Filters the results to only the items for which the `buyer` has an `id` that matches this value. (optional)
    cursor = "ZXhhbXBsZTE" # str | A cursor that identifies the page of results to return. This is used to paginate the results of this API.  For the first page of results, this parameter can be left out. For additional pages, use the value returned by the API in the `next_cursor` field. Similarly the `previous_cursor` can be used to reverse backwards in the list. (optional)
    limit = 1 # int | Defines the maximum number of items to return for this request. (optional) if omitted the server will use the default value of 20
    amount_eq = 500 # int | Filters for transactions that have an `amount` that is equal to the provided `amount_eq` value. (optional)
    amount_gte = 500 # int | Filters for transactions that have an `amount` that is greater than or equal to the `amount_gte` value. (optional)
    amount_lte = 500 # int | Filters for transactions that have an `amount` that is less than or equal to the `amount_lte` value. (optional)
    created_at_gte = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Filters the results to only transactions created after this ISO date-time string. The time zone must be included.  Ensure that the date-time string is URL encoded, e.g. `2022-01-01T12:00:00+08:00` must be encoded as `2022-01-01T12%3A00%3A00%2B08%3A00`. (optional)
    created_at_lte = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Filters the results to only transactions created before this ISO date-time string. The time zone must be included.  Ensure that the date-time string is URL encoded, e.g. `2022-01-01T12:00:00+08:00` must be encoded as `2022-01-01T12%3A00%3A00%2B08%3A00`. (optional)
    currency = ["USD","GBP"] # [str] | Filters for transactions that have matching `currency` values. The `currency` values provided must be formatted as 3-letter ISO currency code. (optional)
    external_identifier = "user-12345" # str | Filters the results to only the items for which the `external_identifier` matches this value. (optional)
    has_refunds = True # bool | When set to `true`, filter for transactions that have at least one completed refund associated with it. When set to `false`, filter for transactions that have no completed refunds. (optional)
    id = "be828248-56de-481e-a580-44b6e1d4df81" # str | Filters for the transaction that has a matching `id` value. (optional)
    metadata = ["{\"key\": \"value\"}","{\"key_one\": \"value\", \"key_two\": \"value\"}"] # [str] | Filters for transactions where their `metadata` values contain all of the provided `metadata` keys. The value sent for `metadata` must be formatted as a JSON string, and all keys and values must be strings. This value should also be URL encoded.  Duplicate keys are not supported. If a key is duplicated, only the last appearing value will be used. (optional)
    method = [
        "card",
    ] # [str] | Filters the results to only the items for which the `method` has been set to this value. (optional)
    payment_method_id = "46973e9d-88a7-44a6-abfe-be4ff0134ff4" # str | The ID of the payment method. (optional)
    payment_method_label = "1234" # str | Filters for transactions that have a payment method with a label that matches exactly with the provided value. (optional)
    payment_service_id = ["46973e9d-88a7-44a6-abfe-be4ff0134ff4"] # [str] | Filters for transactions that were processed by the provided `payment_service_id` values. (optional)
    payment_service_transaction_id = "transaction_123" # str | Filters for transactions that have a matching `payment_service_transaction_id` value. The `payment_service_transaction_id` is the identifier of the transaction given by the payment service. (optional)
    search = "be828248-56de-481e-a580-44b6e1d4df81" # str | Filters for transactions that have one of the following fields match exactly with the provided `search` value: * `buyer_external_identifier` * `buyer_id` * `external_identifier` * `id` * `payment_service_transaction_id` (optional)
    status = ["capture_succeeded","processing"] # [str] | Filters the results to only the transactions that have a `status` that matches with any of the provided status values. (optional)
    updated_at_gte = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Filters the results to only transactions last updated after this ISO date-time string. The time zone must be included.  Ensure that the date-time string is URL encoded, e.g. `2022-01-01T12:00:00+08:00` must be encoded as `2022-01-01T12%3A00%3A00%2B08%3A00`. (optional)
    updated_at_lte = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Filters the results to only transactions last updated before this ISO date-time string. The time zone must be included.  Ensure that the date-time string is URL encoded, e.g. `2022-01-01T12:00:00+08:00` must be encoded as `2022-01-01T12%3A00%3A00%2B08%3A00`. (optional)
    before_created_at = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Filters the results to only transactions created before this ISO date-time string. The time zone must be included.  Ensure that the date-time string is URL encoded, e.g. `2022-01-01T12:00:00+08:00` must be encoded as `2022-01-01T12%3A00%3A00%2B08%3A00`.  **WARNING** This filter is deprecated and may be removed eventually, use `created_at_lte` instead. (optional)
    after_created_at = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Filters the results to only transactions created after this ISO date-time string. The time zone must be included.  Ensure that the date-time string is URL encoded, e.g. `2022-01-01T12:00:00+08:00` must be encoded as `2022-01-01T12%3A00%3A00%2B08%3A00`.  **WARNING** This filter is deprecated and may be removed eventually, use `created_at_gte` instead. (optional)
    before_updated_at = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Filters the results to only transactions last updated before this ISO date-time string. The time zone must be included.  Ensure that the date-time string is URL encoded, e.g. `2022-01-01T12:00:00+08:00` must be encoded as `2022-01-01T12%3A00%3A00%2B08%3A00`.  **WARNING** This filter is deprecated and may be removed eventually, use `updated_at_lte` instead. (optional)
    after_updated_at = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Filters the results to only transactions last updated after this ISO date-time string. The time zone must be included.  Ensure that the date-time string is URL encoded, e.g. `2022-01-01T12:00:00+08:00` must be encoded as `2022-01-01T12%3A00%3A00%2B08%3A00`.  **WARNING** This filter is deprecated and may be removed eventually, use `updated_at_gte` instead. (optional)
    transaction_status = "capture_succeeded" # str | Filters the results to only the transactions for which the `status` matches this value.  **WARNING** This filter is deprecated and may be removed eventually, use `status` instead. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List transactions
        api_response = api_instance.list_transactions(buyer_external_identifier=buyer_external_identifier, buyer_id=buyer_id, cursor=cursor, limit=limit, amount_eq=amount_eq, amount_gte=amount_gte, amount_lte=amount_lte, created_at_gte=created_at_gte, created_at_lte=created_at_lte, currency=currency, external_identifier=external_identifier, has_refunds=has_refunds, id=id, metadata=metadata, method=method, payment_method_id=payment_method_id, payment_method_label=payment_method_label, payment_service_id=payment_service_id, payment_service_transaction_id=payment_service_transaction_id, search=search, status=status, updated_at_gte=updated_at_gte, updated_at_lte=updated_at_lte, before_created_at=before_created_at, after_created_at=after_created_at, before_updated_at=before_updated_at, after_updated_at=after_updated_at, transaction_status=transaction_status)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TransactionsApi->list_transactions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **buyer_external_identifier** | **str**| Filters the results to only the items for which the &#x60;buyer&#x60; has an &#x60;external_identifier&#x60; that matches this value. | [optional]
 **buyer_id** | **str**| Filters the results to only the items for which the &#x60;buyer&#x60; has an &#x60;id&#x60; that matches this value. | [optional]
 **cursor** | **str**| A cursor that identifies the page of results to return. This is used to paginate the results of this API.  For the first page of results, this parameter can be left out. For additional pages, use the value returned by the API in the &#x60;next_cursor&#x60; field. Similarly the &#x60;previous_cursor&#x60; can be used to reverse backwards in the list. | [optional]
 **limit** | **int**| Defines the maximum number of items to return for this request. | [optional] if omitted the server will use the default value of 20
 **amount_eq** | **int**| Filters for transactions that have an &#x60;amount&#x60; that is equal to the provided &#x60;amount_eq&#x60; value. | [optional]
 **amount_gte** | **int**| Filters for transactions that have an &#x60;amount&#x60; that is greater than or equal to the &#x60;amount_gte&#x60; value. | [optional]
 **amount_lte** | **int**| Filters for transactions that have an &#x60;amount&#x60; that is less than or equal to the &#x60;amount_lte&#x60; value. | [optional]
 **created_at_gte** | **datetime**| Filters the results to only transactions created after this ISO date-time string. The time zone must be included.  Ensure that the date-time string is URL encoded, e.g. &#x60;2022-01-01T12:00:00+08:00&#x60; must be encoded as &#x60;2022-01-01T12%3A00%3A00%2B08%3A00&#x60;. | [optional]
 **created_at_lte** | **datetime**| Filters the results to only transactions created before this ISO date-time string. The time zone must be included.  Ensure that the date-time string is URL encoded, e.g. &#x60;2022-01-01T12:00:00+08:00&#x60; must be encoded as &#x60;2022-01-01T12%3A00%3A00%2B08%3A00&#x60;. | [optional]
 **currency** | **[str]**| Filters for transactions that have matching &#x60;currency&#x60; values. The &#x60;currency&#x60; values provided must be formatted as 3-letter ISO currency code. | [optional]
 **external_identifier** | **str**| Filters the results to only the items for which the &#x60;external_identifier&#x60; matches this value. | [optional]
 **has_refunds** | **bool**| When set to &#x60;true&#x60;, filter for transactions that have at least one completed refund associated with it. When set to &#x60;false&#x60;, filter for transactions that have no completed refunds. | [optional]
 **id** | **str**| Filters for the transaction that has a matching &#x60;id&#x60; value. | [optional]
 **metadata** | **[str]**| Filters for transactions where their &#x60;metadata&#x60; values contain all of the provided &#x60;metadata&#x60; keys. The value sent for &#x60;metadata&#x60; must be formatted as a JSON string, and all keys and values must be strings. This value should also be URL encoded.  Duplicate keys are not supported. If a key is duplicated, only the last appearing value will be used. | [optional]
 **method** | **[str]**| Filters the results to only the items for which the &#x60;method&#x60; has been set to this value. | [optional]
 **payment_method_id** | **str**| The ID of the payment method. | [optional]
 **payment_method_label** | **str**| Filters for transactions that have a payment method with a label that matches exactly with the provided value. | [optional]
 **payment_service_id** | **[str]**| Filters for transactions that were processed by the provided &#x60;payment_service_id&#x60; values. | [optional]
 **payment_service_transaction_id** | **str**| Filters for transactions that have a matching &#x60;payment_service_transaction_id&#x60; value. The &#x60;payment_service_transaction_id&#x60; is the identifier of the transaction given by the payment service. | [optional]
 **search** | **str**| Filters for transactions that have one of the following fields match exactly with the provided &#x60;search&#x60; value: * &#x60;buyer_external_identifier&#x60; * &#x60;buyer_id&#x60; * &#x60;external_identifier&#x60; * &#x60;id&#x60; * &#x60;payment_service_transaction_id&#x60; | [optional]
 **status** | **[str]**| Filters the results to only the transactions that have a &#x60;status&#x60; that matches with any of the provided status values. | [optional]
 **updated_at_gte** | **datetime**| Filters the results to only transactions last updated after this ISO date-time string. The time zone must be included.  Ensure that the date-time string is URL encoded, e.g. &#x60;2022-01-01T12:00:00+08:00&#x60; must be encoded as &#x60;2022-01-01T12%3A00%3A00%2B08%3A00&#x60;. | [optional]
 **updated_at_lte** | **datetime**| Filters the results to only transactions last updated before this ISO date-time string. The time zone must be included.  Ensure that the date-time string is URL encoded, e.g. &#x60;2022-01-01T12:00:00+08:00&#x60; must be encoded as &#x60;2022-01-01T12%3A00%3A00%2B08%3A00&#x60;. | [optional]
 **before_created_at** | **datetime**| Filters the results to only transactions created before this ISO date-time string. The time zone must be included.  Ensure that the date-time string is URL encoded, e.g. &#x60;2022-01-01T12:00:00+08:00&#x60; must be encoded as &#x60;2022-01-01T12%3A00%3A00%2B08%3A00&#x60;.  **WARNING** This filter is deprecated and may be removed eventually, use &#x60;created_at_lte&#x60; instead. | [optional]
 **after_created_at** | **datetime**| Filters the results to only transactions created after this ISO date-time string. The time zone must be included.  Ensure that the date-time string is URL encoded, e.g. &#x60;2022-01-01T12:00:00+08:00&#x60; must be encoded as &#x60;2022-01-01T12%3A00%3A00%2B08%3A00&#x60;.  **WARNING** This filter is deprecated and may be removed eventually, use &#x60;created_at_gte&#x60; instead. | [optional]
 **before_updated_at** | **datetime**| Filters the results to only transactions last updated before this ISO date-time string. The time zone must be included.  Ensure that the date-time string is URL encoded, e.g. &#x60;2022-01-01T12:00:00+08:00&#x60; must be encoded as &#x60;2022-01-01T12%3A00%3A00%2B08%3A00&#x60;.  **WARNING** This filter is deprecated and may be removed eventually, use &#x60;updated_at_lte&#x60; instead. | [optional]
 **after_updated_at** | **datetime**| Filters the results to only transactions last updated after this ISO date-time string. The time zone must be included.  Ensure that the date-time string is URL encoded, e.g. &#x60;2022-01-01T12:00:00+08:00&#x60; must be encoded as &#x60;2022-01-01T12%3A00%3A00%2B08%3A00&#x60;.  **WARNING** This filter is deprecated and may be removed eventually, use &#x60;updated_at_gte&#x60; instead. | [optional]
 **transaction_status** | **str**| Filters the results to only the transactions for which the &#x60;status&#x60; matches this value.  **WARNING** This filter is deprecated and may be removed eventually, use &#x60;status&#x60; instead. | [optional]

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

# **void_transaction**
> Transaction void_transaction(transaction_id)

Void transaction

Voids a transaction.  If the transaction was not yet successfully authorized, or was already captured, the void will not be processed. Captured transactions can be [refunded](#operation/refund-transaction) instead.  Voiding zero-amount authorized transactions is not supported.

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

