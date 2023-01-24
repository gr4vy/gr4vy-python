# PaymentMethodTokenized

A mini format version of a payment method.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | &#x60;payment-method&#x60;. | [optional]  if omitted the server will use the default value of "payment-method"
**id** | **str** | The unique ID of the payment method. | [optional] 
**method** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | [optional] 
**label** | **str** | A label for the payment method. For a &#x60;card&#x60; payment method this is the last 4 digits on the card. For others it would be the email address. | [optional] 
**scheme** | **str, none_type** | The type of the card, if the payment method is a card. | [optional] 
**expiration_date** | **str, none_type** | The expiration date for the payment method. | [optional] 
**approval_target** | **str, none_type** | The browser target that an approval URL must be opened in. If &#x60;any&#x60; or &#x60;null&#x60;, then there is no specific requirement. | [optional] 
**approval_url** | **str, none_type** | The optional URL that the buyer needs to be redirected to to further authorize their payment. | [optional] 
**currency** | **str, none_type** | The ISO-4217 currency code that this payment method can be used for. If this value is &#x60;null&#x60; the payment method may be used for multiple currencies. | [optional] 
**country** | **str, none_type** | The 2-letter ISO code of the country this payment method can be used for. If this value is &#x60;null&#x60; the payment method may be used in multiple countries. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


