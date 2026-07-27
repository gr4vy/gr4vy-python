# GiftCards.Issuances

## Overview

### Available Operations

* [create](#create) - Issue a gift card

## create

Issue a new virtual gift card through the primary gift card service.

### Example Usage

<!-- UsageSnippet language="python" operationID="issue_gift_card" method="post" path="/gift-cards/issuances" -->
```python
from gr4vy import Gr4vy
import os


with Gr4vy(
    merchant_account_id="default",
    bearer_auth=os.getenv("GR4VY_BEARER_AUTH", ""),
) as g_client:

    res = g_client.gift_cards.issuances.create(theme="031111372", amount=5000, currency="EUR")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                             | Type                                                                                  | Required                                                                              | Description                                                                           | Example                                                                               |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `theme`                                                                               | *str*                                                                                 | :heavy_check_mark:                                                                    | The provider theme code to issue the gift card against.                               | 031111372                                                                             |
| `amount`                                                                              | *int*                                                                                 | :heavy_check_mark:                                                                    | The amount to load onto the gift card, in the smallest denomination for the currency. | 5000                                                                                  |
| `currency`                                                                            | *str*                                                                                 | :heavy_check_mark:                                                                    | The ISO-4217 currency code for the `amount`.                                          | **Example 1:** EUR<br/>**Example 2:** GBP<br/>**Example 3:** USD                      |
| `idempotency_key`                                                                     | *OptionalNullable[str]*                                                               | :heavy_minus_sign:                                                                    | A unique key forwarded to the gift card service to make the issuance idempotent.      |                                                                                       |
| `merchant_account_id`                                                                 | *Optional[str]*                                                                       | :heavy_minus_sign:                                                                    | The ID of the merchant account to use for this request.                               | default                                                                               |
| `external_identifier`                                                                 | *OptionalNullable[str]*                                                               | :heavy_minus_sign:                                                                    | An optional external identifier for this issuance.                                    | order-12345                                                                           |
| `retries`                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                      | :heavy_minus_sign:                                                                    | Configuration to override the default retry behavior of the client.                   |                                                                                       |

### Response

**[models.GiftCardIssuance](../../models/giftcardissuance.md)**

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