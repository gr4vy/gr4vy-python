# PayoutPaymentService


## Fields

| Field                                                    | Type                                                     | Required                                                 | Description                                              | Example                                                  |
| -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- |
| `type`                                                   | *Optional[Literal["payment-service"]]*                   | :heavy_minus_sign:                                       | Always `payment-service`.                                | payment-service                                          |
| `id`                                                     | *OptionalNullable[str]*                                  | :heavy_minus_sign:                                       | The ID for the payout service.                           | b6c9eb12-2b62-4103-99b9-e3efc94e396d                     |
| `method`                                                 | *Optional[Literal["card"]]*                              | :heavy_minus_sign:                                       | Always `card`.                                           | card                                                     |
| `payment_service_definition_id`                          | *str*                                                    | :heavy_check_mark:                                       | The ID of the connection used for this payout.           | nuvei-card                                               |
| `display_name`                                           | *OptionalNullable[str]*                                  | :heavy_minus_sign:                                       | The display name of the connection used for this payout. | Nuvei                                                    |