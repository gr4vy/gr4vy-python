# GooglePayRequest

Details for a Google Pay payment method.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | The encrypted (opaque) token returned by the Google Pay API that represents a payment method. | 
**method** | **str** | &#x60;googlepay&#x60;. | defaults to "googlepay"
**assurance_details** | [**GooglePayRequestAssuranceDetails**](GooglePayRequestAssuranceDetails.md) |  | [optional] 
**card_holder_name** | **str, none_type** | Name of the card holder. | [optional] 
**redirect_url** | **str, none_type** | The redirect URL to redirect a buyer to after they have authorized their transaction or payment method. This only applies to payment methods that require buyer approval. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


