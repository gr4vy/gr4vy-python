# PaymentMethodTokenized

A mini format version of a payment method.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | &#x60;payment-method&#x60;. | [optional]  if omitted the server will use the default value of "payment-method"
**id** | **str** | The unique ID of the payment method. | [optional] 
**method** | **object** |  | [optional] 
**label** | **str** | A label for the payment method. For a &#x60;card&#x60; payment method this is the last 4 digits on the card. For others it would be the email address. | [optional] 
**scheme** | **str, none_type** | The type of the card, if the payment method is a card. | [optional] 
**expiration_date** | **str, none_type** | The expiration date for the payment method. | [optional] 
**approval_url** | **str, none_type** | The optional URL that the buyer needs to be redirected to to further authorize their payment. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


