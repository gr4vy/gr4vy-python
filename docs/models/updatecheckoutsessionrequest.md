# UpdateCheckoutSessionRequest


## Fields

| Field                                                              | Type                                                               | Required                                                           | Description                                                        | Example                                                            |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `session_id`                                                       | *str*                                                              | :heavy_check_mark:                                                 | The ID of the checkout session.                                    | 4137b1cf-39ac-42a8-bad6-1c680d5dab6b                               |
| `merchant_account_id`                                              | *Optional[str]*                                                    | :heavy_minus_sign:                                                 | The ID of the merchant account to use for this request.            | default                                                            |
| `checkout_session_create`                                          | [models.CheckoutSessionCreate](../models/checkoutsessioncreate.md) | :heavy_check_mark:                                                 | N/A                                                                |                                                                    |