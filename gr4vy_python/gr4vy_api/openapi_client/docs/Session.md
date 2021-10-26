# Session

A user session.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | &#x60;auth.session&#x60;. | [optional]  if omitted the server will use the default value of "auth.session"
**token_type** | **str** | &#x60;bearer&#x60;. | [optional]  if omitted the server will use the default value of "bearer"
**access_token** | **str** | A server-signed JWT that can be used as the bearer token in any API calls. | [optional] 
**refresh_token** | **str** | A server-signed JWT that can be used as the bearer token to refresh the access token. | [optional] 
**expires_in** | **int** | The time in seconds in seconds by which the &#x60;access_token&#x60; token will expire. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


