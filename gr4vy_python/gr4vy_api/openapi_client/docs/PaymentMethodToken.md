# PaymentMethodToken

A token for a payment method.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | &#x60;payment-method-token&#x60;. | [optional]  if omitted the server will use the default value of "payment-method-token"
**id** | **str** | The external ID of this payment method as it has been registered with the payment service, which can be used directly in combination with the &#x60;token&#x60; without the need to go through Gr4vy for a transaction.  In some cases this is a different value to the &#x60;token&#x60; while in others this value is identical. Please see the documentation for the payment service for more details. | [optional] 
**token** | **str** | The token of this payment method as it has been registered with the payment service, which can be used directly in combination with the &#x60;id&#x60; without the need to go through Gr4vy for a transaction.  In some cases this is a different value to the &#x60;id&#x60; while in others this value is identical. Please see the documentation for the payment service for more details. | [optional] 
**payment_service** | **object** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


