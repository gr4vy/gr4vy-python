# openapi_client.DigitalWalletsApi

All URIs are relative to *https://api.plantly.gr4vy.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deregister_digital_wallet**](DigitalWalletsApi.md#deregister_digital_wallet) | **DELETE** /digital-wallets/{digital_wallet_id} | De-register digital wallet
[**get_digital_wallet**](DigitalWalletsApi.md#get_digital_wallet) | **GET** /digital-wallets/{digital_wallet_id} | Get digital wallet
[**list_digital_wallets**](DigitalWalletsApi.md#list_digital_wallets) | **GET** /digital-wallets | List digital wallets
[**register_digital_wallet**](DigitalWalletsApi.md#register_digital_wallet) | **POST** /digital-wallets | Register digital wallet
[**update_digital_wallet**](DigitalWalletsApi.md#update_digital_wallet) | **PUT** /digital-wallets/{digital_wallet_id} | Update digital wallet


# **deregister_digital_wallet**
> deregister_digital_wallet(digital_wallet_id)

De-register digital wallet

De-registers a digital wallet with a provider. Upon successful de-registration, the digital wallet's record is deleted and will no longer be available.

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import openapi_client
from openapi_client.api import digital_wallets_api
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
    api_instance = digital_wallets_api.DigitalWalletsApi(api_client)
    digital_wallet_id = "fe26475d-ec3e-4884-9553-f7356683f7f9" # str | The ID of the registered digital wallet.

    # example passing only required values which don't have defaults set
    try:
        # De-register digital wallet
        api_instance.deregister_digital_wallet(digital_wallet_id)
    except openapi_client.ApiException as e:
        print("Exception when calling DigitalWalletsApi->deregister_digital_wallet: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **digital_wallet_id** | **str**| The ID of the registered digital wallet. |

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

# **get_digital_wallet**
> DigitalWallet get_digital_wallet(digital_wallet_id)

Get digital wallet

Returns a registered digital wallet.

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import openapi_client
from openapi_client.api import digital_wallets_api
from openapi_client.model.error404_not_found import Error404NotFound
from openapi_client.model.digital_wallet import DigitalWallet
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
    api_instance = digital_wallets_api.DigitalWalletsApi(api_client)
    digital_wallet_id = "fe26475d-ec3e-4884-9553-f7356683f7f9" # str | The ID of the registered digital wallet.

    # example passing only required values which don't have defaults set
    try:
        # Get digital wallet
        api_response = api_instance.get_digital_wallet(digital_wallet_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DigitalWalletsApi->get_digital_wallet: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **digital_wallet_id** | **str**| The ID of the registered digital wallet. |

### Return type

[**DigitalWallet**](DigitalWallet.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a registered digital wallet. |  -  |
**401** | Returns an error if no valid authentication was provided. |  -  |
**404** | Returns an error if the resource can not be found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_digital_wallets**
> DigitalWallets list_digital_wallets()

List digital wallets

Returns a list of all registered digital wallets.

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import openapi_client
from openapi_client.api import digital_wallets_api
from openapi_client.model.digital_wallets import DigitalWallets
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
    api_instance = digital_wallets_api.DigitalWalletsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List digital wallets
        api_response = api_instance.list_digital_wallets()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DigitalWalletsApi->list_digital_wallets: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**DigitalWallets**](DigitalWallets.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a list of registered digital wallets. |  -  |
**401** | Returns an error if no valid authentication was provided. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_digital_wallet**
> DigitalWallet register_digital_wallet()

Register digital wallet

Register with a digital wallet provider.

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import openapi_client
from openapi_client.api import digital_wallets_api
from openapi_client.model.digital_wallet import DigitalWallet
from openapi_client.model.error_generic import ErrorGeneric
from openapi_client.model.digital_wallet_request import DigitalWalletRequest
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
    api_instance = digital_wallets_api.DigitalWalletsApi(api_client)
    digital_wallet_request = DigitalWalletRequest(
        provider="apple",
        merchant_name="Gr4vy",
        merchant_url="https://example.com",
        domain_names=["example.com"],
        accept_terms_and_conditions=True,
        environments=["production"],
    ) # DigitalWalletRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Register digital wallet
        api_response = api_instance.register_digital_wallet(digital_wallet_request=digital_wallet_request)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DigitalWalletsApi->register_digital_wallet: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **digital_wallet_request** | [**DigitalWalletRequest**](DigitalWalletRequest.md)|  | [optional]

### Return type

[**DigitalWallet**](DigitalWallet.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Returns the newly registered digital wallet. |  -  |
**400** | Returns an error if the request was badly formatted or missing required fields. |  -  |
**401** | Returns an error if no valid authentication was provided. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_digital_wallet**
> DigitalWallet update_digital_wallet(digital_wallet_id)

Update digital wallet

Updates the values a digital wallet was registered with, and the Gr4vy environments in which a registered digital wallet should be available.

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import openapi_client
from openapi_client.api import digital_wallets_api
from openapi_client.model.error404_not_found import Error404NotFound
from openapi_client.model.digital_wallet_update import DigitalWalletUpdate
from openapi_client.model.digital_wallet import DigitalWallet
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
    api_instance = digital_wallets_api.DigitalWalletsApi(api_client)
    digital_wallet_id = "fe26475d-ec3e-4884-9553-f7356683f7f9" # str | The ID of the registered digital wallet.
    digital_wallet_update = DigitalWalletUpdate(
        merchant_name="Gr4vy",
        domain_names=["example.com"],
        environments=["production"],
    ) # DigitalWalletUpdate |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update digital wallet
        api_response = api_instance.update_digital_wallet(digital_wallet_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DigitalWalletsApi->update_digital_wallet: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update digital wallet
        api_response = api_instance.update_digital_wallet(digital_wallet_id, digital_wallet_update=digital_wallet_update)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DigitalWalletsApi->update_digital_wallet: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **digital_wallet_id** | **str**| The ID of the registered digital wallet. |
 **digital_wallet_update** | [**DigitalWalletUpdate**](DigitalWalletUpdate.md)|  | [optional]

### Return type

[**DigitalWallet**](DigitalWallet.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the updated digital wallet. |  -  |
**400** | Returns an error if the request was badly formatted or missing required fields. |  -  |
**401** | Returns an error if no valid authentication was provided. |  -  |
**404** | Returns an error if the resource can not be found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

