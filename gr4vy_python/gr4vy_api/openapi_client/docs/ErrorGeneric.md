# ErrorGeneric

A generic client error.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of this object. This is always &#x60;error&#x60;. | [optional]  if omitted the server will use the default value of "error"
**code** | **str** | A custom code to further describe the type of error being returned. This code provides further specification within the HTTP &#x60;status&#x60; code and can be used by a program to define logic based on the error. | [optional] 
**status** | **int** | The HTTP status code of this error. | [optional] 
**message** | **str** | A human readable message that describes the error. The content of this field should not be used to determine any business logic.  | [optional] 
**details** | [**[ErrorDetail]**](ErrorDetail.md) | A list of detail objects that further clarify the reason for the error. Not every error supports more detail. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


