# PaymentOption

An available payment option for a locale.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | &#x60;payment-option&#x60;. | [optional]  if omitted the server will use the default value of "payment-option"
**method** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | [optional] 
**icon_url** | **str, none_type** | An icon to display for the payment option. | [optional] 
**mode** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | [optional] 
**label** | **str** | A label that describes this payment option. This label is returned in the language defined by the &#x60;locale&#x60; query parameter. The label can be used to display a list of payment options to the buyer in their language. | [optional] 
**can_store_payment_method** | **bool** | A flag to indicate if storing the payment method is supported. | [optional] 
**can_delay_capture** | **bool** | A flag to indicate if delayed capture is supported. | [optional] 
**context** | [**PaymentOptionContext**](PaymentOptionContext.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


