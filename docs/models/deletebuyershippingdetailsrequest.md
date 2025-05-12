# DeleteBuyerShippingDetailsRequest


## Fields

| Field                                                   | Type                                                    | Required                                                | Description                                             | Example                                                 |
| ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- |
| `buyer_id`                                              | *str*                                                   | :heavy_check_mark:                                      | The ID of the buyer to delete shipping details for.     | fe26475d-ec3e-4884-9553-f7356683f7f9                    |
| `shipping_details_id`                                   | *str*                                                   | :heavy_check_mark:                                      | The ID of the shipping details to delete.               | bf8c36ad-02d9-4904-b0f9-a230b149e341                    |
| `timeout_in_seconds`                                    | *Optional[float]*                                       | :heavy_minus_sign:                                      | N/A                                                     |                                                         |
| `merchant_account_id`                                   | *Optional[str]*                                         | :heavy_minus_sign:                                      | The ID of the merchant account to use for this request. | default                                                 |