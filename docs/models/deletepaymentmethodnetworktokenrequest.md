# DeletePaymentMethodNetworkTokenRequest


## Fields

| Field                                                   | Type                                                    | Required                                                | Description                                             | Example                                                 |
| ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- |
| `payment_method_id`                                     | *str*                                                   | :heavy_check_mark:                                      | The ID of the payment method                            | ef9496d8-53a5-4aad-8ca2-00eb68334389                    |
| `network_token_id`                                      | *str*                                                   | :heavy_check_mark:                                      | The ID of the network token                             | f8dd5cfc-7834-4847-95dc-f75a360e2298                    |
| `application_name`                                      | *Optional[str]*                                         | :heavy_minus_sign:                                      | N/A                                                     |                                                         |
| `merchant_account_id`                                   | *Optional[str]*                                         | :heavy_minus_sign:                                      | The ID of the merchant account to use for this request. | default                                                 |