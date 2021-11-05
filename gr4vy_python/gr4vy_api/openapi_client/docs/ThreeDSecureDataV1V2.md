# ThreeDSecureDataV1V2


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cavv** | **str** | The cardholder authentication value or AAV. | 
**eci** | **str** | The electronic commerce indicator for the 3DS transaction. | 
**version** | **str** | The version of 3-D Secure that was used. | 
**directory_response** | **str** | For 3-D Secure version 1, the enrolment response. For 3-D Secure version , the transaction status from the &#x60;ARes&#x60;. | 
**authentication_response** | **str** | The transaction status from the challenge result (not required for frictionless). | 
**cavv_algorithm** | **str** | The CAVV Algorithm used. | 
**xid** | **str** | The transaction identifier. | 
**directory_transaction_id** | **str** | The transaction identifier. | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


