# Error401Unauthorized

Unauthorized Error (HTTP 401).

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | &#x60;error&#x60;. | [optional]  if omitted the server will use the default value of "error"
**code** | **str** | &#x60;unauthorized&#x60;. | [optional]  if omitted the server will use the default value of "unauthorized"
**status** | **int** | &#x60;401&#x60;. | [optional]  if omitted the server will use the default value of 401
**message** | **str** | No valid API authentication found. | [optional]  if omitted the server will use the default value of "No valid API authentication found"
**details** | [**[ErrorDetail]**](ErrorDetail.md) | A list of detail objects that further clarify the reason for the error. Not every error supports more detail. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


