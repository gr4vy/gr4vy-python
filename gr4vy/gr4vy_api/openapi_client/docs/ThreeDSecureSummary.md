# ThreeDSecureSummary

Details about the 3-D Secure challenge that was presented to the buyer for this transaction, where applicable.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **str** | The version of 3DS used for this transaction. | [optional] 
**status** | **str** | The status of the 3DS challenge for this transaction. | [optional] 
**method** | **str** | The method used for 3DS authentication for this transaction. | [optional] 
**error_data** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | If the transaction had a 3DS error, information about it. | [optional] 
**response_data** | [**ThreeDSecureDataV1V2**](ThreeDSecureDataV1V2.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


