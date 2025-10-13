# PaymentLinksSDK
(*payment_links*)

## Overview

### Available Operations

* [create](#create) - Add a payment link
* [list](#list) - List all payment links
* [expire](#expire) - Expire a payment link
* [get](#get) - Get payment link

## create

Create a new payment link.

### Example Usage

<!-- UsageSnippet language="python" operationID="add_payment_link" method="post" path="/payment-links" -->
```python
from gr4vy import Gr4vy
import os


with Gr4vy(
    merchant_account_id="default",
    bearer_auth=os.getenv("GR4VY_BEARER_AUTH", ""),
) as g_client:

    res = g_client.payment_links.create(amount=1299, country="DE", currency="EUR")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                             | Type                                                                                                  | Required                                                                                              | Description                                                                                           | Example                                                                                               |
| ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| `amount`                                                                                              | *int*                                                                                                 | :heavy_check_mark:                                                                                    | The amount for the payment link.                                                                      | 1299                                                                                                  |
| `country`                                                                                             | *str*                                                                                                 | :heavy_check_mark:                                                                                    | The country code for the payment link.                                                                | DE                                                                                                    |
| `currency`                                                                                            | *str*                                                                                                 | :heavy_check_mark:                                                                                    | The currency code for the payment link.                                                               | EUR                                                                                                   |
| `merchant_account_id`                                                                                 | *Optional[str]*                                                                                       | :heavy_minus_sign:                                                                                    | The ID of the merchant account to use for this request.                                               | default                                                                                               |
| `buyer`                                                                                               | [OptionalNullable[models.GuestBuyerInput]](../../models/guestbuyerinput.md)                           | :heavy_minus_sign:                                                                                    | The guest buyer for the payment link.                                                                 |                                                                                                       |
| `expires_at`                                                                                          | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                  | :heavy_minus_sign:                                                                                    | The expiration date and time for the payment link.                                                    | 2024-06-01T00:00:00.000Z                                                                              |
| `connection_options`                                                                                  | [OptionalNullable[models.TransactionConnectionOptions]](../../models/transactionconnectionoptions.md) | :heavy_minus_sign:                                                                                    | Connection options for the payment link.                                                              |                                                                                                       |
| `external_identifier`                                                                                 | *OptionalNullable[str]*                                                                               | :heavy_minus_sign:                                                                                    | The merchant reference for the payment link.                                                          | external-12345                                                                                        |
| `statement_descriptor`                                                                                | [OptionalNullable[models.StatementDescriptor]](../../models/statementdescriptor.md)                   | :heavy_minus_sign:                                                                                    | The statement descriptor for the payment link.                                                        |                                                                                                       |
| `locale`                                                                                              | *OptionalNullable[str]*                                                                               | :heavy_minus_sign:                                                                                    | The locale for the payment link.                                                                      | en                                                                                                    |
| `merchant_name`                                                                                       | *OptionalNullable[str]*                                                                               | :heavy_minus_sign:                                                                                    | The merchant's display name.                                                                          | ACME Inc.                                                                                             |
| `merchant_url`                                                                                        | *OptionalNullable[str]*                                                                               | :heavy_minus_sign:                                                                                    | The merchant's website URL.                                                                           | https://merchant.example.com                                                                          |
| `merchant_banner_url`                                                                                 | *OptionalNullable[str]*                                                                               | :heavy_minus_sign:                                                                                    | The merchant's banner image URL.                                                                      | https://merchant.example.com/banner.png                                                               |
| `merchant_color`                                                                                      | *OptionalNullable[str]*                                                                               | :heavy_minus_sign:                                                                                    | The merchant's brand color.                                                                           | #FF5733                                                                                               |
| `merchant_message`                                                                                    | *OptionalNullable[str]*                                                                               | :heavy_minus_sign:                                                                                    | A message from the merchant.                                                                          | Thank you for your purchase!                                                                          |
| `merchant_terms_and_conditions_url`                                                                   | *OptionalNullable[str]*                                                                               | :heavy_minus_sign:                                                                                    | URL to the merchant's terms and conditions.                                                           | https://merchant.example.com/terms                                                                    |
| `merchant_favicon_url`                                                                                | *OptionalNullable[str]*                                                                               | :heavy_minus_sign:                                                                                    | URL to the merchant's favicon.                                                                        | https://merchant.example.com/favicon.ico                                                              |
| `intent`                                                                                              | [Optional[models.TransactionIntent]](../../models/transactionintent.md)                               | :heavy_minus_sign:                                                                                    | N/A                                                                                                   |                                                                                                       |
| `return_url`                                                                                          | *OptionalNullable[str]*                                                                               | :heavy_minus_sign:                                                                                    | The return URL after payment completion.                                                              | https://merchant.example.com/return                                                                   |
| `cart_items`                                                                                          | List[[models.CartItem](../../models/cartitem.md)]                                                     | :heavy_minus_sign:                                                                                    | The cart items for the payment link.                                                                  |                                                                                                       |
| `metadata`                                                                                            | Dict[str, *Any*]                                                                                      | :heavy_minus_sign:                                                                                    | Arbitrary metadata for the payment link.                                                              | {<br/>"order_id": "ORD-12345"<br/>}                                                                   |
| `payment_source`                                                                                      | [Optional[models.TransactionPaymentSource]](../../models/transactionpaymentsource.md)                 | :heavy_minus_sign:                                                                                    | The way payment method information made it to this transaction.                                       |                                                                                                       |
| `retries`                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                      | :heavy_minus_sign:                                                                                    | Configuration to override the default retry behavior of the client.                                   |                                                                                                       |

### Response

**[models.PaymentLink](../../models/paymentlink.md)**

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

List all created payment links.

### Example Usage

<!-- UsageSnippet language="python" operationID="list_payment_links" method="get" path="/payment-links" -->
```python
from gr4vy import Gr4vy
import os


with Gr4vy(
    merchant_account_id="default",
    bearer_auth=os.getenv("GR4VY_BEARER_AUTH", ""),
) as g_client:

    res = g_client.payment_links.list(limit=20)

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                                                                                       | Type                                                                                                                            | Required                                                                                                                        | Description                                                                                                                     | Example                                                                                                                         |
| ------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| `cursor`                                                                                                                        | *OptionalNullable[str]*                                                                                                         | :heavy_minus_sign:                                                                                                              | A pointer to the page of results to return.                                                                                     | ZXhhbXBsZTE                                                                                                                     |
| `limit`                                                                                                                         | *Optional[int]*                                                                                                                 | :heavy_minus_sign:                                                                                                              | The maximum number of items that are returned.                                                                                  | 20                                                                                                                              |
| `buyer_search`                                                                                                                  | List[*str*]                                                                                                                     | :heavy_minus_sign:                                                                                                              | Filters the results to only get the items for which some of the buyer data contains exactly the provided `buyer_search` values. | [<br/>"John",<br/>"London"<br/>]                                                                                                |
| `merchant_account_id`                                                                                                           | *Optional[str]*                                                                                                                 | :heavy_minus_sign:                                                                                                              | The ID of the merchant account to use for this request.                                                                         | default                                                                                                                         |
| `retries`                                                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                | :heavy_minus_sign:                                                                                                              | Configuration to override the default retry behavior of the client.                                                             |                                                                                                                                 |

### Response

**[models.ListPaymentLinksResponse](../../models/listpaymentlinksresponse.md)**

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

## expire

Expire an existing payment link.

### Example Usage

<!-- UsageSnippet language="python" operationID="expire_payment_link" method="post" path="/payment-links/{payment_link_id}/expire" -->
```python
from gr4vy import Gr4vy
import os


with Gr4vy(
    merchant_account_id="default",
    bearer_auth=os.getenv("GR4VY_BEARER_AUTH", ""),
) as g_client:

    g_client.payment_links.expire(payment_link_id="a1b2c3d4-5678-90ab-cdef-1234567890ab")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `payment_link_id`                                                   | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier for the payment link.                         | a1b2c3d4-5678-90ab-cdef-1234567890ab                                |
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

## get

Fetch the details for a payment link.

### Example Usage

<!-- UsageSnippet language="python" operationID="get_payment_link" method="get" path="/payment-links/{payment_link_id}" -->
```python
from gr4vy import Gr4vy
import os


with Gr4vy(
    merchant_account_id="default",
    bearer_auth=os.getenv("GR4VY_BEARER_AUTH", ""),
) as g_client:

    res = g_client.payment_links.get(payment_link_id="a1b2c3d4-5678-90ab-cdef-1234567890ab")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `payment_link_id`                                                   | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier for the payment link.                         | a1b2c3d4-5678-90ab-cdef-1234567890ab                                |
| `merchant_account_id`                                               | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | The ID of the merchant account to use for this request.             | default                                                             |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.PaymentLink](../../models/paymentlink.md)**

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