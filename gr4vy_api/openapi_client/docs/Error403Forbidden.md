# Error403Forbidden

Forbidden Error (HTTP 403).

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | &#x60;error&#x60;. | [optional]  if omitted the server will use the default value of "error"
**code** | **str** | &#x60;forbidden&#x60;. | [optional]  if omitted the server will use the default value of "forbidden"
**status** | **int** | &#x60;403&#x60;. | [optional]  if omitted the server will use the default value of 403
**message** | **str** | Invalid credentials. | [optional]  if omitted the server will use the default value of "Invalid credentials"
**details** | [**[ErrorDetail]**](ErrorDetail.md) | A list of detail objects that further clarify the reason for the error. Not every error supports more detail. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


