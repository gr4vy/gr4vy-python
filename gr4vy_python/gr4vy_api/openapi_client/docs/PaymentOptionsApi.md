# openapi_client.PaymentOptionsApi

All URIs are relative to *https://api.plantly.gr4vy.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_payment_options**](PaymentOptionsApi.md#list_payment_options) | **GET** /payment-options | List payment options


# **list_payment_options**
> PaymentOptions list_payment_options()

List payment options

Returns a list of available payment method options for a currency and country.

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import openapi_client
from openapi_client.api import payment_options_api
from openapi_client.model.error401_unauthorized import Error401Unauthorized
from openapi_client.model.error400_bad_request import Error400BadRequest
from openapi_client.model.payment_options import PaymentOptions
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
    api_instance = payment_options_api.PaymentOptionsApi(api_client)
    country = "US" # str | Filters the results to only the items which support this country code. A country is formatted as 2-letter ISO country code. (optional)
    currency = "USD" # str | Filters the results to only the items which support this currency code. A currency is formatted as 3-letter ISO currency code. (optional)
    environment = "staging" # str | Filters the results to only the items available in this environment. (optional) if omitted the server will use the default value of "production"
    locale = "en-US" # str | An ISO 639-1 Language Code and optional ISO 3166 Country Code. This locale determines the language for the labels returned for every payment option. (optional) if omitted the server will use the default value of "en-US"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List payment options
        api_response = api_instance.list_payment_options(country=country, currency=currency, environment=environment, locale=locale)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PaymentOptionsApi->list_payment_options: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country** | **str**| Filters the results to only the items which support this country code. A country is formatted as 2-letter ISO country code. | [optional]
 **currency** | **str**| Filters the results to only the items which support this currency code. A currency is formatted as 3-letter ISO currency code. | [optional]
 **environment** | **str**| Filters the results to only the items available in this environment. | [optional] if omitted the server will use the default value of "production"
 **locale** | **str**| An ISO 639-1 Language Code and optional ISO 3166 Country Code. This locale determines the language for the labels returned for every payment option. | [optional] if omitted the server will use the default value of "en-US"

### Return type

[**PaymentOptions**](PaymentOptions.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a list of available payment options for the given query parameters. |  -  |
**400** | Returns an error if  any of the query parameters are not recognised. |  -  |
**401** | Returns an error if no valid authentication was provided. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

