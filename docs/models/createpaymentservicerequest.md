# CreatePaymentServiceRequest


## Fields

| Field                                                            | Type                                                             | Required                                                         | Description                                                      | Example                                                          |
| ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- |
| `payment_service_id`                                             | *str*                                                            | :heavy_check_mark:                                               | the ID of the payment service                                    | fffd152a-9532-4087-9a4f-de58754210f0                             |
| `merchant_account_id`                                            | *Optional[str]*                                                  | :heavy_minus_sign:                                               | The ID of the merchant account to use for this request.          | default                                                          |
| `payment_service_update`                                         | [models.PaymentServiceUpdate](../models/paymentserviceupdate.md) | :heavy_check_mark:                                               | N/A                                                              |                                                                  |