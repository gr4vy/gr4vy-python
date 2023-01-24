# ShippingDetail

Shipping detail for a buyer.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of this resource. Is always &#x60;shipping-details&#x60;. | [optional]  if omitted the server will use the default value of "shipping-details"
**id** | **str** | The unique ID for a buyer&#39;s shipping detail. | [optional] 
**buyer_id** | **str** | The unique ID for a buyer. | [optional] 
**first_name** | **str, none_type** | The first name(s) or given name of the buyer. | [optional] 
**last_name** | **str, none_type** | The last name, or family name, of the buyer. | [optional] 
**email_address** | **str, none_type** | The email address of the buyer. | [optional] 
**phone_number** | **str, none_type** | The phone number of the buyer. This number is formatted according to the [E164 number standard](https://www.twilio.com/docs/glossary/what-e164). | [optional] 
**address** | **bool, date, datetime, dict, float, int, list, str, none_type** | The physical shipping address associated to this buyer. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


