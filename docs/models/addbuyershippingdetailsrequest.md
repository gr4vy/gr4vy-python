# AddBuyerShippingDetailsRequest


## Fields

| Field                                                              | Type                                                               | Required                                                           | Description                                                        | Example                                                            |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `buyer_id`                                                         | *str*                                                              | :heavy_check_mark:                                                 | The ID of the buyer to add shipping details to.                    | fe26475d-ec3e-4884-9553-f7356683f7f9                               |
| `merchant_account_id`                                              | *Optional[str]*                                                    | :heavy_minus_sign:                                                 | The ID of the merchant account to use for this request.            | default                                                            |
| `shipping_details_create`                                          | [models.ShippingDetailsCreate](../models/shippingdetailscreate.md) | :heavy_check_mark:                                                 | N/A                                                                |                                                                    |