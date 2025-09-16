# BuyersShippingDetails
(*buyers.shipping_details*)

## Overview

### Available Operations

* [create](#create) - Add buyer shipping details
* [list](#list) - List a buyer's shipping details
* [get](#get) - Get buyer shipping details
* [update](#update) - Update a buyer's shipping details
* [delete](#delete) - Delete a buyer's shipping details

## create

Associate shipping details to a buyer.

### Example Usage

<!-- UsageSnippet language="python" operationID="add_buyer_shipping_details" method="post" path="/buyers/{buyer_id}/shipping-details" -->
```python
from gr4vy import Gr4vy
import os


with Gr4vy(
    merchant_account_id="default",
    bearer_auth=os.getenv("GR4VY_BEARER_AUTH", ""),
) as g_client:

    res = g_client.buyers.shipping_details.create(buyer_id="fe26475d-ec3e-4884-9553-f7356683f7f9")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                       | Type                                                                                            | Required                                                                                        | Description                                                                                     | Example                                                                                         |
| ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| `buyer_id`                                                                                      | *str*                                                                                           | :heavy_check_mark:                                                                              | The ID of the buyer to add shipping details to.                                                 | fe26475d-ec3e-4884-9553-f7356683f7f9                                                            |
| `merchant_account_id`                                                                           | *Optional[str]*                                                                                 | :heavy_minus_sign:                                                                              | The ID of the merchant account to use for this request.                                         | default                                                                                         |
| `first_name`                                                                                    | *OptionalNullable[str]*                                                                         | :heavy_minus_sign:                                                                              | The first name(s) or given name for the buyer.                                                  | John                                                                                            |
| `last_name`                                                                                     | *OptionalNullable[str]*                                                                         | :heavy_minus_sign:                                                                              | The last name, or family name, of the buyer.                                                    | Doe                                                                                             |
| `email_address`                                                                                 | *OptionalNullable[str]*                                                                         | :heavy_minus_sign:                                                                              | The email address for the buyer.                                                                | john@example.com                                                                                |
| `phone_number`                                                                                  | *OptionalNullable[str]*                                                                         | :heavy_minus_sign:                                                                              | The phone number for the buyer which should be formatted according to the E164 number standard. | +1234567890                                                                                     |
| `address`                                                                                       | [OptionalNullable[models.Address]](../../models/address.md)                                     | :heavy_minus_sign:                                                                              | The billing address for the buyer.                                                              |                                                                                                 |
| `retries`                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                | :heavy_minus_sign:                                                                              | Configuration to override the default retry behavior of the client.                             |                                                                                                 |

### Response

**[models.ShippingDetails](../../models/shippingdetails.md)**

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

List all the shipping details associated to a specific buyer.

### Example Usage

<!-- UsageSnippet language="python" operationID="list_buyer_shipping_details" method="get" path="/buyers/{buyer_id}/shipping-details" -->
```python
from gr4vy import Gr4vy
import os


with Gr4vy(
    merchant_account_id="default",
    bearer_auth=os.getenv("GR4VY_BEARER_AUTH", ""),
) as g_client:

    res = g_client.buyers.shipping_details.list(buyer_id="fe26475d-ec3e-4884-9553-f7356683f7f9")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `buyer_id`                                                          | *str*                                                               | :heavy_check_mark:                                                  | The ID of the buyer to retrieve shipping details for.               | fe26475d-ec3e-4884-9553-f7356683f7f9                                |
| `merchant_account_id`                                               | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | The ID of the merchant account to use for this request.             | default                                                             |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.ShippingDetailsList](../../models/shippingdetailslist.md)**

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

Get a buyer's shipping details.

### Example Usage

<!-- UsageSnippet language="python" operationID="get_buyer_shipping_details" method="get" path="/buyers/{buyer_id}/shipping-details/{shipping_details_id}" -->
```python
from gr4vy import Gr4vy
import os


with Gr4vy(
    merchant_account_id="default",
    bearer_auth=os.getenv("GR4VY_BEARER_AUTH", ""),
) as g_client:

    res = g_client.buyers.shipping_details.get(buyer_id="fe26475d-ec3e-4884-9553-f7356683f7f9", shipping_details_id="bf8c36ad-02d9-4904-b0f9-a230b149e341")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `buyer_id`                                                          | *str*                                                               | :heavy_check_mark:                                                  | The ID of the buyer to retrieve shipping details for.               | fe26475d-ec3e-4884-9553-f7356683f7f9                                |
| `shipping_details_id`                                               | *str*                                                               | :heavy_check_mark:                                                  | The ID of the shipping details to retrieve.                         | bf8c36ad-02d9-4904-b0f9-a230b149e341                                |
| `merchant_account_id`                                               | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | The ID of the merchant account to use for this request.             | default                                                             |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.ShippingDetails](../../models/shippingdetails.md)**

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

Update the shipping details associated to a specific buyer.

### Example Usage

<!-- UsageSnippet language="python" operationID="update_buyer_shipping_details" method="put" path="/buyers/{buyer_id}/shipping-details/{shipping_details_id}" -->
```python
from gr4vy import Gr4vy
import os


with Gr4vy(
    merchant_account_id="default",
    bearer_auth=os.getenv("GR4VY_BEARER_AUTH", ""),
) as g_client:

    res = g_client.buyers.shipping_details.update(buyer_id="fe26475d-ec3e-4884-9553-f7356683f7f9", shipping_details_id="bf8c36ad-02d9-4904-b0f9-a230b149e341")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                       | Type                                                                                            | Required                                                                                        | Description                                                                                     | Example                                                                                         |
| ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| `buyer_id`                                                                                      | *str*                                                                                           | :heavy_check_mark:                                                                              | The ID of the buyer to update shipping details for.                                             | fe26475d-ec3e-4884-9553-f7356683f7f9                                                            |
| `shipping_details_id`                                                                           | *str*                                                                                           | :heavy_check_mark:                                                                              | The ID of the shipping details to update.                                                       | bf8c36ad-02d9-4904-b0f9-a230b149e341                                                            |
| `merchant_account_id`                                                                           | *Optional[str]*                                                                                 | :heavy_minus_sign:                                                                              | The ID of the merchant account to use for this request.                                         | default                                                                                         |
| `first_name`                                                                                    | *OptionalNullable[str]*                                                                         | :heavy_minus_sign:                                                                              | The first name(s) or given name for the buyer.                                                  | John                                                                                            |
| `last_name`                                                                                     | *OptionalNullable[str]*                                                                         | :heavy_minus_sign:                                                                              | The last name, or family name, of the buyer.                                                    | Doe                                                                                             |
| `email_address`                                                                                 | *OptionalNullable[str]*                                                                         | :heavy_minus_sign:                                                                              | The email address for the buyer.                                                                | john@example.com                                                                                |
| `phone_number`                                                                                  | *OptionalNullable[str]*                                                                         | :heavy_minus_sign:                                                                              | The phone number for the buyer which should be formatted according to the E164 number standard. | +1234567890                                                                                     |
| `address`                                                                                       | [OptionalNullable[models.Address]](../../models/address.md)                                     | :heavy_minus_sign:                                                                              | The billing address for the buyer.                                                              |                                                                                                 |
| `retries`                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                | :heavy_minus_sign:                                                                              | Configuration to override the default retry behavior of the client.                             |                                                                                                 |

### Response

**[models.ShippingDetails](../../models/shippingdetails.md)**

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

Delete the shipping details associated to a specific buyer.

### Example Usage

<!-- UsageSnippet language="python" operationID="delete_buyer_shipping_details" method="delete" path="/buyers/{buyer_id}/shipping-details/{shipping_details_id}" -->
```python
from gr4vy import Gr4vy
import os


with Gr4vy(
    merchant_account_id="default",
    bearer_auth=os.getenv("GR4VY_BEARER_AUTH", ""),
) as g_client:

    g_client.buyers.shipping_details.delete(buyer_id="fe26475d-ec3e-4884-9553-f7356683f7f9", shipping_details_id="bf8c36ad-02d9-4904-b0f9-a230b149e341")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `buyer_id`                                                          | *str*                                                               | :heavy_check_mark:                                                  | The ID of the buyer to delete shipping details for.                 | fe26475d-ec3e-4884-9553-f7356683f7f9                                |
| `shipping_details_id`                                               | *str*                                                               | :heavy_check_mark:                                                  | The ID of the shipping details to delete.                           | bf8c36ad-02d9-4904-b0f9-a230b149e341                                |
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