# Transaction

A transaction record.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of this resource. Is always &#x60;transaction&#x60;. | [optional]  if omitted the server will use the default value of "transaction"
**id** | **str** | The unique identifier for this transaction. | [optional] 
**status** | **str** | The status of the transaction. The status may change over time as asynchronous  processing events occur. | [optional] 
**amount** | **int** | The authorized amount for this transaction. This can be different than the actual captured amount and part of this amount may be refunded. | [optional] 
**captured_amount** | **int** | The captured amount for this transaction. This can be a part and in some cases even more than the authorized amount. | [optional] 
**refunded_amount** | **int** | The refunded amount for this transaction. This can be a part or all of the captured amount. | [optional] 
**currency** | **str** | The currency code for this transaction. | [optional] 
**payment_method** | **object** |  | [optional] 
**buyer** | **object** |  | [optional] 
**created_at** | **datetime** | The date and time when this transaction was created in our system. | [optional] 
**external_identifier** | **str, none_type** | An external identifier that can be used to match the transaction against your own records. | [optional] 
**updated_at** | **datetime** | Defines when the transaction was last updated. | [optional] 
**payment_service** | **object** |  | [optional] 
**environment** | **str** | The environment this transaction has been created in. | [optional]  if omitted the server will use the default value of "production"

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


