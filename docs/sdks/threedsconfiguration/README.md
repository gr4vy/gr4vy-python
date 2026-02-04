# MerchantAccounts.ThreeDsConfiguration

## Overview

### Available Operations

* [create](#create) - Create 3DS configuration for merchant
* [list](#list) - List 3DS configurations for merchant
* [update](#update) - Edit 3DS configuration
* [delete](#delete) - Delete 3DS configuration for a merchant

## create

Create a new 3DS configuration for a merchant account.

### Example Usage

<!-- UsageSnippet language="python" operationID="create_three_ds_configuration" method="post" path="/merchant-accounts/{merchant_account_id}/three-ds-configurations" -->
```python
from gr4vy import Gr4vy
import os


with Gr4vy(
    bearer_auth=os.getenv("GR4VY_BEARER_AUTH", ""),
) as g_client:

    res = g_client.merchant_accounts.three_ds_configuration.create(merchant_account_id="merchant-12345", merchant_acquirer_bin="516327", merchant_acquirer_id="123456789012345", merchant_name="Acme Inc.", merchant_country_code="840", merchant_category_code="1234", merchant_url="https://example.com", scheme="visa", metadata={
        "key": "<value>",
        "key1": "<value>",
        "key2": "<value>",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                               | Type                                                                                                    | Required                                                                                                | Description                                                                                             | Example                                                                                                 |
| ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| `merchant_account_id`                                                                                   | *str*                                                                                                   | :heavy_check_mark:                                                                                      | The ID of the merchant account.                                                                         | merchant-12345                                                                                          |
| `merchant_acquirer_bin`                                                                                 | *str*                                                                                                   | :heavy_check_mark:                                                                                      | Acquirer BIN to use when calling 3DS through this scheme.                                               | 516327                                                                                                  |
| `merchant_acquirer_id`                                                                                  | *str*                                                                                                   | :heavy_check_mark:                                                                                      | Merchant ID to use when calling 3DS through this scheme.                                                | 123456789012345                                                                                         |
| `merchant_name`                                                                                         | *str*                                                                                                   | :heavy_check_mark:                                                                                      | N/A                                                                                                     | Acme Inc.                                                                                               |
| `merchant_country_code`                                                                                 | *str*                                                                                                   | :heavy_check_mark:                                                                                      | The merchant's ISO 3166-1 numeric country code.                                                         | 840                                                                                                     |
| `merchant_category_code`                                                                                | *str*                                                                                                   | :heavy_check_mark:                                                                                      | Merchant category code to use when calling 3DS through this scheme.                                     | 1234                                                                                                    |
| `merchant_url`                                                                                          | *str*                                                                                                   | :heavy_check_mark:                                                                                      | URL to send when calling 3DS through this scheme.                                                       | https://example.com                                                                                     |
| `scheme`                                                                                                | [models.CardScheme](../../models/cardscheme.md)                                                         | :heavy_check_mark:                                                                                      | N/A                                                                                                     | visa                                                                                                    |
| `metadata`                                                                                              | Dict[str, *str*]                                                                                        | :heavy_check_mark:                                                                                      | Any additional information about the 3DS configuration that you would like to store as key-value pairs. |                                                                                                         |
| `currency`                                                                                              | *OptionalNullable[str]*                                                                                 | :heavy_minus_sign:                                                                                      | ISO 4217 currency code (3 characters). If left null, the configuration will apply to all currencies.    | USD                                                                                                     |
| `retries`                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                        | :heavy_minus_sign:                                                                                      | Configuration to override the default retry behavior of the client.                                     |                                                                                                         |

### Response

**[models.MerchantAccountThreeDSConfiguration](../../models/merchantaccountthreedsconfiguration.md)**

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

## list

List all 3DS configurations for a merchant account.

### Example Usage

<!-- UsageSnippet language="python" operationID="list_three_ds_configurations" method="get" path="/merchant-accounts/{merchant_account_id}/three-ds-configurations" -->
```python
from gr4vy import Gr4vy
import os


with Gr4vy(
    bearer_auth=os.getenv("GR4VY_BEARER_AUTH", ""),
) as g_client:

    res = g_client.merchant_accounts.three_ds_configuration.list(merchant_account_id="merchant-12345")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `merchant_account_id`                                               | *str*                                                               | :heavy_check_mark:                                                  | The ID of the merchant account.                                     | merchant-12345                                                      |
| `currency`                                                          | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | ISO 4217 currency code (3 characters) to filter 3DS configurations. | USD                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.MerchantAccountThreeDSConfigurations](../../models/merchantaccountthreedsconfigurations.md)**

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

Update the 3DS configuration for a merchant account.

### Example Usage

<!-- UsageSnippet language="python" operationID="edit_three_ds_configuration" method="put" path="/merchant-accounts/{merchant_account_id}/three-ds-configurations/{three_ds_configuration_id}" -->
```python
from gr4vy import Gr4vy
import os


with Gr4vy(
    bearer_auth=os.getenv("GR4VY_BEARER_AUTH", ""),
) as g_client:

    res = g_client.merchant_accounts.three_ds_configuration.update(merchant_account_id="merchant-12345", three_ds_configuration_id="1808f5e6-b49c-4db9-94fa-22371ea352f5")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                               | Type                                                                                                    | Required                                                                                                | Description                                                                                             | Example                                                                                                 |
| ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| `merchant_account_id`                                                                                   | *str*                                                                                                   | :heavy_check_mark:                                                                                      | The ID of the merchant account.                                                                         | merchant-12345                                                                                          |
| `three_ds_configuration_id`                                                                             | *str*                                                                                                   | :heavy_check_mark:                                                                                      | The ID of the 3DS configuration for a merchant account.                                                 | 1808f5e6-b49c-4db9-94fa-22371ea352f5                                                                    |
| `merchant_acquirer_bin`                                                                                 | *OptionalNullable[str]*                                                                                 | :heavy_minus_sign:                                                                                      | Acquirer BIN to use when calling 3DS through this scheme.                                               | 516327                                                                                                  |
| `merchant_acquirer_id`                                                                                  | *OptionalNullable[str]*                                                                                 | :heavy_minus_sign:                                                                                      | Merchant ID to use when calling 3DS through this scheme.                                                | 123456789012345                                                                                         |
| `merchant_name`                                                                                         | *OptionalNullable[str]*                                                                                 | :heavy_minus_sign:                                                                                      | N/A                                                                                                     | Acme Inc.                                                                                               |
| `merchant_country_code`                                                                                 | *OptionalNullable[str]*                                                                                 | :heavy_minus_sign:                                                                                      | The merchant's ISO 3166-1 numeric country code.                                                         | 840                                                                                                     |
| `merchant_category_code`                                                                                | *OptionalNullable[str]*                                                                                 | :heavy_minus_sign:                                                                                      | Merchant category code to use when calling 3DS through this scheme.                                     | 1234                                                                                                    |
| `merchant_url`                                                                                          | *OptionalNullable[str]*                                                                                 | :heavy_minus_sign:                                                                                      | URL to send when calling 3DS through this scheme.                                                       | https://example.com                                                                                     |
| `scheme`                                                                                                | [OptionalNullable[models.CardScheme]](../../models/cardscheme.md)                                       | :heavy_minus_sign:                                                                                      | The card scheme for this 3DS configuration                                                              | visa                                                                                                    |
| `currency`                                                                                              | *OptionalNullable[str]*                                                                                 | :heavy_minus_sign:                                                                                      | ISO 4217 currency code (3 characters). If left null, the configuration will apply to all currencies.    | USD                                                                                                     |
| `metadata`                                                                                              | Dict[str, *str*]                                                                                        | :heavy_minus_sign:                                                                                      | Any additional information about the 3DS configuration that you would like to store as key-value pairs. |                                                                                                         |
| `retries`                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                        | :heavy_minus_sign:                                                                                      | Configuration to override the default retry behavior of the client.                                     |                                                                                                         |

### Response

**[models.MerchantAccountThreeDSConfiguration](../../models/merchantaccountthreedsconfiguration.md)**

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

Delete a 3DS configuration for a merchant account.

### Example Usage

<!-- UsageSnippet language="python" operationID="delete_three_ds_configuration" method="delete" path="/merchant-accounts/{merchant_account_id}/three-ds-configurations/{three_ds_configuration_id}" -->
```python
from gr4vy import Gr4vy
import os


with Gr4vy(
    bearer_auth=os.getenv("GR4VY_BEARER_AUTH", ""),
) as g_client:

    g_client.merchant_accounts.three_ds_configuration.delete(merchant_account_id="merchant-12345", three_ds_configuration_id="1808f5e6-b49c-4db9-94fa-22371ea352f5")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `merchant_account_id`                                               | *str*                                                               | :heavy_check_mark:                                                  | The ID of the merchant account.                                     | merchant-12345                                                      |
| `three_ds_configuration_id`                                         | *str*                                                               | :heavy_check_mark:                                                  | The ID of the 3DS configuration for a merchant account.             | 1808f5e6-b49c-4db9-94fa-22371ea352f5                                |
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