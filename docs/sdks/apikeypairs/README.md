# ApiKeyPairs

## Overview

### Available Operations

* [list](#list) - List all API key pairs
* [create](#create) - Create an API key pair
* [get](#get) - Get an API key pair
* [update](#update) - Update an API key pair
* [delete](#delete) - Delete an API key pair

## list

List all API key pairs.

### Example Usage

<!-- UsageSnippet language="python" operationID="list_api_key_pairs" method="get" path="/api-key-pairs" -->
```python
from gr4vy import Gr4vy
import os


with Gr4vy(
    bearer_auth=os.getenv("GR4VY_BEARER_AUTH", ""),
) as g_client:

    res = g_client.api_key_pairs.list(limit=20)

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `cursor`                                                            | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | A pointer to the page of results to return.                         | ZXhhbXBsZTE                                                         |
| `limit`                                                             | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | The maximum number of items that are returned.                      | 20                                                                  |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.ListAPIKeyPairsResponse](../../models/listapikeypairsresponse.md)**

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

Create a new API key pair.

### Example Usage

<!-- UsageSnippet language="python" operationID="create_api_key_pair" method="post" path="/api-key-pairs" -->
```python
from gr4vy import Gr4vy
import os


with Gr4vy(
    bearer_auth=os.getenv("GR4VY_BEARER_AUTH", ""),
) as g_client:

    res = g_client.api_key_pairs.create(display_name="Production key", role_ids=[
        "8f4b8c1a-1b2c-4d3e-9f5a-6b7c8d9e0f1a",
    ], active=True)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                 | Type                                                                                                                                                                                      | Required                                                                                                                                                                                  | Description                                                                                                                                                                               | Example                                                                                                                                                                                   |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `display_name`                                                                                                                                                                            | *str*                                                                                                                                                                                     | :heavy_check_mark:                                                                                                                                                                        | The display name for the API key pair.                                                                                                                                                    | Production key                                                                                                                                                                            |
| `role_ids`                                                                                                                                                                                | List[*str*]                                                                                                                                                                               | :heavy_check_mark:                                                                                                                                                                        | The ID of the role to assign to the API key pair. Exactly one role is supported. The caller can only assign a role whose scopes are a subset of its own.                                  | [<br/>"8f4b8c1a-1b2c-4d3e-9f5a-6b7c8d9e0f1a"<br/>]                                                                                                                                        |
| `algorithm`                                                                                                                                                                               | [Optional[models.CertificateAlgorithm]](../../models/certificatealgorithm.md)                                                                                                             | :heavy_minus_sign:                                                                                                                                                                        | N/A                                                                                                                                                                                       |                                                                                                                                                                                           |
| `active`                                                                                                                                                                                  | *Optional[bool]*                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                        | Whether the API key pair should be active and usable once created.                                                                                                                        | true                                                                                                                                                                                      |
| `merchant_account_ids`                                                                                                                                                                    | List[*str*]                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                        | The IDs of the merchant accounts to associate with the API key pair. An empty list grants access to all merchant accounts. The caller can only assign merchant accounts it has access to. | [<br/>"merchant-12345"<br/>]                                                                                                                                                              |
| `public_key`                                                                                                                                                                              | *OptionalNullable[str]*                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                        | A PEM-encoded ECDSA P-521 (ES512) public key. Provide this to register your own key pair (bring your own key); If omitted, Gr4vy will generate the key pair and return the private key.   | -----BEGIN PUBLIC KEY-----<br/>MIGbMBAGByqGSM49AgEGBSuBBAAjA4GGAAQB...<br/>-----END PUBLIC KEY-----                                                                                       |
| `retries`                                                                                                                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                        | Configuration to override the default retry behavior of the client.                                                                                                                       |                                                                                                                                                                                           |

### Response

**[models.APIKeyPair](../../models/apikeypair.md)**

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

Fetches an API key pair by its ID.

### Example Usage

<!-- UsageSnippet language="python" operationID="get_api_key_pair" method="get" path="/api-key-pairs/{api_key_pair_id}" -->
```python
from gr4vy import Gr4vy
import os


with Gr4vy(
    bearer_auth=os.getenv("GR4VY_BEARER_AUTH", ""),
) as g_client:

    res = g_client.api_key_pairs.get(api_key_pair_id="fe26475d-ec3e-4884-9553-f7356683f7f9")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `api_key_pair_id`                                                   | *str*                                                               | :heavy_check_mark:                                                  | The ID of the API key pair.                                         | fe26475d-ec3e-4884-9553-f7356683f7f9                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.APIKeyPair](../../models/apikeypair.md)**

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

Updates an API key pair.

### Example Usage

<!-- UsageSnippet language="python" operationID="update_api_key_pair" method="put" path="/api-key-pairs/{api_key_pair_id}" -->
```python
from gr4vy import Gr4vy
import os


with Gr4vy(
    bearer_auth=os.getenv("GR4VY_BEARER_AUTH", ""),
) as g_client:

    res = g_client.api_key_pairs.update(api_key_pair_id="fe26475d-ec3e-4884-9553-f7356683f7f9")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                           | Type                                                                                                                                | Required                                                                                                                            | Description                                                                                                                         | Example                                                                                                                             |
| ----------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| `api_key_pair_id`                                                                                                                   | *str*                                                                                                                               | :heavy_check_mark:                                                                                                                  | The ID of the API key pair.                                                                                                         | fe26475d-ec3e-4884-9553-f7356683f7f9                                                                                                |
| `display_name`                                                                                                                      | *OptionalNullable[str]*                                                                                                             | :heavy_minus_sign:                                                                                                                  | The display name for the API key pair.                                                                                              | Production key                                                                                                                      |
| `active`                                                                                                                            | *OptionalNullable[bool]*                                                                                                            | :heavy_minus_sign:                                                                                                                  | Whether the API key pair is active and can be used to authenticate.                                                                 | true                                                                                                                                |
| `role_ids`                                                                                                                          | List[*str*]                                                                                                                         | :heavy_minus_sign:                                                                                                                  | N/A                                                                                                                                 | [<br/>"8f4b8c1a-1b2c-4d3e-9f5a-6b7c8d9e0f1a"<br/>]                                                                                  |
| `merchant_account_ids`                                                                                                              | List[*str*]                                                                                                                         | :heavy_minus_sign:                                                                                                                  | The IDs of the merchant accounts to associate with the API key pair. The caller can only assign merchant accounts it has access to. | [<br/>"merchant-12345"<br/>]                                                                                                        |
| `retries`                                                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                    | :heavy_minus_sign:                                                                                                                  | Configuration to override the default retry behavior of the client.                                                                 |                                                                                                                                     |

### Response

**[models.APIKeyPair](../../models/apikeypair.md)**

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

Permanently removes an API key pair.

### Example Usage

<!-- UsageSnippet language="python" operationID="delete_api_key_pair" method="delete" path="/api-key-pairs/{api_key_pair_id}" -->
```python
from gr4vy import Gr4vy
import os


with Gr4vy(
    bearer_auth=os.getenv("GR4VY_BEARER_AUTH", ""),
) as g_client:

    g_client.api_key_pairs.delete(api_key_pair_id="fe26475d-ec3e-4884-9553-f7356683f7f9")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `api_key_pair_id`                                                   | *str*                                                               | :heavy_check_mark:                                                  | The ID of the API key pair.                                         | fe26475d-ec3e-4884-9553-f7356683f7f9                                |
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