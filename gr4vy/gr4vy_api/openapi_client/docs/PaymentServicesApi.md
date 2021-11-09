# openapi_client.PaymentServicesApi

All URIs are relative to *https://api.plantly.gr4vy.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_payment_service**](PaymentServicesApi.md#add_payment_service) | **POST** /payment-services | New payment service
[**delete_payment_service**](PaymentServicesApi.md#delete_payment_service) | **DELETE** /payment-services/{payment_service_id} | Delete payment service
[**get_payment_service**](PaymentServicesApi.md#get_payment_service) | **GET** /payment-services/{payment_service_id} | Get payment service
[**list_payment_services**](PaymentServicesApi.md#list_payment_services) | **GET** /payment-services | List payment services
[**update_payment_service**](PaymentServicesApi.md#update_payment_service) | **PUT** /payment-services/{payment_service_id} | Update payment service


# **add_payment_service**
> PaymentService add_payment_service()

New payment service

Adds a new payment service by providing a custom name and a value for each of the required fields.

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import openapi_client
from openapi_client.api import payment_services_api
from openapi_client.model.error_generic import ErrorGeneric
from openapi_client.model.payment_service import PaymentService
from openapi_client.model.payment_service_request import PaymentServiceRequest
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
    api_instance = payment_services_api.PaymentServicesApi(api_client)
    payment_service_request = PaymentServiceRequest() # PaymentServiceRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # New payment service
        api_response = api_instance.add_payment_service(payment_service_request=payment_service_request)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PaymentServicesApi->add_payment_service: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_service_request** | [**PaymentServiceRequest**](PaymentServiceRequest.md)|  | [optional]

### Return type

[**PaymentService**](PaymentService.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Returns the created payment service. |  -  |
**400** | Returns an error if the request was badly formatted or missing required fields. |  -  |
**401** | Returns an error if no valid authentication was provided. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_payment_service**
> delete_payment_service(payment_service_id)

Delete payment service

Deletes a specific active payment service.

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import openapi_client
from openapi_client.api import payment_services_api
from openapi_client.model.error404_not_found import Error404NotFound
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
    api_instance = payment_services_api.PaymentServicesApi(api_client)
    payment_service_id = "46973e9d-88a7-44a6-abfe-be4ff0134ff4" # str | The ID of the payment service.

    # example passing only required values which don't have defaults set
    try:
        # Delete payment service
        api_instance.delete_payment_service(payment_service_id)
    except openapi_client.ApiException as e:
        print("Exception when calling PaymentServicesApi->delete_payment_service: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_service_id** | **str**| The ID of the payment service. |

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
**404** | Returns an error if the resource can not be found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payment_service**
> PaymentService get_payment_service(payment_service_id)

Get payment service

Retrieves the details of a single configured payment service.

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import openapi_client
from openapi_client.api import payment_services_api
from openapi_client.model.error404_not_found import Error404NotFound
from openapi_client.model.payment_service import PaymentService
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
    api_instance = payment_services_api.PaymentServicesApi(api_client)
    payment_service_id = "46973e9d-88a7-44a6-abfe-be4ff0134ff4" # str | The ID of the payment service.

    # example passing only required values which don't have defaults set
    try:
        # Get payment service
        api_response = api_instance.get_payment_service(payment_service_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PaymentServicesApi->get_payment_service: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_service_id** | **str**| The ID of the payment service. |

### Return type

[**PaymentService**](PaymentService.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a payment service. |  -  |
**401** | Returns an error if no valid authentication was provided. |  -  |
**404** | Returns an error if the resource can not be found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_payment_services**
> PaymentServices list_payment_services()

List payment services

Lists the currently configured and activated payment services.

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import openapi_client
from openapi_client.api import payment_services_api
from openapi_client.model.error401_unauthorized import Error401Unauthorized
from openapi_client.model.payment_services import PaymentServices
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
    api_instance = payment_services_api.PaymentServicesApi(api_client)
    limit = 1 # int | Defines the maximum number of items to return for this request. (optional) if omitted the server will use the default value of 20
    cursor = "ZXhhbXBsZTE" # str | A cursor that identifies the page of results to return. This is used to paginate the results of this API.  For the first page of results, this parameter can be left out. For additional pages, use the value returned by the API in the `next_cursor` field. Similarly the `previous_cursor` can be used to reverse backwards in the list. (optional)
    method = "card" # str | Filters the results to only the items for which the `method` has been set to this value. (optional)
    environment = "staging" # str | Filters the results to only the items available in this environment. (optional) if omitted the server will use the default value of "production"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List payment services
        api_response = api_instance.list_payment_services(limit=limit, cursor=cursor, method=method, environment=environment)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PaymentServicesApi->list_payment_services: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Defines the maximum number of items to return for this request. | [optional] if omitted the server will use the default value of 20
 **cursor** | **str**| A cursor that identifies the page of results to return. This is used to paginate the results of this API.  For the first page of results, this parameter can be left out. For additional pages, use the value returned by the API in the &#x60;next_cursor&#x60; field. Similarly the &#x60;previous_cursor&#x60; can be used to reverse backwards in the list. | [optional]
 **method** | **str**| Filters the results to only the items for which the &#x60;method&#x60; has been set to this value. | [optional]
 **environment** | **str**| Filters the results to only the items available in this environment. | [optional] if omitted the server will use the default value of "production"

### Return type

[**PaymentServices**](PaymentServices.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a list of payment services. |  -  |
**401** | Returns an error if no valid authentication was provided. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_payment_service**
> PaymentService update_payment_service(payment_service_id)

Update payment service

Updates an existing payment service. Allows all fields to be changed except for the service ID.

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import openapi_client
from openapi_client.api import payment_services_api
from openapi_client.model.payment_service_update import PaymentServiceUpdate
from openapi_client.model.error404_not_found import Error404NotFound
from openapi_client.model.error_generic import ErrorGeneric
from openapi_client.model.payment_service import PaymentService
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
    api_instance = payment_services_api.PaymentServicesApi(api_client)
    payment_service_id = "46973e9d-88a7-44a6-abfe-be4ff0134ff4" # str | The ID of the payment service.
    payment_service_update = PaymentServiceUpdate(
        display_name="Stripe (Main)",
        fields=[
            PaymentServiceUpdateFields(
                key="private_key",
                value="sk_test_4eC39HqLyjWDarjtT1zdp7dc",
            ),
        ],
        accepted_countries=["US","GB","DE"],
        accepted_currencies=["EUR","USD","GBP"],
        three_d_secure_enabled=True,
        acquirer_bin_visa="acquirer_bin_visa_example",
        acquirer_bin_mastercard="acquirer_bin_mastercard_example",
        acquirer_bin_amex="acquirer_bin_amex_example",
        acquirer_bin_discover="acquirer_bin_discover_example",
        acquirer_merchant_id="acquirer_merchant_id_example",
        merchant_name="gr4vy",
        merchant_country_code="840",
        merchant_category_code="5045",
        merchant_url="merchant_url_example",
        credentials_mode="live",
        active=True,
        environments=["production"],
        position=1,
    ) # PaymentServiceUpdate |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update payment service
        api_response = api_instance.update_payment_service(payment_service_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PaymentServicesApi->update_payment_service: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update payment service
        api_response = api_instance.update_payment_service(payment_service_id, payment_service_update=payment_service_update)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PaymentServicesApi->update_payment_service: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_service_id** | **str**| The ID of the payment service. |
 **payment_service_update** | [**PaymentServiceUpdate**](PaymentServiceUpdate.md)|  | [optional]

### Return type

[**PaymentService**](PaymentService.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Returns the updated payment service. |  -  |
**400** | Returns an error if the request was badly formatted or missing required fields. |  -  |
**401** | Returns an error if no valid authentication was provided. |  -  |
**404** | Returns an error if the resource can not be found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

