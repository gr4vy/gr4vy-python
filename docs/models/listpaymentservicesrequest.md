# ListPaymentServicesRequest


## Fields

| Field                                                   | Type                                                    | Required                                                | Description                                             | Example                                                 |
| ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- |
| `method`                                                | [OptionalNullable[models.Method]](../models/method.md)  | :heavy_minus_sign:                                      | Return any payment service for this method.             |                                                         |
| `cursor`                                                | *OptionalNullable[str]*                                 | :heavy_minus_sign:                                      | A pointer to the page of results to return.             | ZXhhbXBsZTE                                             |
| `limit`                                                 | *Optional[int]*                                         | :heavy_minus_sign:                                      | The maximum number of items that are at returned.       | 20                                                      |
| `deleted`                                               | *OptionalNullable[bool]*                                | :heavy_minus_sign:                                      | Return any deleted payment service.                     | true                                                    |
| `merchant_account_id`                                   | *Optional[str]*                                         | :heavy_minus_sign:                                      | The ID of the merchant account to use for this request. | default                                                 |