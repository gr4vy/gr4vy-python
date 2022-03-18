# CartItem

A cart item that represents a single cart line item for a transaction. Note that some optional properties are required for certain payment service providers. If no value is set for these properties, we will use their default value.  If the total due to be paid for the item is required by the payment service provider, generally referred to as the \"total amount\", the formula below will usually be used to calculate this amount:  `(unit_amount * quantity) - discount_amount + tax_amount`  It's highly recommended that the total amount to pay for all items should match the transaction's amount to reduce the risk of the transaction being declined by the payment service provider.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the cart item. The value you set for this property may be truncated if the maximum length accepted by a payment service provider is less than 255 characters. | 
**quantity** | **int** | The quantity of this item in the cart. This value cannot be negative or zero. | 
**unit_amount** | **int** | The amount for an individual item represented as a monetary amount in the smallest currency unit for the given currency, for example &#x60;1299&#x60; USD cents represents &#x60;$12.99&#x60;. | 
**discount_amount** | **int, none_type** | The amount discounted for this item represented as a monetary amount in the smallest currency unit for the given currency, for example &#x60;1299&#x60; USD cents represents &#x60;$12.99&#x60;.  Please note that this amount is for the total of the cart item and not for an individual item. For example, if the quantity is 5, this value should be the total discount amount for 5 of the cart item.  You might see unexpected failed transactions if the &#x60;discount_amount&#x60; can not be equally divided by the &#x60;quantity&#x60; value. This is due to the fact that some payment services require this amount to be specified per unit.  In this situation we recommend splitting this item into separate items, each with their own specific discount. | [optional]  if omitted the server will use the default value of 0
**tax_amount** | **int, none_type** | The tax amount for this item represented as a monetary amount in the smallest currency unit for the given currency, for example &#x60;1299&#x60; USD cents represents &#x60;$12.99&#x60;.  Please not that this amount is for the total of the cart item and not for an individual item. For example, if the quantity is 5, this value should be the total tax amount for 5 of the cart item.  You might see unexpected failed transactions if the &#x60;tax_amount&#x60; can not be equally divided by the &#x60;quantity&#x60; value. This is due to the fact that some payment services require this amount to be specified per unit.  In this situation we recommend splitting this item into separate items, each with their own specific tax amount. | [optional]  if omitted the server will use the default value of 0
**external_identifier** | **str, none_type** | An external identifier for the cart item. This can be set to any value and is not sent to the payment service. | [optional] 
**sku** | **str, none_type** | The SKU for the item. | [optional] 
**product_url** | **str, none_type** | The product URL for the item. | [optional] 
**image_url** | **str, none_type** | The URL for the image of the item. | [optional] 
**categories** | **[str], none_type** | A list of strings containing product categories for the item. Max length per item: 50. | [optional] 
**product_type** | **str, none_type** | The product type of the cart item. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


