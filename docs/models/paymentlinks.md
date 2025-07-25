# PaymentLinks


## Fields

| Field                                                | Type                                                 | Required                                             | Description                                          | Example                                              |
| ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- |
| `items`                                              | List[[models.PaymentLink](../models/paymentlink.md)] | :heavy_check_mark:                                   | A list of items returned for this request.           |                                                      |
| `limit`                                              | *Optional[int]*                                      | :heavy_minus_sign:                                   | The number of items for this page.                   | 20                                                   |
| `next_cursor`                                        | *OptionalNullable[str]*                              | :heavy_minus_sign:                                   | The cursor pointing at the next page of items.       | ZXhhbXBsZTE                                          |
| `previous_cursor`                                    | *OptionalNullable[str]*                              | :heavy_minus_sign:                                   | The cursor pointing at the previous page of items.   | Xkjss7asS                                            |