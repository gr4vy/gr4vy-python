# ErrorDetail

Additional detail about the part of a request body that caused an issue.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**location** | **str** | The location where the error caused an issue. | [optional] 
**type** | **str** | A unique identifier for the type of error that occurred. | [optional] 
**pointer** | **str** | The exact item for which the validation did not succeed. This is a JSON pointer for request bodies, while for query, path, and header parameters it is the name of the parameter. | [optional] 
**message** | **str** | A human readable message for this error detail. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


