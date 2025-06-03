# CheckoutSessions
(*checkout_sessions*)

## Overview

### Available Operations

* [create](#create) - Create checkout session
* [update](#update) - Update checkout session
* [get](#get) - Get checkout session
* [delete](#delete) - Delete checkout session

## create

Create a new checkout session.

### Example Usage

```python
from gr4vy import Gr4vy
import os


with Gr4vy(
    bearer_auth=os.getenv("GR4VY_BEARER_AUTH", ""),
) as g_client:

    res = g_client.checkout_sessions.create()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                       | Type                                                                            | Required                                                                        | Description                                                                     | Example                                                                         |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| `merchant_account_id`                                                           | *Optional[str]*                                                                 | :heavy_minus_sign:                                                              | The ID of the merchant account to use for this request.                         | default                                                                         |
| `checkout_session_create`                                                       | [Optional[models.CheckoutSessionCreate]](../../models/checkoutsessioncreate.md) | :heavy_minus_sign:                                                              | N/A                                                                             |                                                                                 |
| `retries`                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                | :heavy_minus_sign:                                                              | Configuration to override the default retry behavior of the client.             |                                                                                 |

### Response

**[models.CheckoutSession](../../models/checkoutsession.md)**

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

Update the information stored on a checkout session.

### Example Usage

```python
from gr4vy import Gr4vy
import os


with Gr4vy(
    bearer_auth=os.getenv("GR4VY_BEARER_AUTH", ""),
) as g_client:

    res = g_client.checkout_sessions.update(session_id="4137b1cf-39ac-42a8-bad6-1c680d5dab6b")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                           | Type                                                                                                                                                                | Required                                                                                                                                                            | Description                                                                                                                                                         | Example                                                                                                                                                             |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `session_id`                                                                                                                                                        | *str*                                                                                                                                                               | :heavy_check_mark:                                                                                                                                                  | The ID of the checkout session.                                                                                                                                     | 4137b1cf-39ac-42a8-bad6-1c680d5dab6b                                                                                                                                |
| `merchant_account_id`                                                                                                                                               | *Optional[str]*                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                  | The ID of the merchant account to use for this request.                                                                                                             | default                                                                                                                                                             |
| `cart_items`                                                                                                                                                        | List[[models.CartItem](../../models/cartitem.md)]                                                                                                                   | :heavy_minus_sign:                                                                                                                                                  | An array of cart items that represents the line items of a transaction.                                                                                             |                                                                                                                                                                     |
| `metadata`                                                                                                                                                          | Dict[str, *str*]                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                  | Any additional information about the transaction that you would like to store as key-value pairs. This data is passed to payment service providers that support it. | {<br/>"cohort": "cohort-a",<br/>"order_id": "order-12345"<br/>}                                                                                                     |
| `buyer`                                                                                                                                                             | [OptionalNullable[models.GuestBuyerInput]](../../models/guestbuyerinput.md)                                                                                         | :heavy_minus_sign:                                                                                                                                                  | Provide buyer details for the transaction. No buyer resource will be created on Gr4vy when used.                                                                    |                                                                                                                                                                     |
| `airline`                                                                                                                                                           | [OptionalNullable[models.Airline]](../../models/airline.md)                                                                                                         | :heavy_minus_sign:                                                                                                                                                  | The airline addendum data which describes the airline booking associated with this transaction.                                                                     |                                                                                                                                                                     |
| `expires_in`                                                                                                                                                        | *Optional[float]*                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                  | N/A                                                                                                                                                                 |                                                                                                                                                                     |
| `retries`                                                                                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                    | :heavy_minus_sign:                                                                                                                                                  | Configuration to override the default retry behavior of the client.                                                                                                 |                                                                                                                                                                     |

### Response

**[models.CheckoutSession](../../models/checkoutsession.md)**

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

Retrieve the information stored on a checkout session.

### Example Usage

```python
from gr4vy import Gr4vy
import os


with Gr4vy(
    bearer_auth=os.getenv("GR4VY_BEARER_AUTH", ""),
) as g_client:

    res = g_client.checkout_sessions.get(session_id="4137b1cf-39ac-42a8-bad6-1c680d5dab6b")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `session_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | The ID of the checkout session.                                     | 4137b1cf-39ac-42a8-bad6-1c680d5dab6b                                |
| `merchant_account_id`                                               | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | The ID of the merchant account to use for this request.             | default                                                             |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.CheckoutSession](../../models/checkoutsession.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error400  | 400              | application/json |
| errors.Error401  | 401              | application/json |
| errors.Error403  | 403              | application/json |
| errors.Error404  | 404              | application/json |
| errors.Error405  | 405              | application/json |
| errors.Error409  | 409              | application/json |
| errors.Error425  | 425              | application/json |
| errors.Error429  | 429              | application/json |
| errors.Error500  | 500              | application/json |
| errors.Error502  | 502              | application/json |
| errors.Error504  | 504              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## delete

Deleta a checkout session and all of its (PCI) data.

### Example Usage

```python
from gr4vy import Gr4vy
import os


with Gr4vy(
    bearer_auth=os.getenv("GR4VY_BEARER_AUTH", ""),
) as g_client:

    g_client.checkout_sessions.delete(session_id="4137b1cf-39ac-42a8-bad6-1c680d5dab6b")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `session_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | The ID of the checkout session.                                     | 4137b1cf-39ac-42a8-bad6-1c680d5dab6b                                |
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