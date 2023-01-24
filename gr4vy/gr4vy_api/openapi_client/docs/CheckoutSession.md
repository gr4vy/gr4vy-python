# CheckoutSession

A short-lived checkout session.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | &#x60;checkout-session&#x60;. | [optional]  if omitted the server will use the default value of "checkout-session"
**id** | **str** | The ID of the Checkout Session. | [optional] 
**expires_at** | **datetime** | The date and time when the Checkout Session will expire. By default this will be set to 1 hour from the date of creation. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


