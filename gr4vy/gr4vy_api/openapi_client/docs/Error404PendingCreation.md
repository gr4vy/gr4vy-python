# Error404PendingCreation

Pending Creation Error (HTTP 404).

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | &#x60;error&#x60;. | [optional]  if omitted the server will use the default value of "error"
**code** | **str** | &#x60;pending_creation&#x60;. | [optional]  if omitted the server will use the default value of "pending_creation"
**status** | **int** | &#x60;404&#x60;. | [optional]  if omitted the server will use the default value of 404
**message** | **str** | The resource is still pending. | [optional]  if omitted the server will use the default value of "The resource is still pending"
**details** | [**[ErrorDetail]**](ErrorDetail.md) | A list of detail objects that further clarify the reason for the error. Not every error supports more detail. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


