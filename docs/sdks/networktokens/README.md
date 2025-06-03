# NetworkTokens
(*payment_methods.network_tokens*)

## Overview

### Available Operations

* [list](#list) - List network tokens
* [create](#create) - Provision network token
* [suspend](#suspend) - Suspend network token
* [resume](#resume) - Resume network token
* [delete](#delete) - Delete network token

## list

List all network tokens stored for a payment method.

### Example Usage

```python
from gr4vy import Gr4vy
import os


with Gr4vy(
    bearer_auth=os.getenv("GR4VY_BEARER_AUTH", ""),
    merchant_account_id="default",
) as g_client:

    res = g_client.payment_methods.network_tokens.list(payment_method_id="ef9496d8-53a5-4aad-8ca2-00eb68334389", merchant_account_id="default")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `payment_method_id`                                                 | *str*                                                               | :heavy_check_mark:                                                  | The ID of the payment method                                        | ef9496d8-53a5-4aad-8ca2-00eb68334389                                |
| `application_name`                                                  | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |                                                                     |
| `merchant_account_id`                                               | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | The ID of the merchant account to use for this request.             | default                                                             |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.CollectionNoCursorNetworkToken](../../models/collectionnocursornetworktoken.md)**

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

Provision a network token for a payment method.

### Example Usage

```python
from gr4vy import Gr4vy
import os


with Gr4vy(
    bearer_auth=os.getenv("GR4VY_BEARER_AUTH", ""),
    merchant_account_id="default",
) as g_client:

    res = g_client.payment_methods.network_tokens.create(payment_method_id="ef9496d8-53a5-4aad-8ca2-00eb68334389", merchant_initiated=False, is_subsequent_payment=False, merchant_account_id="default", security_code="123")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                         | Type                                                                                              | Required                                                                                          | Description                                                                                       | Example                                                                                           |
| ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| `payment_method_id`                                                                               | *str*                                                                                             | :heavy_check_mark:                                                                                | The ID of the payment method                                                                      | ef9496d8-53a5-4aad-8ca2-00eb68334389                                                              |
| `merchant_initiated`                                                                              | *bool*                                                                                            | :heavy_check_mark:                                                                                | Defines if the request is merchant initiated or not.                                              | false                                                                                             |
| `is_subsequent_payment`                                                                           | *bool*                                                                                            | :heavy_check_mark:                                                                                | Defines if the request is a subsequent of another request or not.                                 | false                                                                                             |
| `application_name`                                                                                | *Optional[str]*                                                                                   | :heavy_minus_sign:                                                                                | N/A                                                                                               |                                                                                                   |
| `merchant_account_id`                                                                             | *Optional[str]*                                                                                   | :heavy_minus_sign:                                                                                | The ID of the merchant account to use for this request.                                           | default                                                                                           |
| `security_code`                                                                                   | *OptionalNullable[str]*                                                                           | :heavy_minus_sign:                                                                                | The 3 or 4 digit security code often found on the card. This often referred to as the CVV or CVD. | 123                                                                                               |
| `retries`                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                  | :heavy_minus_sign:                                                                                | Configuration to override the default retry behavior of the client.                               |                                                                                                   |

### Response

**[models.NetworkToken](../../models/networktoken.md)**

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

## suspend

Suspend a network token for a payment method.

### Example Usage

```python
from gr4vy import Gr4vy
import os


with Gr4vy(
    bearer_auth=os.getenv("GR4VY_BEARER_AUTH", ""),
    merchant_account_id="default",
) as g_client:

    res = g_client.payment_methods.network_tokens.suspend(payment_method_id="ef9496d8-53a5-4aad-8ca2-00eb68334389", network_token_id="f8dd5cfc-7834-4847-95dc-f75a360e2298", merchant_account_id="default")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `payment_method_id`                                                 | *str*                                                               | :heavy_check_mark:                                                  | The ID of the payment method                                        | ef9496d8-53a5-4aad-8ca2-00eb68334389                                |
| `network_token_id`                                                  | *str*                                                               | :heavy_check_mark:                                                  | The ID of the network token                                         | f8dd5cfc-7834-4847-95dc-f75a360e2298                                |
| `application_name`                                                  | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |                                                                     |
| `merchant_account_id`                                               | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | The ID of the merchant account to use for this request.             | default                                                             |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.NetworkToken](../../models/networktoken.md)**

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

## resume

Resume a suspended network token for a payment method.

### Example Usage

```python
from gr4vy import Gr4vy
import os


with Gr4vy(
    bearer_auth=os.getenv("GR4VY_BEARER_AUTH", ""),
    merchant_account_id="default",
) as g_client:

    res = g_client.payment_methods.network_tokens.resume(payment_method_id="ef9496d8-53a5-4aad-8ca2-00eb68334389", network_token_id="f8dd5cfc-7834-4847-95dc-f75a360e2298", merchant_account_id="default")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `payment_method_id`                                                 | *str*                                                               | :heavy_check_mark:                                                  | The ID of the payment method                                        | ef9496d8-53a5-4aad-8ca2-00eb68334389                                |
| `network_token_id`                                                  | *str*                                                               | :heavy_check_mark:                                                  | The ID of the network token                                         | f8dd5cfc-7834-4847-95dc-f75a360e2298                                |
| `application_name`                                                  | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |                                                                     |
| `merchant_account_id`                                               | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | The ID of the merchant account to use for this request.             | default                                                             |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.NetworkToken](../../models/networktoken.md)**

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

Delete a network token for a payment method.

### Example Usage

```python
from gr4vy import Gr4vy
import os


with Gr4vy(
    bearer_auth=os.getenv("GR4VY_BEARER_AUTH", ""),
    merchant_account_id="default",
) as g_client:

    g_client.payment_methods.network_tokens.delete(payment_method_id="ef9496d8-53a5-4aad-8ca2-00eb68334389", network_token_id="f8dd5cfc-7834-4847-95dc-f75a360e2298", merchant_account_id="default")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `payment_method_id`                                                 | *str*                                                               | :heavy_check_mark:                                                  | The ID of the payment method                                        | ef9496d8-53a5-4aad-8ca2-00eb68334389                                |
| `network_token_id`                                                  | *str*                                                               | :heavy_check_mark:                                                  | The ID of the network token                                         | f8dd5cfc-7834-4847-95dc-f75a360e2298                                |
| `application_name`                                                  | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |                                                                     |
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