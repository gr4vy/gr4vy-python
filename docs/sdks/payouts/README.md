# Payouts
(*payouts*)

## Overview

### Available Operations

* [list](#list) - List payouts created
* [create](#create) - Create a payout
* [get](#get) - Get a payout

## list

Returns a list of payouts made.

### Example Usage

```python
from gr4vy import Gr4vy
import os


with Gr4vy(
    merchant_account_id="default",
    bearer_auth=os.getenv("GR4VY_BEARER_AUTH", ""),
) as g_client:

    res = g_client.payouts.list(cursor="ZXhhbXBsZTE", limit=20)

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `cursor`                                                            | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | A pointer to the page of results to return.                         | ZXhhbXBsZTE                                                         |
| `limit`                                                             | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | The maximum number of items that are at returned.                   | 20                                                                  |
| `merchant_account_id`                                               | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | The ID of the merchant account to use for this request.             | default                                                             |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.ListPayoutsResponse](../../models/listpayoutsresponse.md)**

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

## create

Creates a new payout.

### Example Usage

```python
from gr4vy import Gr4vy
import os


with Gr4vy(
    merchant_account_id="default",
    bearer_auth=os.getenv("GR4VY_BEARER_AUTH", ""),
) as g_client:

    res = g_client.payouts.create(amount=1299, currency="EUR", payment_service_id="ed8bd87d-85ad-40cf-8e8f-007e21e55aad", payment_method={
        "method": "id",
        "id": "852b951c-d7ea-4c98-b09e-4a1c9e97c077",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                  | Type                                                                                                                                                       | Required                                                                                                                                                   | Description                                                                                                                                                | Example                                                                                                                                                    |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `amount`                                                                                                                                                   | *int*                                                                                                                                                      | :heavy_check_mark:                                                                                                                                         | The monetary amount for this payout, in the smallest currency unit for the given currency, for example `1299` cents to create an authorization for $12.99. | 1299                                                                                                                                                       |
| `currency`                                                                                                                                                 | *str*                                                                                                                                                      | :heavy_check_mark:                                                                                                                                         | The ISO-4217 currency code for this payout.                                                                                                                | EUR                                                                                                                                                        |
| `payment_service_id`                                                                                                                                       | *str*                                                                                                                                                      | :heavy_check_mark:                                                                                                                                         | The ID of the payment service to use for the payout.                                                                                                       | ed8bd87d-85ad-40cf-8e8f-007e21e55aad                                                                                                                       |
| `payment_method`                                                                                                                                           | [models.PayoutCreatePaymentMethod](../../models/payoutcreatepaymentmethod.md)                                                                              | :heavy_check_mark:                                                                                                                                         | The type of payment method to send funds too.                                                                                                              |                                                                                                                                                            |
| `merchant_account_id`                                                                                                                                      | *Optional[str]*                                                                                                                                            | :heavy_minus_sign:                                                                                                                                         | The ID of the merchant account to use for this request.                                                                                                    | default                                                                                                                                                    |
| `category`                                                                                                                                                 | [OptionalNullable[models.PayoutCategory]](../../models/payoutcategory.md)                                                                                  | :heavy_minus_sign:                                                                                                                                         | The type of payout to process.                                                                                                                             | online_gambling                                                                                                                                            |
| `external_identifier`                                                                                                                                      | *OptionalNullable[str]*                                                                                                                                    | :heavy_minus_sign:                                                                                                                                         | A value that can be used to match the payout against your own records.                                                                                     | payout-12345                                                                                                                                               |
| `buyer_id`                                                                                                                                                 | *OptionalNullable[str]*                                                                                                                                    | :heavy_minus_sign:                                                                                                                                         | The `id` of a stored buyer to use for this payout Use this instead of the `buyer` or `buyer_external_identifier`.                                          | fe26475d-ec3e-4884-9553-f7356683f7f9                                                                                                                       |
| `buyer`                                                                                                                                                    | [OptionalNullable[models.GuestBuyerInput]](../../models/guestbuyerinput.md)                                                                                | :heavy_minus_sign:                                                                                                                                         | Inline buyer details for the payout. Use this instead of the `buyer_id` or `buyer_external_identifier`.                                                    |                                                                                                                                                            |
| `buyer_external_identifier`                                                                                                                                | *OptionalNullable[str]*                                                                                                                                    | :heavy_minus_sign:                                                                                                                                         | The `external_identifier` of a stored buyer to use for this payout. Use this instead of the `buyer_id` or `buyer`.                                         | buyer-12345                                                                                                                                                |
| `merchant`                                                                                                                                                 | [OptionalNullable[models.PayoutMerchant]](../../models/payoutmerchant.md)                                                                                  | :heavy_minus_sign:                                                                                                                                         | Merchant information for the source of the payout.                                                                                                         |                                                                                                                                                            |
| `connection_options`                                                                                                                                       | [OptionalNullable[models.PayoutConnectionOptions]](../../models/payoutconnectionoptions.md)                                                                | :heavy_minus_sign:                                                                                                                                         | Optional fields for processing payouts on specific payment services.                                                                                       |                                                                                                                                                            |
| `retries`                                                                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                           | :heavy_minus_sign:                                                                                                                                         | Configuration to override the default retry behavior of the client.                                                                                        |                                                                                                                                                            |

### Response

**[models.PayoutSummary](../../models/payoutsummary.md)**

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

## get

Retrieves a payout.

### Example Usage

```python
from gr4vy import Gr4vy
import os


with Gr4vy(
    merchant_account_id="default",
    bearer_auth=os.getenv("GR4VY_BEARER_AUTH", ""),
) as g_client:

    res = g_client.payouts.get(payout_id="4344fef2-bc2f-49a6-924f-343e62f67224")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `payout_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |                                                                     |
| `merchant_account_id`                                               | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | The ID of the merchant account to use for this request.             | default                                                             |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.PayoutSummary](../../models/payoutsummary.md)**

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