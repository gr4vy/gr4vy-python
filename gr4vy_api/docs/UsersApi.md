# api.openapi_client.UsersApi

All URIs are relative to *https://api.plantly.gr4vy.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_user**](UsersApi.md#add_user) | **POST** /users | New user
[**delete_user**](UsersApi.md#delete_user) | **DELETE** /users/{user_id} | Delete user
[**get_current_user**](UsersApi.md#get_current_user) | **GET** /users/me | Get current
[**get_user**](UsersApi.md#get_user) | **GET** /users/{user_id} | Get user
[**list_users**](UsersApi.md#list_users) | **GET** /users | List users
[**reset_user_password**](UsersApi.md#reset_user_password) | **POST** /users/reset-password | Reset user password
[**set_user_password**](UsersApi.md#set_user_password) | **POST** /users/set-password | Set user password


# **add_user**
> User add_user()

New user

Adds a new user.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import time
import api.openapi_client
from gr4vy_api.openapi_client.api import users_api
from gr4vy_api.openapi_client.model.user import User
from gr4vy_api.openapi_client.model.user_request import UserRequest
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
    api_instance = users_api.UsersApi(api_client)
    user_request = UserRequest(
        display_name="John L.",
        email_address="john@example.com",
    ) # UserRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # New user
        api_response = api_instance.add_user(user_request=user_request)
        pprint(api_response)
    except api.openapi_client.ApiException as e:
        print("Exception when calling UsersApi->add_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_request** | [**UserRequest**](UserRequest.md)|  | [optional]

### Return type

[**User**](User.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns new user. |  -  |
**401** | Returns an error if no valid authentication was provided. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user**
> delete_user(user_id)

Delete user

Deletes a user record. Any associated sessions will also be deleted.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import time
import api.openapi_client
from gr4vy_api.openapi_client.api import users_api
from gr4vy_api.openapi_client.model.error404_not_found import Error404NotFound
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
    api_instance = users_api.UsersApi(api_client)
    user_id = "8724fd24-5489-4a5d-90fd-0604df7d3b83" # str | The unique ID for a user.

    # example passing only required values which don't have defaults set
    try:
        # Delete user
        api_instance.delete_user(user_id)
    except api.openapi_client.ApiException as e:
        print("Exception when calling UsersApi->delete_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The unique ID for a user. |

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

# **get_current_user**
> User get_current_user()

Get current

Get current user information.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import time
import api.openapi_client
from gr4vy_api.openapi_client.api import users_api
from gr4vy_api.openapi_client.model.user import User
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
    api_instance = users_api.UsersApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get current
        api_response = api_instance.get_current_user()
        pprint(api_response)
    except api.openapi_client.ApiException as e:
        print("Exception when calling UsersApi->get_current_user: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**User**](User.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the currently authenticated user. |  -  |
**401** | Returns an error if no valid authentication was provided. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user**
> User get_user(user_id)

Get user

Gets the information about a user.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import time
import api.openapi_client
from gr4vy_api.openapi_client.api import users_api
from gr4vy_api.openapi_client.model.error404_not_found import Error404NotFound
from gr4vy_api.openapi_client.model.user import User
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
    api_instance = users_api.UsersApi(api_client)
    user_id = "8724fd24-5489-4a5d-90fd-0604df7d3b83" # str | The unique ID for a user.

    # example passing only required values which don't have defaults set
    try:
        # Get user
        api_response = api_instance.get_user(user_id)
        pprint(api_response)
    except api.openapi_client.ApiException as e:
        print("Exception when calling UsersApi->get_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The unique ID for a user. |

### Return type

[**User**](User.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the user. |  -  |
**401** | Returns an error if no valid authentication was provided. |  -  |
**404** | Returns an error if the resource can not be found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_users**
> Users list_users()

List users

Returns a list of users.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import time
import api.openapi_client
from gr4vy_api.openapi_client.api import users_api
from gr4vy_api.openapi_client.model.users import Users
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
    api_instance = users_api.UsersApi(api_client)
    limit = 1 # int | Defines the maximum number of items to return for this request. (optional) if omitted the server will use the default value of 20
    cursor = "ZXhhbXBsZTE" # str | A cursor that identifies the page of results to return. This is used to paginate the results of this API.  For the first page of results, this parameter can be left out. For additional pages, use the value returned by the API in the `next_cursor` field. Similarly the `previous_cursor` can be used to reverse backwards in the list. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List users
        api_response = api_instance.list_users(limit=limit, cursor=cursor)
        pprint(api_response)
    except api.openapi_client.ApiException as e:
        print("Exception when calling UsersApi->list_users: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Defines the maximum number of items to return for this request. | [optional] if omitted the server will use the default value of 20
 **cursor** | **str**| A cursor that identifies the page of results to return. This is used to paginate the results of this API.  For the first page of results, this parameter can be left out. For additional pages, use the value returned by the API in the &#x60;next_cursor&#x60; field. Similarly the &#x60;previous_cursor&#x60; can be used to reverse backwards in the list. | [optional]

### Return type

[**Users**](Users.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a list of users. |  -  |
**401** | Returns an error if no valid authentication was provided. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reset_user_password**
> User reset_user_password()

Reset user password

Generates a new reset token for a given user.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import time
import api.openapi_client
from gr4vy_api.openapi_client.api import users_api
from gr4vy_api.openapi_client.model.error409_duplicate_record import Error409DuplicateRecord
from gr4vy_api.openapi_client.model.user import User
from gr4vy_api.openapi_client.model.reset_password_request import ResetPasswordRequest
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
    api_instance = users_api.UsersApi(api_client)
    reset_password_request = ResetPasswordRequest(
        email_address="john@example.com",
    ) # ResetPasswordRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Reset user password
        api_response = api_instance.reset_user_password(reset_password_request=reset_password_request)
        pprint(api_response)
    except api.openapi_client.ApiException as e:
        print("Exception when calling UsersApi->reset_user_password: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reset_password_request** | [**ResetPasswordRequest**](ResetPasswordRequest.md)|  | [optional]

### Return type

[**User**](User.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the user object. |  -  |
**204** | Returns an empty response. |  -  |
**401** | Returns an error if no valid authentication was provided. |  -  |
**409** | Returns an error if duplicate resource has been found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_user_password**
> set_user_password()

Set user password

Sets a user password to allow authentication with the dashboard.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import time
import api.openapi_client
from gr4vy_api.openapi_client.api import users_api
from gr4vy_api.openapi_client.model.error401_unauthorized import Error401Unauthorized
from gr4vy_api.openapi_client.model.set_password_request import SetPasswordRequest
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
    api_instance = users_api.UsersApi(api_client)
    set_password_request = SetPasswordRequest(
        reset_token="nXyWSHq2r5q_8F1_NXtppEStY7KbBHqwU9T8pdmOQa_LYJxpxxXcjOXL58xpHLy5gh1k6s0Myl3ygA6SnsxIjLXBKO3x1EZX3igq",
        password="this-is-n0t-a-secure-passw0rd",
    ) # SetPasswordRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Set user password
        api_instance.set_user_password(set_password_request=set_password_request)
    except api.openapi_client.ApiException as e:
        print("Exception when calling UsersApi->set_user_password: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **set_password_request** | [**SetPasswordRequest**](SetPasswordRequest.md)|  | [optional]

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
**204** | Returns an empty response. |  -  |
**401** | Returns an error if no valid authentication was provided. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

