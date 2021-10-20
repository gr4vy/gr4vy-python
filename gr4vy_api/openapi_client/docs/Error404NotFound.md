# Error404NotFound

Not Found Error (HTTP 404).

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | &#x60;error&#x60;. | [optional]  if omitted the server will use the default value of "error"
**code** | **str** | &#x60;not_found&#x60;. | [optional]  if omitted the server will use the default value of "not_found"
**status** | **int** | &#x60;404&#x60;. | [optional]  if omitted the server will use the default value of 404
**message** | **str** | The resource could not be found. | [optional]  if omitted the server will use the default value of "The resource could not be found"
**details** | [**[ErrorDetail]**](ErrorDetail.md) | A list of detail objects that further clarify the reason for the error. Not every error supports more detail. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


