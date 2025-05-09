# PaymentMethods
(*payment_methods*)

## Overview

### Available Operations

* [list](#list) - List all payment methods
* [create](#create) - Create payment method
* [get](#get) - Get payment method
* [delete](#delete) - Delete payment method

## list

List all stored payment method.

### Example Usage

```python
from gr4vy import Gr4vy, auth
import os


with Gr4vy(
    bearer_auth=os.getenv("GR4VY_BEARER_AUTH", ""),
    merchant_account_id="default",
) as g_client:

    res = g_client.payment_methods.list(cursor="ZXhhbXBsZTE", buyer_id="fe26475d-ec3e-4884-9553-f7356683f7f9", buyer_external_identifier="buyer-12345", external_identifier="payment-method-12345", merchant_account_id="default")

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                               | Type                                                                    | Required                                                                | Description                                                             | Example                                                                 |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `cursor`                                                                | *OptionalNullable[str]*                                                 | :heavy_minus_sign:                                                      | A pointer to the page of results to return.                             | ZXhhbXBsZTE                                                             |
| `limit`                                                                 | *Optional[int]*                                                         | :heavy_minus_sign:                                                      | The maximum number of items that are at returned.                       | 20                                                                      |
| `buyer_id`                                                              | *OptionalNullable[str]*                                                 | :heavy_minus_sign:                                                      | The ID of the buyer to filter payment methods by.                       | fe26475d-ec3e-4884-9553-f7356683f7f9                                    |
| `buyer_external_identifier`                                             | *OptionalNullable[str]*                                                 | :heavy_minus_sign:                                                      | The external identifier of the buyer to filter payment methods by.      | buyer-12345                                                             |
| `status`                                                                | List[[models.PaymentMethodStatus](../../models/paymentmethodstatus.md)] | :heavy_minus_sign:                                                      | N/A                                                                     |                                                                         |
| `external_identifier`                                                   | *OptionalNullable[str]*                                                 | :heavy_minus_sign:                                                      | The external identifier of the payment method to filter by.             | payment-method-12345                                                    |
| `merchant_account_id`                                                   | *Optional[str]*                                                         | :heavy_minus_sign:                                                      | The ID of the merchant account to use for this request.                 | default                                                                 |
| `retries`                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)        | :heavy_minus_sign:                                                      | Configuration to override the default retry behavior of the client.     |                                                                         |

### Response

**[models.ListPaymentMethodsResponse](../../models/listpaymentmethodsresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.Error400            | 400                        | application/json           |
| errors.Error401            | 401                        | application/json           |
| errors.Error403            | 403                        | application/json           |
| errors.Error403Forbidden   | 403                        | application/json           |
| errors.Error403Active      | 403                        | application/json           |
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

Store a new payment method.

### Example Usage

```python
from gr4vy import Gr4vy, auth
import os


with Gr4vy(
    bearer_auth=os.getenv("GR4VY_BEARER_AUTH", ""),
    merchant_account_id="default",
) as g_client:

    res = g_client.payment_methods.create(request_body={
        "method": "paypal",
        "buyer_id": "fe26475d-ec3e-4884-9553-f7356683f7f9",
        "buyer_external_identifier": "buyer-12345",
        "country": "GB",
        "currency": "GBP",
        "redirect_url": "https://standard-utilization.com/",
        "external_identifier": "payment-method-12345",
    }, merchant_account_id="default")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                 | Type                                                                      | Required                                                                  | Description                                                               | Example                                                                   |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `request_body`                                                            | [models.CreatePaymentMethodBody](../../models/createpaymentmethodbody.md) | :heavy_check_mark:                                                        | N/A                                                                       |                                                                           |
| `timeout_in_seconds`                                                      | *Optional[float]*                                                         | :heavy_minus_sign:                                                        | N/A                                                                       |                                                                           |
| `merchant_account_id`                                                     | *Optional[str]*                                                           | :heavy_minus_sign:                                                        | The ID of the merchant account to use for this request.                   | default                                                                   |
| `retries`                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)          | :heavy_minus_sign:                                                        | Configuration to override the default retry behavior of the client.       |                                                                           |

### Response

**[models.PaymentMethod](../../models/paymentmethod.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.Error400            | 400                        | application/json           |
| errors.Error401            | 401                        | application/json           |
| errors.Error403            | 403                        | application/json           |
| errors.Error403Forbidden   | 403                        | application/json           |
| errors.Error403Active      | 403                        | application/json           |
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

Retrieve a payment method.

### Example Usage

```python
from gr4vy import Gr4vy, auth
import os


with Gr4vy(
    bearer_auth=os.getenv("GR4VY_BEARER_AUTH", ""),
    merchant_account_id="default",
) as g_client:

    res = g_client.payment_methods.get(payment_method_id="ef9496d8-53a5-4aad-8ca2-00eb68334389", merchant_account_id="default")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `payment_method_id`                                                 | *str*                                                               | :heavy_check_mark:                                                  | The ID of the payment method                                        | ef9496d8-53a5-4aad-8ca2-00eb68334389                                |
| `merchant_account_id`                                               | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | The ID of the merchant account to use for this request.             | default                                                             |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.PaymentMethod](../../models/paymentmethod.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.Error400            | 400                        | application/json           |
| errors.Error401            | 401                        | application/json           |
| errors.Error403            | 403                        | application/json           |
| errors.Error403Forbidden   | 403                        | application/json           |
| errors.Error403Active      | 403                        | application/json           |
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

Delete a payment method.

### Example Usage

```python
from gr4vy import Gr4vy, auth
import os


with Gr4vy(
    bearer_auth=os.getenv("GR4VY_BEARER_AUTH", ""),
    merchant_account_id="default",
) as g_client:

    g_client.payment_methods.delete(payment_method_id="ef9496d8-53a5-4aad-8ca2-00eb68334389", merchant_account_id="default")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `payment_method_id`                                                 | *str*                                                               | :heavy_check_mark:                                                  | The ID of the payment method                                        | ef9496d8-53a5-4aad-8ca2-00eb68334389                                |
| `merchant_account_id`                                               | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | The ID of the merchant account to use for this request.             | default                                                             |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.Error400            | 400                        | application/json           |
| errors.Error401            | 401                        | application/json           |
| errors.Error403            | 403                        | application/json           |
| errors.Error403Forbidden   | 403                        | application/json           |
| errors.Error403Active      | 403                        | application/json           |
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