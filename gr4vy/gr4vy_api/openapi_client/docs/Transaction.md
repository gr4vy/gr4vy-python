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
**merchant_initiated** | **bool** | Indicates whether the transaction was initiated by the merchant (true) or customer (false). | [optional]  if omitted the server will use the default value of False
**payment_source** | **str** | The source of the transaction. Defaults to &#x60;ecommerce&#x60;. | [optional] 
**is_subsequent_payment** | **bool** | Indicates whether the transaction represents a subsequent payment coming from a setup recurring payment. Please note this flag is only compatible with &#x60;payment_source&#x60; set to &#x60;recurring&#x60;, &#x60;installment&#x60;, or &#x60;card_on_file&#x60; and will be ignored for other values or if &#x60;payment_source&#x60; is not present. | [optional]  if omitted the server will use the default value of False

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


