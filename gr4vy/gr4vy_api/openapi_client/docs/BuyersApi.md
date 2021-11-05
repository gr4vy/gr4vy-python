# openapi_client.BuyersApi

All URIs are relative to *https://api.plantly.gr4vy.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_buyer**](BuyersApi.md#add_buyer) | **POST** /buyers | New buyer
[**delete_buyer**](BuyersApi.md#delete_buyer) | **DELETE** /buyers/{buyer_id} | Delete buyer
[**get_buyer**](BuyersApi.md#get_buyer) | **GET** /buyers/{buyer_id} | Get buyer
[**list_buyers**](BuyersApi.md#list_buyers) | **GET** /buyers | List buyers
[**update_buyer**](BuyersApi.md#update_buyer) | **PUT** /buyers/{buyer_id} | Update buyer


# **add_buyer**
> Buyer add_buyer()

New buyer

Adds a buyer, allowing for payment methods and transactions to be associated to this buyer. 

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import openapi_client
from openapi_client.api import buyers_api
from openapi_client.model.buyer import Buyer
from openapi_client.model.error409_duplicate_record import Error409DuplicateRecord
from openapi_client.model.error_generic import ErrorGeneric
from openapi_client.model.buyer_request import BuyerRequest
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
    api_instance = buyers_api.BuyersApi(api_client)
    buyer_request = BuyerRequest(
        external_identifier="user-789123",
        display_name="John L.",
        billing_details=,
    ) # BuyerRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # New buyer
        api_response = api_instance.add_buyer(buyer_request=buyer_request)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling BuyersApi->add_buyer: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **buyer_request** | [**BuyerRequest**](BuyerRequest.md)|  | [optional]

### Return type

[**Buyer**](Buyer.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Returns the buyer that was added. |  -  |
**400** | Returns an error if the request was badly formatted or missing required fields. |  -  |
**401** | Returns an error if no valid authentication was provided. |  -  |
**409** | Returns an error if duplicate resource has been found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_buyer**
> delete_buyer(buyer_id)

Delete buyer

Deletes a buyer record. Any associated tokenized payment methods will remain in the system but no longer associated to the buyer.

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import openapi_client
from openapi_client.api import buyers_api
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
    api_instance = buyers_api.BuyersApi(api_client)
    buyer_id = "8724fd24-5489-4a5d-90fd-0604df7d3b83" # str | The unique ID for a buyer.

    # example passing only required values which don't have defaults set
    try:
        # Delete buyer
        api_instance.delete_buyer(buyer_id)
    except openapi_client.ApiException as e:
        print("Exception when calling BuyersApi->delete_buyer: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **buyer_id** | **str**| The unique ID for a buyer. |

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

# **get_buyer**
> Buyer get_buyer(buyer_id)

Get buyer

Gets the information about a buyer.

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import openapi_client
from openapi_client.api import buyers_api
from openapi_client.model.buyer import Buyer
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
    api_instance = buyers_api.BuyersApi(api_client)
    buyer_id = "8724fd24-5489-4a5d-90fd-0604df7d3b83" # str | The unique ID for a buyer.

    # example passing only required values which don't have defaults set
    try:
        # Get buyer
        api_response = api_instance.get_buyer(buyer_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling BuyersApi->get_buyer: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **buyer_id** | **str**| The unique ID for a buyer. |

### Return type

[**Buyer**](Buyer.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the information about a buyer. |  -  |
**401** | Returns an error if no valid authentication was provided. |  -  |
**404** | Returns an error if the resource can not be found. |  -  |
**0** | Returns a generic error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_buyers**
> Buyers list_buyers()

List buyers

Returns a list of buyers.

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import openapi_client
from openapi_client.api import buyers_api
from openapi_client.model.buyers import Buyers
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
    api_instance = buyers_api.BuyersApi(api_client)
    search = "John" # str | Filters the results to only the buyers for which the `display_name` or `external_identifier` matches this value. This field allows for a partial match, matching any buyer for which either of the fields partially or completely matches. (optional)
    limit = 1 # int | Defines the maximum number of items to return for this request. (optional) if omitted the server will use the default value of 20
    cursor = "ZXhhbXBsZTE" # str | A cursor that identifies the page of results to return. This is used to paginate the results of this API.  For the first page of results, this parameter can be left out. For additional pages, use the value returned by the API in the `next_cursor` field. Similarly the `previous_cursor` can be used to reverse backwards in the list. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List buyers
        api_response = api_instance.list_buyers(search=search, limit=limit, cursor=cursor)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling BuyersApi->list_buyers: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| Filters the results to only the buyers for which the &#x60;display_name&#x60; or &#x60;external_identifier&#x60; matches this value. This field allows for a partial match, matching any buyer for which either of the fields partially or completely matches. | [optional]
 **limit** | **int**| Defines the maximum number of items to return for this request. | [optional] if omitted the server will use the default value of 20
 **cursor** | **str**| A cursor that identifies the page of results to return. This is used to paginate the results of this API.  For the first page of results, this parameter can be left out. For additional pages, use the value returned by the API in the &#x60;next_cursor&#x60; field. Similarly the &#x60;previous_cursor&#x60; can be used to reverse backwards in the list. | [optional]

### Return type

[**Buyers**](Buyers.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a list of buyers. |  -  |
**401** | Returns an error if no valid authentication was provided. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_buyer**
> Buyer update_buyer(buyer_id)

Update buyer

Updates a buyer's details. 

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import openapi_client
from openapi_client.api import buyers_api
from openapi_client.model.buyer import Buyer
from openapi_client.model.error404_not_found import Error404NotFound
from openapi_client.model.error_generic import ErrorGeneric
from openapi_client.model.buyer_update import BuyerUpdate
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
    api_instance = buyers_api.BuyersApi(api_client)
    buyer_id = "8724fd24-5489-4a5d-90fd-0604df7d3b83" # str | The unique ID for a buyer.
    buyer_update = BuyerUpdate(
        billing_details=,
    ) # BuyerUpdate |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update buyer
        api_response = api_instance.update_buyer(buyer_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling BuyersApi->update_buyer: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update buyer
        api_response = api_instance.update_buyer(buyer_id, buyer_update=buyer_update)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling BuyersApi->update_buyer: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **buyer_id** | **str**| The unique ID for a buyer. |
 **buyer_update** | [**BuyerUpdate**](BuyerUpdate.md)|  | [optional]

### Return type

[**Buyer**](Buyer.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the updated buyer record. |  -  |
**400** | Returns an error if the request was badly formatted or missing required fields. |  -  |
**401** | Returns an error if no valid authentication was provided. |  -  |
**404** | Returns an error if the resource can not be found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

