# Error409DuplicateRecord

Duplicate Record Error (HTTP 409).

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | &#x60;error&#x60;. | [optional]  if omitted the server will use the default value of "error"
**code** | **str** | &#x60;duplicate_record&#x60;. | [optional]  if omitted the server will use the default value of "duplicate_record"
**status** | **int** | &#x60;409&#x60;. | [optional]  if omitted the server will use the default value of 409
**message** | **str** | Further details on the field that triggered the error. | [optional] 
**details** | [**[ErrorDetail]**](ErrorDetail.md) | A list of detail objects that further clarify the reason for the error. Not every error supports more detail. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


