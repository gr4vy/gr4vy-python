# PaymentOptionsRequest

A request to get list of payment options.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **int, none_type** | The monetary amount to create an authorization for, in the smallest currency unit for the given currency, for example &#x60;1299&#x60; cents to create an authorization for &#x60;$12.99&#x60;.  If the &#x60;intent&#x60; is set to &#x60;capture&#x60;, an amount greater than zero must be supplied. | [optional] 
**locale** | **str, none_type** | An ISO 639-1 Language Code and optional ISO 3166 Country Code. This locale determines the language for the labels returned for every payment option. | [optional]  if omitted the server will use the default value of "en"
**currency** | **str, none_type** | A supported ISO-4217 currency code.  For redirect requests, this value must match the one specified for &#x60;currency&#x60; in &#x60;payment_method&#x60;.  | [optional] 
**country** | **str, none_type** | Filters the results to only the items which support this country code. A country is formatted as 2-letter ISO country code.  | [optional] 
**metadata** | **{str: (str,)}, none_type** | Used by the Flow engine to filter available options based on various client-defined parameters. If present, this must be a string representing a valid JSON dictionary. | [optional] 
**cart_items** | [**[CartItem], none_type**](CartItem.md) | An array of cart items that represents the line items of a transaction. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


