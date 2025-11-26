# BuyerUpdate

Request body for updating an existing buyer


## Fields

| Field                                                                  | Type                                                                   | Required                                                               | Description                                                            | Example                                                                |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `display_name`                                                         | *OptionalNullable[str]*                                                | :heavy_minus_sign:                                                     | The display name for the buyer.                                        | John Doe                                                               |
| `external_identifier`                                                  | *OptionalNullable[str]*                                                | :heavy_minus_sign:                                                     | The merchant identifier for this buyer.                                | buyer-12345                                                            |
| `account_number`                                                       | *OptionalNullable[str]*                                                | :heavy_minus_sign:                                                     | The buyer account number                                               |                                                                        |
| `billing_details`                                                      | [OptionalNullable[models.BillingDetails]](../models/billingdetails.md) | :heavy_minus_sign:                                                     | The billing name, address, email, and other fields for this buyer.     |                                                                        |