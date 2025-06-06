# BuyersSDK
(*buyers*)

## Overview

### Available Operations

* [list](#list) - List all buyers
* [create](#create) - Add a buyer
* [get](#get) - Get a buyer
* [update](#update) - Update a buyer
* [delete](#delete) - Delete a buyer

## list

List all buyers or search for a specific buyer.

### Example Usage

```python
from gr4vy import Gr4vy
import os


with Gr4vy(
    merchant_account_id="default",
    bearer_auth=os.getenv("GR4VY_BEARER_AUTH", ""),
) as g_client:

    res = g_client.buyers.list(cursor="ZXhhbXBsZTE", limit=20, search="John", external_identifier="buyer-12345")

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                                                                        | Type                                                                                                             | Required                                                                                                         | Description                                                                                                      | Example                                                                                                          |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `cursor`                                                                                                         | *OptionalNullable[str]*                                                                                          | :heavy_minus_sign:                                                                                               | A pointer to the page of results to return.                                                                      | ZXhhbXBsZTE                                                                                                      |
| `limit`                                                                                                          | *Optional[int]*                                                                                                  | :heavy_minus_sign:                                                                                               | The maximum number of items that are at returned.                                                                | 20                                                                                                               |
| `search`                                                                                                         | *OptionalNullable[str]*                                                                                          | :heavy_minus_sign:                                                                                               | Filters the results to only the buyers for which the `display_name` or `external_identifier` matches this value. | John                                                                                                             |
| `external_identifier`                                                                                            | *OptionalNullable[str]*                                                                                          | :heavy_minus_sign:                                                                                               | Filters the results to only the buyers for which the `external_identifier` matches this value.                   | buyer-12345                                                                                                      |
| `merchant_account_id`                                                                                            | *Optional[str]*                                                                                                  | :heavy_minus_sign:                                                                                               | The ID of the merchant account to use for this request.                                                          | default                                                                                                          |
| `retries`                                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                 | :heavy_minus_sign:                                                                                               | Configuration to override the default retry behavior of the client.                                              |                                                                                                                  |

### Response

**[models.ListBuyersResponse](../../models/listbuyersresponse.md)**

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

Create a new buyer record.

### Example Usage

```python
from gr4vy import Gr4vy
import os


with Gr4vy(
    merchant_account_id="default",
    bearer_auth=os.getenv("GR4VY_BEARER_AUTH", ""),
) as g_client:

    res = g_client.buyers.create()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                           | Type                                                                                | Required                                                                            | Description                                                                         | Example                                                                             |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `merchant_account_id`                                                               | *Optional[str]*                                                                     | :heavy_minus_sign:                                                                  | The ID of the merchant account to use for this request.                             | default                                                                             |
| `display_name`                                                                      | *OptionalNullable[str]*                                                             | :heavy_minus_sign:                                                                  | The display name for the buyer.                                                     | John Doe                                                                            |
| `external_identifier`                                                               | *OptionalNullable[str]*                                                             | :heavy_minus_sign:                                                                  | The merchant identifier for this buyer.                                             | buyer-12345                                                                         |
| `billing_details`                                                                   | [OptionalNullable[models.BillingDetailsInput]](../../models/billingdetailsinput.md) | :heavy_minus_sign:                                                                  | The billing name, address, email, and other fields for this buyer.                  |                                                                                     |
| `account_number`                                                                    | *OptionalNullable[str]*                                                             | :heavy_minus_sign:                                                                  | The buyer account number                                                            |                                                                                     |
| `retries`                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                    | :heavy_minus_sign:                                                                  | Configuration to override the default retry behavior of the client.                 |                                                                                     |

### Response

**[models.Buyer](../../models/buyer.md)**

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

Fetches a buyer by its ID.

### Example Usage

```python
from gr4vy import Gr4vy
import os


with Gr4vy(
    merchant_account_id="default",
    bearer_auth=os.getenv("GR4VY_BEARER_AUTH", ""),
) as g_client:

    res = g_client.buyers.get(buyer_id="fe26475d-ec3e-4884-9553-f7356683f7f9")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `buyer_id`                                                          | *str*                                                               | :heavy_check_mark:                                                  | The ID of the buyer to retrieve.                                    | fe26475d-ec3e-4884-9553-f7356683f7f9                                |
| `merchant_account_id`                                               | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | The ID of the merchant account to use for this request.             | default                                                             |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.Buyer](../../models/buyer.md)**

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

## update

Updates a buyer record.

### Example Usage

```python
from gr4vy import Gr4vy
import os


with Gr4vy(
    merchant_account_id="default",
    bearer_auth=os.getenv("GR4VY_BEARER_AUTH", ""),
) as g_client:

    res = g_client.buyers.update(buyer_id="fe26475d-ec3e-4884-9553-f7356683f7f9")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                           | Type                                                                                | Required                                                                            | Description                                                                         | Example                                                                             |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `buyer_id`                                                                          | *str*                                                                               | :heavy_check_mark:                                                                  | The ID of the buyer to edit.                                                        | fe26475d-ec3e-4884-9553-f7356683f7f9                                                |
| `merchant_account_id`                                                               | *Optional[str]*                                                                     | :heavy_minus_sign:                                                                  | The ID of the merchant account to use for this request.                             | default                                                                             |
| `display_name`                                                                      | *OptionalNullable[str]*                                                             | :heavy_minus_sign:                                                                  | The display name for the buyer.                                                     | John Doe                                                                            |
| `external_identifier`                                                               | *OptionalNullable[str]*                                                             | :heavy_minus_sign:                                                                  | The merchant identifier for this buyer.                                             | buyer-12345                                                                         |
| `account_number`                                                                    | *OptionalNullable[str]*                                                             | :heavy_minus_sign:                                                                  | The buyer account number                                                            |                                                                                     |
| `billing_details`                                                                   | [OptionalNullable[models.BillingDetailsInput]](../../models/billingdetailsinput.md) | :heavy_minus_sign:                                                                  | The billing name, address, email, and other fields for this buyer.                  |                                                                                     |
| `retries`                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                    | :heavy_minus_sign:                                                                  | Configuration to override the default retry behavior of the client.                 |                                                                                     |

### Response

**[models.Buyer](../../models/buyer.md)**

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

## delete

Permanently removes a buyer record.

### Example Usage

```python
from gr4vy import Gr4vy
import os


with Gr4vy(
    merchant_account_id="default",
    bearer_auth=os.getenv("GR4VY_BEARER_AUTH", ""),
) as g_client:

    g_client.buyers.delete(buyer_id="fe26475d-ec3e-4884-9553-f7356683f7f9")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `buyer_id`                                                          | *str*                                                               | :heavy_check_mark:                                                  | The ID of the buyer to delete.                                      | fe26475d-ec3e-4884-9553-f7356683f7f9                                |
| `merchant_account_id`                                               | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | The ID of the merchant account to use for this request.             | default                                                             |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

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