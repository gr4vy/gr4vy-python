# RedirectRequest

Request to use a redirect payment method in a transaction.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**method** | **object** |  | 
**redirect_url** | **str** | The redirect URL to redirect a buyer to after they have authorized their transaction. | 
**currency** | **str** | The ISO-4217 currency code to use this payment method for. This is used to select the payment service to use. | 
**country** | **str** | The 2-letter ISO code of the country to use this payment method for. This is used to select the payment service to use. | 
**external_identifier** | **str, none_type** | An external identifier that can be used to match the account against your own records. | [optional] 
**buyer_id** | **str** | The ID of the buyer to associate this payment method to. If this field is provided then the &#x60;buyer_external_identifier&#x60; field needs to be unset. | [optional] 
**buyer_external_identifier** | **str** | The &#x60;external_identifier&#x60; of the buyer to associate this payment method to. If this field is provided then the &#x60;buyer_id&#x60; field needs to be unset. | [optional] 
**environment** | **str** | Defines the environment to store this payment method in. Setting this to anything other than &#x60;production&#x60; will force Gr4vy to use a payment a service configured for that environment. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


