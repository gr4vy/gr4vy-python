# ListPayoutsRequest


## Fields

| Field                                                   | Type                                                    | Required                                                | Description                                             | Example                                                 |
| ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- |
| `cursor`                                                | *OptionalNullable[str]*                                 | :heavy_minus_sign:                                      | A pointer to the page of results to return.             | ZXhhbXBsZTE                                             |
| `limit`                                                 | *Optional[int]*                                         | :heavy_minus_sign:                                      | The maximum number of items that are at returned.       | 20                                                      |
| `application_name`                                      | *Optional[str]*                                         | :heavy_minus_sign:                                      | N/A                                                     |                                                         |
| `merchant_account_id`                                   | *Optional[str]*                                         | :heavy_minus_sign:                                      | The ID of the merchant account to use for this request. | default                                                 |