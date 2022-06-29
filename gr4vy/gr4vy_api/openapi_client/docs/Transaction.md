# Transaction

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
**merchant_initiated** | **bool** | Indicates whether the transaction was initiated by the merchant (true) or customer (false). | [optional]  if omitted the server will use the default value of False
**payment_source** | **str** | The source of the transaction. Defaults to &#x60;ecommerce&#x60;. | [optional] 
**is_subsequent_payment** | **bool** | Indicates whether the transaction represents a subsequent payment coming from a setup recurring payment. Please note there are some restrictions on how this flag may be used.  The flag can only be &#x60;false&#x60; (or not set) when the transaction meets one of the following criteria:  * It is not &#x60;merchant_initiated&#x60;. * &#x60;payment_source&#x60; is set to &#x60;card_on_file&#x60;.  The flag can only be set to &#x60;true&#x60; when the transaction meets one of the following criteria:  * It is not &#x60;merchant_initiated&#x60;. * &#x60;payment_source&#x60; is set to &#x60;recurring&#x60; or &#x60;installment&#x60; and &#x60;merchant_initiated&#x60; is set to &#x60;true&#x60;. * &#x60;payment_source&#x60; is set to &#x60;card_on_file&#x60;. | [optional]  if omitted the server will use the default value of False
**statement_descriptor** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | [optional] 
**cart_items** | [**[CartItem]**](CartItem.md) | An array of cart items that represents the line items of a transaction. | [optional] 
**scheme_transaction_id** | **str, none_type** | An identifier for the transaction used by the scheme itself, when available.  e.g. the Visa Transaction Identifier, or Mastercard Trace ID. | [optional]  if omitted the server will use the default value of "null"
**raw_response_code** | **str, none_type** | This is the response code received from the payment service. This can be set to any value and is not standardized across different payment services. | [optional] 
**raw_response_description** | **str, none_type** | This is the response description received from the payment service. This can be set to any value and is not standardized across different payment services. | [optional] 
**avs_response_code** | **str, none_type** | The response code received from the payment service for the Address Verification Check (AVS). This code is mapped to a standardized Gr4vy AVS response code.  - &#x60;no_match&#x60; - neither address or postal code match - &#x60;match&#x60; - both address and postal code match - &#x60;partial_match_address&#x60; - address matches but postal code does not - &#x60;partial_match_postcode&#x60; - postal code matches but address does not - &#x60;unavailable &#x60; - AVS is unavailable for card/country  The value of this field can be &#x60;null&#x60; if the payment service did not provide a response. | [optional] 
**cvv_response_code** | **str, none_type** | The response code received from the payment service for the Card Verification Value (CVV). This code is mapped to a standardized Gr4vy CVV response code.  - &#x60;no_match&#x60; - the CVV does not match the expected value - &#x60;match&#x60; - the CVV matches the expected value - &#x60;unavailable &#x60; - CVV check unavailable for card our country - &#x60;not_provided &#x60; - CVV not provided  The value of this field can be &#x60;null&#x60; if the payment service did not provide a response. | [optional] 
**method** | **str** |  | [optional] 
**payment_service_transaction_id** | **str** | The payment service&#39;s unique ID for the transaction. | [optional] 
**metadata** | **{str: (str,)}** | Additional information about the transaction stored as key-value pairs. | [optional] 
**three_d_secure** | [**ThreeDSecureSummary**](ThreeDSecureSummary.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


