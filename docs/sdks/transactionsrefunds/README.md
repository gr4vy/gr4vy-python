# TransactionsRefunds
(*transactions.refunds*)

## Overview

### Available Operations

* [list](#list) - List transaction refunds
* [create](#create) - Create transaction refund
* [get](#get) - Get transaction refund

## list

List refunds for a transaction.

### Example Usage

```python
from gr4vy import Gr4vy
import os


with Gr4vy(
    merchant_account_id="default",
    bearer_auth=os.getenv("GR4VY_BEARER_AUTH", ""),
) as g_client:

    res = g_client.transactions.refunds.list(transaction_id="7099948d-7286-47e4-aad8-b68f7eb44591")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `transaction_id`                                                    | *str*                                                               | :heavy_check_mark:                                                  | The ID of the transaction                                           | 7099948d-7286-47e4-aad8-b68f7eb44591                                |
| `merchant_account_id`                                               | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | The ID of the merchant account to use for this request.             | default                                                             |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.Refunds](../../models/refunds.md)**

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

Create a refund for a transaction.

### Example Usage

```python
from gr4vy import Gr4vy
import os


with Gr4vy(
    merchant_account_id="default",
    bearer_auth=os.getenv("GR4VY_BEARER_AUTH", ""),
) as g_client:

    res = g_client.transactions.refunds.create(transaction_id="7099948d-7286-47e4-aad8-b68f7eb44591")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                       | Type                                                                                                                            | Required                                                                                                                        | Description                                                                                                                     | Example                                                                                                                         |
| ------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| `transaction_id`                                                                                                                | *str*                                                                                                                           | :heavy_check_mark:                                                                                                              | The ID of the transaction                                                                                                       | 7099948d-7286-47e4-aad8-b68f7eb44591                                                                                            |
| `merchant_account_id`                                                                                                           | *Optional[str]*                                                                                                                 | :heavy_minus_sign:                                                                                                              | The ID of the merchant account to use for this request.                                                                         | default                                                                                                                         |
| `amount`                                                                                                                        | *OptionalNullable[int]*                                                                                                         | :heavy_minus_sign:                                                                                                              | The amount to refund, in the smallest currency unit (e.g., cents). If omitted, a full refund will be requested.                 | 1299                                                                                                                            |
| `target_type`                                                                                                                   | [Optional[models.RefundTargetType]](../../models/refundtargettype.md)                                                           | :heavy_minus_sign:                                                                                                              | N/A                                                                                                                             |                                                                                                                                 |
| `target_id`                                                                                                                     | *OptionalNullable[str]*                                                                                                         | :heavy_minus_sign:                                                                                                              | The optional ID of the instrument to refund for. This is only required when the `target_type` is set to `gift-card-redemption`. | 7a6c366d-9205-45ab-8021-0d9ee37f20f2                                                                                            |
| `reason`                                                                                                                        | *OptionalNullable[str]*                                                                                                         | :heavy_minus_sign:                                                                                                              | An optional reason to attach extra context to the refund request.                                                               | Refund due to user request.                                                                                                     |
| `external_identifier`                                                                                                           | *OptionalNullable[str]*                                                                                                         | :heavy_minus_sign:                                                                                                              | An external identifier that can be used to match the refund against your own records.                                           | refund-12345                                                                                                                    |
| `retries`                                                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                | :heavy_minus_sign:                                                                                                              | Configuration to override the default retry behavior of the client.                                                             |                                                                                                                                 |

### Response

**[models.Refund](../../models/refund.md)**

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

Fetch refund for a transaction.

### Example Usage

```python
from gr4vy import Gr4vy
import os


with Gr4vy(
    merchant_account_id="default",
    bearer_auth=os.getenv("GR4VY_BEARER_AUTH", ""),
) as g_client:

    res = g_client.transactions.refunds.get(transaction_id="7099948d-7286-47e4-aad8-b68f7eb44591", refund_id="6a1d4e46-14ed-4fe1-a45f-eff4e025d211")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `transaction_id`                                                    | *str*                                                               | :heavy_check_mark:                                                  | The ID of the transaction                                           | 7099948d-7286-47e4-aad8-b68f7eb44591                                |
| `refund_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | The ID of the refund                                                | 6a1d4e46-14ed-4fe1-a45f-eff4e025d211                                |
| `merchant_account_id`                                               | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | The ID of the merchant account to use for this request.             | default                                                             |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.Refund](../../models/refund.md)**

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