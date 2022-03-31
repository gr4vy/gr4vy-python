# DigitalWalletRequest

Merchant details used to register with a digital wallet provider.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider** | **str** | The name of the digital wallet provider. | 
**merchant_name** | **str** | The name of the merchant. This is used to register the merchant with a digital wallet provider and this name is not displayed to the buyer. | 
**domain_names** | **[str]** | The list of domain names that a digital wallet can be used on. To use a digital wallet on a website, the domain of the site is required to be in this list. | 
**accept_terms_and_conditions** | **bool** | The explicit acceptance of the digital wallet provider&#39;s terms and conditions by the merchant. Needs to be &#x60;true&#x60; to register a new digital wallet. | 
**merchant_url** | **str, none_type** | The main URL of the merchant. This is used to register the merchant with a digital wallet provider and this URL is not displayed to the buyer. | [optional]  if omitted the server will use the default value of "null"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


