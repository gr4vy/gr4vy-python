# TransactionRefundRequest

A request to refund a transaction.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **int** | The amount requested to refund.  If omitted, a full refund will be requested. Otherwise, the amount must be lower than or equal to the remaining balance in the associated transaction. Negative refunds are not supported. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


