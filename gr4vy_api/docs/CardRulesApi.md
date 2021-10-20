# api.openapi_client.CardRulesApi

All URIs are relative to *https://api.plantly.gr4vy.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_card_rule**](CardRulesApi.md#add_card_rule) | **POST** /card-rules | Create card rule
[**delete_card_rule**](CardRulesApi.md#delete_card_rule) | **DELETE** /card-rules/{card_rule_id} | Delete card rule
[**get_card_rule**](CardRulesApi.md#get_card_rule) | **GET** /card-rules/{card_rule_id} | Get card rule
[**list_cards_rules**](CardRulesApi.md#list_cards_rules) | **GET** /card-rules | List card rules
[**update_card_rule**](CardRulesApi.md#update_card_rule) | **PUT** /card-rules/{card_rule_id} | Update card rule


# **add_card_rule**
> CardRule add_card_rule()

Create card rule

Creates a new rule that is used for card transactions.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import time
import api.openapi_client
from gr4vy_api.openapi_client.api import card_rules_api
from gr4vy_api.openapi_client.model.error401_unauthorized import Error401Unauthorized
from gr4vy_api.openapi_client.model.card_rule_request import CardRuleRequest
from gr4vy_api.openapi_client.model.card_rule import CardRule
from pprint import pprint
# Defining the host is optional and defaults to https://api.plantly.gr4vy.app
# See configuration.py for a list of all supported configuration parameters.
configuration = api.openapi_client.Configuration(
    host = "https://api.plantly.gr4vy.app"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): BearerAuth
configuration = api.openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with api.openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = card_rules_api.CardRulesApi(api_client)
    card_rule_request = CardRuleRequest(
        active=True,
        environment="production",
        position=1,
        conditions=[
            None,
        ],
        payment_service_ids=["f47db210-8e30-4f74-8123-b834604f2042","0bb93ab0-86ef-4ad5-addf-b69913128d96"],
        unprocessable_fallback_strategy="use_all_providers",
        invalid_rule_fallback_strategy="use_all_providers",
    ) # CardRuleRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create card rule
        api_response = api_instance.add_card_rule(card_rule_request=card_rule_request)
        pprint(api_response)
    except api.openapi_client.ApiException as e:
        print("Exception when calling CardRulesApi->add_card_rule: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **card_rule_request** | [**CardRuleRequest**](CardRuleRequest.md)|  | [optional]

### Return type

[**CardRule**](CardRule.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Returns the newly created rule. |  -  |
**400** | Returns an error if the request was badly formatted or missing required fields. |  -  |
**401** | Returns an error if no valid authentication was provided. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_card_rule**
> delete_card_rule(card_rule_id)

Delete card rule

Deletes a specific card rule.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import time
import api.openapi_client
from gr4vy_api.openapi_client.api import card_rules_api
from gr4vy_api.openapi_client.model.error404_not_found import Error404NotFound
from gr4vy_api.openapi_client.model.error_generic import ErrorGeneric
from gr4vy_api.openapi_client.model.error401_unauthorized import Error401Unauthorized
from pprint import pprint
# Defining the host is optional and defaults to https://api.plantly.gr4vy.app
# See configuration.py for a list of all supported configuration parameters.
configuration = api.openapi_client.Configuration(
    host = "https://api.plantly.gr4vy.app"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): BearerAuth
configuration = api.openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with api.openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = card_rules_api.CardRulesApi(api_client)
    card_rule_id = "8724fd24-5489-4a5d-90fd-0604df7d3b83" # str | The unique ID for a card rule.

    # example passing only required values which don't have defaults set
    try:
        # Delete card rule
        api_instance.delete_card_rule(card_rule_id)
    except api.openapi_client.ApiException as e:
        print("Exception when calling CardRulesApi->delete_card_rule: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **card_rule_id** | **str**| The unique ID for a card rule. |

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
**403** | Returns an error if the rule could not be deleted. |  -  |
**404** | Returns an error if the resource can not be found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_card_rule**
> CardRule get_card_rule(card_rule_id)

Get card rule

Returns a rule that can be used for card transactions.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import time
import api.openapi_client
from gr4vy_api.openapi_client.api import card_rules_api
from gr4vy_api.openapi_client.model.error404_not_found import Error404NotFound
from gr4vy_api.openapi_client.model.error401_unauthorized import Error401Unauthorized
from gr4vy_api.openapi_client.model.card_rule import CardRule
from pprint import pprint
# Defining the host is optional and defaults to https://api.plantly.gr4vy.app
# See configuration.py for a list of all supported configuration parameters.
configuration = api.openapi_client.Configuration(
    host = "https://api.plantly.gr4vy.app"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): BearerAuth
configuration = api.openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with api.openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = card_rules_api.CardRulesApi(api_client)
    card_rule_id = "8724fd24-5489-4a5d-90fd-0604df7d3b83" # str | The unique ID for a card rule.

    # example passing only required values which don't have defaults set
    try:
        # Get card rule
        api_response = api_instance.get_card_rule(card_rule_id)
        pprint(api_response)
    except api.openapi_client.ApiException as e:
        print("Exception when calling CardRulesApi->get_card_rule: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **card_rule_id** | **str**| The unique ID for a card rule. |

### Return type

[**CardRule**](CardRule.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a card rule. |  -  |
**401** | Returns an error if no valid authentication was provided. |  -  |
**404** | Returns an error if the resource can not be found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_cards_rules**
> CardRules list_cards_rules()

List card rules

Returns a list of rules for card transactions.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import time
import api.openapi_client
from gr4vy_api.openapi_client.api import card_rules_api
from gr4vy_api.openapi_client.model.card_rules import CardRules
from gr4vy_api.openapi_client.model.error401_unauthorized import Error401Unauthorized
from pprint import pprint
# Defining the host is optional and defaults to https://api.plantly.gr4vy.app
# See configuration.py for a list of all supported configuration parameters.
configuration = api.openapi_client.Configuration(
    host = "https://api.plantly.gr4vy.app"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): BearerAuth
configuration = api.openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with api.openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = card_rules_api.CardRulesApi(api_client)
    limit = 1 # int | Defines the maximum number of items to return for this request. (optional) if omitted the server will use the default value of 20
    cursor = "ZXhhbXBsZTE" # str | A cursor that identifies the page of results to return. This is used to paginate the results of this API.  For the first page of results, this parameter can be left out. For additional pages, use the value returned by the API in the `next_cursor` field. Similarly the `previous_cursor` can be used to reverse backwards in the list. (optional)
    environment = "staging" # str | Filters the results to only the items available in this environment. (optional) if omitted the server will use the default value of "production"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List card rules
        api_response = api_instance.list_cards_rules(limit=limit, cursor=cursor, environment=environment)
        pprint(api_response)
    except api.openapi_client.ApiException as e:
        print("Exception when calling CardRulesApi->list_cards_rules: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Defines the maximum number of items to return for this request. | [optional] if omitted the server will use the default value of 20
 **cursor** | **str**| A cursor that identifies the page of results to return. This is used to paginate the results of this API.  For the first page of results, this parameter can be left out. For additional pages, use the value returned by the API in the &#x60;next_cursor&#x60; field. Similarly the &#x60;previous_cursor&#x60; can be used to reverse backwards in the list. | [optional]
 **environment** | **str**| Filters the results to only the items available in this environment. | [optional] if omitted the server will use the default value of "production"

### Return type

[**CardRules**](CardRules.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a list of card rules. |  -  |
**401** | Returns an error if no valid authentication was provided. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_card_rule**
> CardRule update_card_rule(card_rule_id)

Update card rule

Updates a rule that can be used for card transactions.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import time
import api.openapi_client
from gr4vy_api.openapi_client.api import card_rules_api
from gr4vy_api.openapi_client.model.error404_not_found import Error404NotFound
from gr4vy_api.openapi_client.model.card_rule_update import CardRuleUpdate
from gr4vy_api.openapi_client.model.error401_unauthorized import Error401Unauthorized
from gr4vy_api.openapi_client.model.card_rule import CardRule
from pprint import pprint
# Defining the host is optional and defaults to https://api.plantly.gr4vy.app
# See configuration.py for a list of all supported configuration parameters.
configuration = api.openapi_client.Configuration(
    host = "https://api.plantly.gr4vy.app"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): BearerAuth
configuration = api.openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with api.openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = card_rules_api.CardRulesApi(api_client)
    card_rule_id = "8724fd24-5489-4a5d-90fd-0604df7d3b83" # str | The unique ID for a card rule.
    card_rule_update = CardRuleUpdate(
        active=True,
        environment="production",
        position=1,
        conditions=[
            None,
        ],
        payment_service_ids=["f47db210-8e30-4f74-8123-b834604f2042","0bb93ab0-86ef-4ad5-addf-b69913128d96"],
        unprocessable_fallback_strategy="use_all_providers",
        invalid_rule_fallback_strategy="use_all_providers",
    ) # CardRuleUpdate |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update card rule
        api_response = api_instance.update_card_rule(card_rule_id)
        pprint(api_response)
    except api.openapi_client.ApiException as e:
        print("Exception when calling CardRulesApi->update_card_rule: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update card rule
        api_response = api_instance.update_card_rule(card_rule_id, card_rule_update=card_rule_update)
        pprint(api_response)
    except api.openapi_client.ApiException as e:
        print("Exception when calling CardRulesApi->update_card_rule: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **card_rule_id** | **str**| The unique ID for a card rule. |
 **card_rule_update** | [**CardRuleUpdate**](CardRuleUpdate.md)|  | [optional]

### Return type

[**CardRule**](CardRule.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the updated card rule. |  -  |
**400** | Returns an error if the request was badly formatted or missing required fields. |  -  |
**401** | Returns an error if no valid authentication was provided. |  -  |
**404** | Returns an error if the resource can not be found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

