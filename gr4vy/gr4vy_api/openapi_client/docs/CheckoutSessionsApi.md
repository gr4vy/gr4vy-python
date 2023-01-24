# openapi_client.CheckoutSessionsApi

All URIs are relative to *https://api.plantly.gr4vy.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_checkout_session**](CheckoutSessionsApi.md#add_checkout_session) | **POST** /checkout/sessions | Create a new Checkout Session
[**delete_checkout_session**](CheckoutSessionsApi.md#delete_checkout_session) | **DELETE** /checkout/sessions/{checkout_session_id} | Delete a Checkout Session
[**get_checkout_session**](CheckoutSessionsApi.md#get_checkout_session) | **GET** /checkout/sessions/{checkout_session_id} | Get a Checkout Session
[**update_checkout_session_fields**](CheckoutSessionsApi.md#update_checkout_session_fields) | **PUT** /checkout/sessions/{checkout_session_id}/fields | Update a Checkout Session&#39;s Secure Fields


# **add_checkout_session**
> CheckoutSession add_checkout_session()

Create a new Checkout Session

Creates a new Checkout Session.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import time
import openapi_client
from openapi_client.api import checkout_sessions_api
from openapi_client.model.error_generic import ErrorGeneric
from openapi_client.model.checkout_session import CheckoutSession
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
    api_instance = checkout_sessions_api.CheckoutSessionsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Create a new Checkout Session
        api_response = api_instance.add_checkout_session()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CheckoutSessionsApi->add_checkout_session: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**CheckoutSession**](CheckoutSession.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Returns the new Checkout Session. |  -  |
**401** | Returns an error if no valid authentication was provided. |  -  |
**0** | Returns a generic error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_checkout_session**
> delete_checkout_session(checkout_session_id)

Delete a Checkout Session

Deletes a Checkout Session.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import time
import openapi_client
from openapi_client.api import checkout_sessions_api
from openapi_client.model.error404_not_found import Error404NotFound
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
    api_instance = checkout_sessions_api.CheckoutSessionsApi(api_client)
    checkout_session_id = "8724fd24-5489-4a5d-90fd-0604df7d3b83" # str | The unique ID for a Checkout Session.

    # example passing only required values which don't have defaults set
    try:
        # Delete a Checkout Session
        api_instance.delete_checkout_session(checkout_session_id)
    except openapi_client.ApiException as e:
        print("Exception when calling CheckoutSessionsApi->delete_checkout_session: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **checkout_session_id** | **str**| The unique ID for a Checkout Session. |

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Returns an empty response. |  -  |
**401** | Returns an error if no valid authentication was provided. |  -  |
**404** | Returns an error if the Checkout Session can not be found or has expired. |  -  |
**0** | Returns a generic error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_checkout_session**
> CheckoutSession get_checkout_session(checkout_session_id)

Get a Checkout Session

Gets details about a current Checkout Session.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import time
import openapi_client
from openapi_client.api import checkout_sessions_api
from openapi_client.model.error404_not_found import Error404NotFound
from openapi_client.model.error_generic import ErrorGeneric
from openapi_client.model.checkout_session import CheckoutSession
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
    api_instance = checkout_sessions_api.CheckoutSessionsApi(api_client)
    checkout_session_id = "8724fd24-5489-4a5d-90fd-0604df7d3b83" # str | The unique ID for a Checkout Session.

    # example passing only required values which don't have defaults set
    try:
        # Get a Checkout Session
        api_response = api_instance.get_checkout_session(checkout_session_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CheckoutSessionsApi->get_checkout_session: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **checkout_session_id** | **str**| The unique ID for a Checkout Session. |

### Return type

[**CheckoutSession**](CheckoutSession.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns details about a current Checkout Session. |  -  |
**401** | Returns an error if no valid authentication was provided. |  -  |
**404** | Returns an error if the Checkout Session can not be found or has expired. |  -  |
**0** | Returns a generic error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_checkout_session_fields**
> update_checkout_session_fields(checkout_session_id)

Update a Checkout Session's Secure Fields

Updates the Secure Fields of the Checkout Session. Once the fields have been received the `expires_at` will be updated to 5 minutes from the time of receipt.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import time
import openapi_client
from openapi_client.api import checkout_sessions_api
from openapi_client.model.error404_not_found import Error404NotFound
from openapi_client.model.error_generic import ErrorGeneric
from openapi_client.model.checkout_session_secure_fields_update import CheckoutSessionSecureFieldsUpdate
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
    api_instance = checkout_sessions_api.CheckoutSessionsApi(api_client)
    checkout_session_id = "8724fd24-5489-4a5d-90fd-0604df7d3b83" # str | The unique ID for a Checkout Session.
    checkout_session_secure_fields_update = CheckoutSessionSecureFieldsUpdate(
        payment_method=CardRequest(
            method="card",
            number="4111111111111111",
            expiration_date="11/25",
            security_code="123",
            external_identifier="card-323444",
            buyer_id="fe26475d-ec3e-4884-9553-f7356683f7f9",
            buyer_external_identifier="user-789123",
            redirect_url="https://example.com/callback",
        ),
    ) # CheckoutSessionSecureFieldsUpdate |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a Checkout Session's Secure Fields
        api_instance.update_checkout_session_fields(checkout_session_id)
    except openapi_client.ApiException as e:
        print("Exception when calling CheckoutSessionsApi->update_checkout_session_fields: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a Checkout Session's Secure Fields
        api_instance.update_checkout_session_fields(checkout_session_id, checkout_session_secure_fields_update=checkout_session_secure_fields_update)
    except openapi_client.ApiException as e:
        print("Exception when calling CheckoutSessionsApi->update_checkout_session_fields: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **checkout_session_id** | **str**| The unique ID for a Checkout Session. |
 **checkout_session_secure_fields_update** | [**CheckoutSessionSecureFieldsUpdate**](CheckoutSessionSecureFieldsUpdate.md)|  | [optional]

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Returns when the Checkout Session was updated. |  -  |
**401** | Returns an error if no valid authentication was provided. |  -  |
**404** | Returns an error if the Checkout Session can not be found or has expired. |  -  |
**0** | Returns a generic error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

