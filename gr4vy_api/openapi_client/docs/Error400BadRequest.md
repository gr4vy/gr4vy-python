# Error400BadRequest

Bad Request (HTTP 400).

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | &#x60;error&#x60;. | [optional]  if omitted the server will use the default value of "error"
**code** | **str** | &#x60;bad_request&#x60;. | [optional]  if omitted the server will use the default value of "bad_request"
**status** | **int** | &#x60;400&#x60;. | [optional]  if omitted the server will use the default value of 400
**message** | **str** | Describes the fields that are missing or incorrectly formatted in the API request. | [optional] 
**details** | [**[ErrorDetail]**](ErrorDetail.md) | A list of detail objects that further clarify the reason for the error. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


