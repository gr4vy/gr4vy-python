# Refund

A refund record.  A refund is always associated with a single transaction, while a transaction can potentially have several refunds.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of this resource. Is always &#x60;refund&#x60;. | [optional]  if omitted the server will use the default value of "refund"
**id** | **str** | The unique ID of the refund. | [optional] 
**transaction_id** | **str** | The ID of the transaction associated with this refund. | [optional] 
**status** | **str** | The status of the refund. It may change over time as asynchronous processing events occur.  - &#x60;processing&#x60; - The refund is being processed. - &#x60;succeeded&#x60; - The refund was successful. - &#x60;declined&#x60; - The refund was declined by the underlying PSP. - &#x60;failed&#x60; - The refund could not proceed due to a technical issue. - &#x60;voided&#x60; - The refund was voided and will not proceed. | [optional] 
**currency** | **str** | The currency code for this refund. Will always match that of the associated transaction. | [optional] 
**amount** | **int** | The amount requested for this refund. | [optional] 
**created_at** | **datetime** | The date and time when this refund was created. | [optional] 
**updated_at** | **datetime** | The date and time when this refund was last updated. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


