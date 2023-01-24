# TransactionSummary

A transaction record.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of this resource. Is always &#x60;transaction&#x60;. | [optional]  if omitted the server will use the default value of "transaction"
**id** | **str** | The unique identifier for this transaction. | [optional] 
**status** | **str** | The status of the transaction. The status may change over time as asynchronous processing events occur. | [optional] 
**intent** | **str** | The original &#x60;intent&#x60; used when the transaction was [created](#operation/authorize-new-transaction). | [optional] 
**amount** | **int** | The authorized amount for this transaction. This can be more than the actual captured amount and part of this amount may be refunded. | [optional] 
**captured_amount** | **int** | The captured amount for this transaction. This can be the total or a portion of the authorized amount. | [optional] 
**refunded_amount** | **int** | The refunded amount for this transaction. This can be the total or a portion of the captured amount. | [optional] 
**currency** | **str** | The currency code for this transaction. | [optional] 
**country** | **str, none_type** | The 2-letter ISO code of the country of the transaction. This is used to filter the payment services that is used to process the transaction.  | [optional] 
**payment_method** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | [optional] 
**buyer** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | [optional] 
**created_at** | **datetime** | The date and time when this transaction was created in our system. | [optional] 
**external_identifier** | **str, none_type** | An external identifier that can be used to match the transaction against your own records. | [optional] 
**updated_at** | **datetime** | Defines when the transaction was last updated. | [optional] 
**payment_service** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | [optional] 
**method** | **str** |  | [optional] 
**raw_response_code** | **str, none_type** | This is the response code received from the payment service. This can be set to any value and is not standardized across different payment services. | [optional] 
**raw_response_description** | **str, none_type** | This is the response description received from the payment service. This can be set to any value and is not standardized across different payment services. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


