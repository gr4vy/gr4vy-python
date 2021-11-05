# PaymentService

An active, configured payment service.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of this payment service. | [optional] 
**type** | **str** | The type of this resource. | [optional]  if omitted the server will use the default value of "payment-service"
**payment_service_definition_id** | **str** | The ID of the payment service definition used to create this service.  | [optional] 
**method** | **object** |  | [optional] 
**display_name** | **str** | The custom name set for this service. | [optional] 
**status** | **str** | The current status of this service. This will start off as pending, move to created, and might eventually move to an error status if and when the credentials are no longer valid.  | [optional] 
**accepted_currencies** | **[str]** | A list of currencies for which this service is enabled, in ISO 4217 three-letter code format. | [optional] 
**accepted_countries** | **[str]** | A list of countries for which this service is enabled, in ISO two-letter code format. | [optional] 
**three_d_secure_enabled** | **bool** | Defines if 3-D Secure is enabled for the service (can only be enabled if the payment service definition supports the &#x60;three_d_secure_hosted&#x60; feature). This does not affect pass through 3-D Secure data. | [optional]  if omitted the server will use the default value of False
**acquirer_bin_visa** | **str, none_type** | Acquiring institution identification code for VISA. | [optional] 
**acquirer_bin_mastercard** | **str, none_type** | Acquiring institution identification code for Mastercard. | [optional] 
**acquirer_bin_amex** | **str, none_type** | Acquiring institution identification code for Amex. | [optional] 
**acquirer_bin_discover** | **str, none_type** | Acquiring institution identification code for Discover. | [optional] 
**acquirer_merchant_id** | **str, none_type** | Merchant identifier used in authorisation requests (assigned by the acquirer). | [optional] 
**merchant_name** | **str, none_type** | Merchant name (assigned by the acquirer). | [optional] 
**merchant_country_code** | **str, none_type** | ISO 3166-1 numeric three-digit country code. | [optional] 
**merchant_category_code** | **str, none_type** | Merchant category code that describes the business. | [optional] 
**merchant_url** | **str, none_type** | Fully qualified URL of 3-D Secure requestor website or customer care site. | [optional] 
**credentials_mode** | **str** | Defines if the credentials are intended for the service&#39;s live API or sandbox/test API. | [optional]  if omitted the server will use the default value of "live"
**active** | **bool** | Defines if this service is currently active or not. | [optional]  if omitted the server will use the default value of True
**environments** | **[str]** | Determines the Gr4vy environments in which this service should be available. This can be used in combination with the &#x60;environment&#x60; parameters in the payment method and transaction APIs to route transactions through this service. | [optional]  if omitted the server will use the default value of ["production"]
**position** | **float** | The numeric rank of a payment service. Payment services with a lower position value are processed first. | [optional] 
**created_at** | **datetime** | The date and time when this service was created. | [optional] 
**updated_at** | **datetime** | The date and time when this service was last updated. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


