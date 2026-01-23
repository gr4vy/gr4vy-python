# ThreeDSecureScenarioConditions


## Fields

| Field                                | Type                                 | Required                             | Description                          | Example                              |
| ------------------------------------ | ------------------------------------ | ------------------------------------ | ------------------------------------ | ------------------------------------ |
| `first_name`                         | *OptionalNullable[str]*              | :heavy_minus_sign:                   | First name of the buyer to match.    | John                                 |
| `last_name`                          | *OptionalNullable[str]*              | :heavy_minus_sign:                   | Last name of the buyer to match.     | Luhn                                 |
| `email_address`                      | *OptionalNullable[str]*              | :heavy_minus_sign:                   | Email address of the buyer to match. | john@example.com                     |
| `amount`                             | *OptionalNullable[int]*              | :heavy_minus_sign:                   | Amount of the transaction to match.  | 100                                  |
| `external_identifier`                | *OptionalNullable[str]*              | :heavy_minus_sign:                   | External identifier to match.        | buyer-12345                          |
| `card_number`                        | *OptionalNullable[str]*              | :heavy_minus_sign:                   | Card number to match.                | 4242424242424242                     |