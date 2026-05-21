# DigitalWallets.Sessions

## Overview

### Available Operations

* [google_pay](#google_pay) - Create a Google Pay session
* [apple_pay](#apple_pay) - Create a Apple Pay session
* [paze](#paze) - Create a Paze session
* [paze_mobile_session_review](#paze_mobile_session_review) - Review a Paze session
* [click_to_pay](#click_to_pay) - Create a Click to Pay session

## google_pay

Create a session for use with Google Pay.

### Example Usage

<!-- UsageSnippet language="python" operationID="create_google_pay_digital_wallet_session" method="post" path="/digital-wallets/google/session" -->
```python
from gr4vy import Gr4vy
import os


with Gr4vy(
    merchant_account_id="default",
    bearer_auth=os.getenv("GR4VY_BEARER_AUTH", ""),
) as g_client:

    res = g_client.digital_wallets.sessions.google_pay(origin_domain="example.com")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `origin_domain`                                                     | *str*                                                               | :heavy_check_mark:                                                  | The domain on which Google Pay is being loaded.                     | example.com                                                         |
| `merchant_account_id`                                               | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | The ID of the merchant account to use for this request.             | default                                                             |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.GooglePaySession](../../models/googlepaysession.md)**

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

## apple_pay

Create a session for use with Apple Pay.

### Example Usage

<!-- UsageSnippet language="python" operationID="create_apple_pay_digital_wallet_session" method="post" path="/digital-wallets/apple/session" -->
```python
from gr4vy import Gr4vy
import os


with Gr4vy(
    merchant_account_id="default",
    bearer_auth=os.getenv("GR4VY_BEARER_AUTH", ""),
) as g_client:

    res = g_client.digital_wallets.sessions.apple_pay(validation_url="https://apple-pay-gateway-cert.apple.com", domain_name="example.com")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                | Example                                                                    |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `validation_url`                                                           | *str*                                                                      | :heavy_check_mark:                                                         | The validation URL as provided by the Apple SDK when processing a payment. | https://apple-pay-gateway-cert.apple.com                                   |
| `domain_name`                                                              | *str*                                                                      | :heavy_check_mark:                                                         | The domain on which Apple Pay is being loaded.                             | example.com                                                                |
| `merchant_account_id`                                                      | *Optional[str]*                                                            | :heavy_minus_sign:                                                         | The ID of the merchant account to use for this request.                    | default                                                                    |
| `retries`                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)           | :heavy_minus_sign:                                                         | Configuration to override the default retry behavior of the client.        |                                                                            |

### Response

**[Dict[str, Any]](../../models/.md)**

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

## paze

Create a session for use with Paze.

### Example Usage

<!-- UsageSnippet language="python" operationID="create_paze_digital_wallet_session" method="post" path="/digital-wallets/paze/session" -->
```python
from gr4vy import Gr4vy
import os


with Gr4vy(
    merchant_account_id="default",
    bearer_auth=os.getenv("GR4VY_BEARER_AUTH", ""),
) as g_client:

    res = g_client.digital_wallets.sessions.paze(source="web")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                   | Type                                                                        | Required                                                                    | Description                                                                 | Example                                                                     |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `merchant_account_id`                                                       | *Optional[str]*                                                             | :heavy_minus_sign:                                                          | The ID of the merchant account to use for this request.                     | default                                                                     |
| `source`                                                                    | [Optional[models.Source]](../../models/source.md)                           | :heavy_minus_sign:                                                          | The platform that the Paze session is being created for. Defaults to `web`. | web                                                                         |
| `domain_name`                                                               | *OptionalNullable[str]*                                                     | :heavy_minus_sign:                                                          | The domain on which Paze is being loaded. Required when `source` is `web`.  | example.com                                                                 |
| `retries`                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)            | :heavy_minus_sign:                                                          | Configuration to override the default retry behavior of the client.         |                                                                             |

### Response

**[models.ResponseCreatePazeDigitalWalletSession](../../models/responsecreatepazedigitalwalletsession.md)**

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

## paze_mobile_session_review

Review a Paze checkout session and retrieve the selected card, consumer, and shipping address details.

### Example Usage

<!-- UsageSnippet language="python" operationID="review_paze_mobile_session" method="post" path="/digital-wallets/paze/session/review" -->
```python
from gr4vy import Gr4vy
import os


with Gr4vy(
    merchant_account_id="default",
    bearer_auth=os.getenv("GR4VY_BEARER_AUTH", ""),
) as g_client:

    res = g_client.digital_wallets.sessions.paze_mobile_session_review(session_id="7c1cba03-d20e-4a3f-9d77-e5dc23a39ac2", code="eyJhdWQiOm51bGwsImtpZCI6IjE3...", access_token="eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9...")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                             | Type                                                                                                                                                  | Required                                                                                                                                              | Description                                                                                                                                           | Example                                                                                                                                               |
| ----------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| `session_id`                                                                                                                                          | *str*                                                                                                                                                 | :heavy_check_mark:                                                                                                                                    | Session reference identifier generated by the merchant. Must match the value sent in the Paze session create call.                                    | 7c1cba03-d20e-4a3f-9d77-e5dc23a39ac2                                                                                                                  |
| `code`                                                                                                                                                | *str*                                                                                                                                                 | :heavy_check_mark:                                                                                                                                    | Opaque token issued by the Paze service in the response from the most recent Paze UX interaction (checkout, change card, or change shipping address). | eyJhdWQiOm51bGwsImtpZCI6IjE3...                                                                                                                       |
| `access_token`                                                                                                                                        | *str*                                                                                                                                                 | :heavy_check_mark:                                                                                                                                    | The Paze OAuth access token returned by the Paze mobile session create call. Used to authenticate the request to Paze.                                | eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9...                                                                                                               |
| `merchant_account_id`                                                                                                                                 | *Optional[str]*                                                                                                                                       | :heavy_minus_sign:                                                                                                                                    | The ID of the merchant account to use for this request.                                                                                               | default                                                                                                                                               |
| `retries`                                                                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                      | :heavy_minus_sign:                                                                                                                                    | Configuration to override the default retry behavior of the client.                                                                                   |                                                                                                                                                       |

### Response

**[models.PazeSessionReview](../../models/pazesessionreview.md)**

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

## click_to_pay

Create a session for use with Click to Pay.

### Example Usage

<!-- UsageSnippet language="python" operationID="create_click_to_pay_digital_wallet_session" method="post" path="/digital-wallets/click-to-pay/session" -->
```python
from gr4vy import Gr4vy
import os


with Gr4vy(
    bearer_auth=os.getenv("GR4VY_BEARER_AUTH", ""),
) as g_client:

    res = g_client.digital_wallets.sessions.click_to_pay(checkout_session_id="4137b1cf-39ac-42a8-bad6-1c680d5dab6b")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `checkout_session_id`                                               | *str*                                                               | :heavy_check_mark:                                                  | The checkout session ID to create a Click to Pay session for.       | 4137b1cf-39ac-42a8-bad6-1c680d5dab6b                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.ClickToPaySession](../../models/clicktopaysession.md)**

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