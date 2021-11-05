# DigitalWalletRequest

Merchant details used to register with a digital wallet provider.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**merchant_name** | **str** | The name of the merchant. This is used to register the merchant with a digital wallet provider and this name is not displayed to the buyer. | 
**domain_names** | **[str]** | The list of fully qualified domain names that a digital wallet provider should process payments for. | 
**accept_terms_and_conditions** | **bool** | The explicit acceptance of the digital wallet provider&#39;s terms and conditions by the merchant. Needs to be &#x60;true&#x60; to register a new digital wallet. | 
**provider** | **str** | The name of the digital wallet provider. | defaults to "apple"
**merchant_url** | **str, none_type** | The main URL of the merchant. This is used to register the merchant with a digital wallet provider and this URL is not displayed to the buyer. | [optional]  if omitted the server will use the default value of "null"
**environments** | **[str]** | Determines the Gr4vy environments in which this digital wallet should be available. | [optional]  if omitted the server will use the default value of ["production"]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


