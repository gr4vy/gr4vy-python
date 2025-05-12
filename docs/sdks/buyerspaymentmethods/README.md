# BuyersPaymentMethods
(*buyers.payment_methods*)

## Overview

### Available Operations

* [list](#list) - List payment methods for a buyer

## list

List all the stored payment methods for a specific buyer.

### Example Usage

```python
from gr4vy import Gr4vy
import os


with Gr4vy(
    bearer_auth=os.getenv("GR4VY_BEARER_AUTH", ""),
    merchant_account_id="default",
) as g_client:

    res = g_client.buyers.payment_methods.list(buyer_id="fe26475d-ec3e-4884-9553-f7356683f7f9", buyer_external_identifier="buyer-12345", country="US", currency="USD", merchant_account_id="default")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                     | Type                                                                                                          | Required                                                                                                      | Description                                                                                                   | Example                                                                                                       |
| ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| `buyer_id`                                                                                                    | *OptionalNullable[str]*                                                                                       | :heavy_minus_sign:                                                                                            | The ID of the buyer to query payment methods for.                                                             | fe26475d-ec3e-4884-9553-f7356683f7f9                                                                          |
| `buyer_external_identifier`                                                                                   | *OptionalNullable[str]*                                                                                       | :heavy_minus_sign:                                                                                            | The external identifier of the buyer to query payment methods for.                                            | buyer-12345                                                                                                   |
| `order_by`                                                                                                    | [Optional[models.OrderBy]](../../models/orderby.md)                                                           | :heavy_minus_sign:                                                                                            | The direction to sort the payment methods in.                                                                 | desc                                                                                                          |
| `country`                                                                                                     | *OptionalNullable[str]*                                                                                       | :heavy_minus_sign:                                                                                            | The country code to filter payment methods by. This only applies to payment methods with a `country` value.   | US                                                                                                            |
| `currency`                                                                                                    | *OptionalNullable[str]*                                                                                       | :heavy_minus_sign:                                                                                            | The currency code to filter payment methods by. This only applies to payment methods with a `currency` value. | USD                                                                                                           |
| `merchant_account_id`                                                                                         | *Optional[str]*                                                                                               | :heavy_minus_sign:                                                                                            | The ID of the merchant account to use for this request.                                                       | default                                                                                                       |
| `retries`                                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                              | :heavy_minus_sign:                                                                                            | Configuration to override the default retry behavior of the client.                                           |                                                                                                               |

### Response

**[models.CollectionNoCursorPaymentMethodSummary](../../models/collectionnocursorpaymentmethodsummary.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.Error400            | 400                        | application/json           |
| errors.Error401            | 401                        | application/json           |
| errors.Error403            | 403                        | application/json           |
| errors.Error403Forbidden   | 403                        | application/json           |
| errors.Error403Active      | 403                        | application/json           |
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