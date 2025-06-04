# PaymentOptionsSDK
(*payment_options*)

## Overview

### Available Operations

* [list](#list) - List payment options

## list

List the payment options available at checkout. filtering by country, currency, and additional fields passed to Flow rules.

### Example Usage

```python
from gr4vy import Gr4vy
import os


with Gr4vy(
    merchant_account_id="default",
    bearer_auth=os.getenv("GR4VY_BEARER_AUTH", ""),
) as g_client:

    res = g_client.payment_options.list(locale="en")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                     | Type                                                                                                                          | Required                                                                                                                      | Description                                                                                                                   | Example                                                                                                                       |
| ----------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| `merchant_account_id`                                                                                                         | *Optional[str]*                                                                                                               | :heavy_minus_sign:                                                                                                            | The ID of the merchant account to use for this request.                                                                       | default                                                                                                                       |
| `metadata`                                                                                                                    | Dict[str, *str*]                                                                                                              | :heavy_minus_sign:                                                                                                            | The metadata to used to evaluate checkout rules, which will help determine the right payment options to display.              | {<br/>"cohort": "a"<br/>}                                                                                                     |
| `country`                                                                                                                     | *OptionalNullable[str]*                                                                                                       | :heavy_minus_sign:                                                                                                            | The country code used to evaluate checkout rules, and which are used to help determine the right payment options to display.  | US                                                                                                                            |
| `currency`                                                                                                                    | *OptionalNullable[str]*                                                                                                       | :heavy_minus_sign:                                                                                                            | The currency code used to evaluate checkout rules, and which are used to help determine the right payment options to display. | USD                                                                                                                           |
| `amount`                                                                                                                      | *OptionalNullable[int]*                                                                                                       | :heavy_minus_sign:                                                                                                            | The amount used to evaluate checkout rules, and which are used to help determine the right payment options to display.        | 1299                                                                                                                          |
| `locale`                                                                                                                      | *Optional[str]*                                                                                                               | :heavy_minus_sign:                                                                                                            | The locale used to determine the labels for each payment option.                                                              | en                                                                                                                            |
| `cart_items`                                                                                                                  | List[[models.CartItem](../../models/cartitem.md)]                                                                             | :heavy_minus_sign:                                                                                                            | The cart items used to evaluate checkout rules, and which are used to help determine the right payment options to display.    |                                                                                                                               |
| `retries`                                                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                              | :heavy_minus_sign:                                                                                                            | Configuration to override the default retry behavior of the client.                                                           |                                                                                                                               |

### Response

**[models.PaymentOptions](../../models/paymentoptions.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.Error400            | 400                        | application/json           |
| errors.Error401            | 401                        | application/json           |
| errors.Error403            | 403                        | application/json           |
| errors.Error404            | 404                        | application/json           |
| errors.Error405            | 405                        | application/json           |
| errors.Error409            | 409                        | application/json           |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.Error425            | 425                        | application/json           |
| errors.Error429            | 429                        | application/json           |
| errors.Error500            | 500                        | application/json           |
| errors.Error502            | 502                        | application/json           |
| errors.Error504            | 504                        | application/json           |
| errors.APIError            | 4XX, 5XX                   | \*/\*                      |