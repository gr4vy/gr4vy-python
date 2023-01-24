# PaymentOptionContext

Additional context specific to the payment option. This is currently only returned for Apple Pay and Google Pay.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gateway** | **str** | Gateway used for Google Pay payments. | [optional] 
**gateway_merchant_id** | **str** | Gateway merchant identifier used for Google Pay payments. | [optional] 
**merchant_name** | **str** | Display name of the merchant as registered with the digital wallet provider. | [optional] 
**supported_schemes** | **[str]** | Card schemes supported by the digital wallet provider. | [optional] 
**approval_ui** | [**PaymentOptionApprovalUI**](PaymentOptionApprovalUI.md) |  | [optional] 
**required_fields** | [**RequiredFields**](RequiredFields.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


