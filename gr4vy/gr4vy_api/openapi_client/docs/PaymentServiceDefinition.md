# PaymentServiceDefinition

An available payment service that can be configured.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of the payment service. This is the underlying provider followed by a dash followed by the payment method ID. | [optional] 
**type** | **str** | &#x60;payment-service-definition&#x60;. | [optional]  if omitted the server will use the default value of "payment-service-definition"
**display_name** | **str** | The display name of this service. | [optional] 
**method** | **object** |  | [optional] 
**fields** | [**[PaymentServiceDefinitionFields]**](PaymentServiceDefinitionFields.md) | A list of fields that need to be submitted when activating the payment. service. | [optional] 
**supported_currencies** | **[str]** | A list of three-letter ISO currency codes that this service supports. | [optional] 
**supported_countries** | **[str]** | A list of two-letter ISO country codes that this service supports. | [optional] 
**mode** | **object** |  | [optional] 
**supported_features** | [**PaymentServiceDefinitionSupportedFeatures**](PaymentServiceDefinitionSupportedFeatures.md) |  | [optional] 
**icon_url** | **str, none_type** | An icon to display for the payment service. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


