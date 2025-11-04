# Gr4vy Python SDK

Developer-friendly & type-safe Python SDK specifically catered to leverage *Gr4vy* API.

<div align="left">
    <a href="https://pypi.org/project/gr4vy/"></a><img alt="PyPI - Version" src="https://img.shields.io/pypi/v/gr4vy?style=for-the-badge"></a>
    <a href="https://www.speakeasy.com/?utm_source=gr4vy&utm_campaign=python">
        <img src="https://custom-icon-badges.demolab.com/badge/-Built%20By%20Speakeasy-212015?style=for-the-badge&logoColor=FBE331&logo=speakeasy&labelColor=545454" />
    </a>
</div>

## Summary

Gr4vy Python SDK

The official Gr4vy SDK for Python provides a convenient way to interact with the Gr4vy API from your server-side application. This SDK allows you to seamlessly integrate Gr4vy's powerful payment orchestration capabilities, including:

* Creating Transactions: Initiate and process payments with various payment methods and services.
* Managing Buyers: Store and manage buyer information securely.
* Storing Payment Methods: Securely store and tokenize payment methods for future use.
* Handling Webhooks: Easily process and respond to webhook events from Gr4vy.
* And much more: Access the full suite of Gr4vy API payment features.

This SDK is designed to simplify development, reduce boilerplate code, and help you get up and running with Gr4vy quickly and efficiently. It handles authentication, request signing, and provides easy-to-use methods for most API endpoints.

<!-- No Summary [summary] -->

<!-- Start Table of Contents [toc] -->
## Table of Contents
<!-- $toc-max-depth=2 -->
* [Gr4vy Python SDK](#gr4vy-python-sdk)
  * [SDK Installation](#sdk-installation)
  * [IDE Support](#ide-support)
  * [SDK Example Usage](#sdk-example-usage)
  * [Bearer token generation](#bearer-token-generation)
  * [Embed token generation](#embed-token-generation)
  * [Merchant account ID selection](#merchant-account-id-selection)
  * [Webhooks verification](#webhooks-verification)
  * [Available Resources and Operations](#available-resources-and-operations)
  * [Global Parameters](#global-parameters)
  * [Pagination](#pagination)
  * [Retries](#retries)
  * [Error Handling](#error-handling)
  * [Server Selection](#server-selection)
  * [Custom HTTP Client](#custom-http-client)
  * [Resource Management](#resource-management)
  * [Debugging](#debugging)
* [Development](#development)
  * [Testing](#testing)
  * [Contributions](#contributions)

<!-- End Table of Contents [toc] -->

<!-- Start SDK Installation [installation] -->
## SDK Installation

> [!NOTE]
> **Python version upgrade policy**
>
> Once a Python version reaches its [official end of life date](https://devguide.python.org/versions/), a 3-month grace period is provided for users to upgrade. Following this grace period, the minimum python version supported in the SDK will be updated.

The SDK can be installed with *uv*, *pip*, or *poetry* package managers.

### uv

*uv* is a fast Python package installer and resolver, designed as a drop-in replacement for pip and pip-tools. It's recommended for its speed and modern Python tooling capabilities.

```bash
uv add gr4vy
```

### PIP

*PIP* is the default package installer for Python, enabling easy installation and management of packages from PyPI via the command line.

```bash
pip install gr4vy
```

### Poetry

*Poetry* is a modern tool that simplifies dependency management and package publishing by using a single `pyproject.toml` file to handle project metadata and dependencies.

```bash
poetry add gr4vy
```

### Shell and script usage with `uv`

You can use this SDK in a Python shell with [uv](https://docs.astral.sh/uv/) and the `uvx` command that comes with it like so:

```shell
uvx --from gr4vy python
```

It's also possible to write a standalone Python script without needing to set up a whole project like so:

```python
#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.9"
# dependencies = [
#     "gr4vy",
# ]
# ///

from gr4vy import Gr4vy

sdk = Gr4vy(
  # SDK arguments
)

# Rest of script here...
```

Once that is saved to a file, you can run it with `uv run script.py` where
`script.py` can be replaced with the actual file name.
<!-- End SDK Installation [installation] -->

<!-- Start IDE Support [idesupport] -->
## IDE Support

### PyCharm

Generally, the SDK will work well with most IDEs out of the box. However, when using PyCharm, you can enjoy much better integration with Pydantic by installing an additional plugin.

- [PyCharm Pydantic Plugin](https://docs.pydantic.dev/latest/integrations/pycharm/)
<!-- End IDE Support [idesupport] -->

## SDK Example Usage

### Example

```python
# Synchronous Example
from gr4vy import Gr4vy, auth
import os


with Gr4vy(
    id="example",
    server="production",
    merchant_account_id="default",
    bearer_auth=auth.with_token(open("./private_key.pem").read())
) as g_client:

    res = g_client.transactions.list()

    assert res is not None

    # Handle response
    print(res)
```

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
from gr4vy import Gr4vy, auth
import os

async def main():

    async with Gr4vy(
        id="example",
        server="production",
        merchant_account_id="default",
        bearer_auth=auth.with_token(open("./private_key.pem").read())
    ) as g_client:
        res = await g_client.transactions.list()

        assert res is not None

        # Handle response
        print(res)

asyncio.run(main())
```

<br /><br />
> [!IMPORTANT]
> Please use the `auth.with_token` where the documentation mentions `os.getenv("GR4VY_BEARER_AUTH", ""),`.

<!-- No SDK Example Usage [usage] -->

<!-- No Authentication [security] -->

## Bearer token generation

Alternatively, you can create a token for use with the SDK or with your own client library.

```python
from gr4vy import Gr4vy, auth

auth.get_token(open("./private_key.pem").read()
```

> **Note:** This will only create a token once. Use `auth.with_token` to dynamically generate a token
> for every request.


## Embed token generation

Alternatively, you can create a token for use with Embed as follows.

```python
from gr4vy import Gr4vy, auth

private_key = open("./private_key.pem").read()

g_client = Gr4vy(
    id="example",
    server="production",
    merchant_account_id="default",
    bearer_auth=auth.with_token(private_key)
)

checkout_session = g_client.checkout_sessions.create()

auth.get_embed_token(
    privatekey,
    embed_params={
        "amount": 1299,
        "currency": 'USD',
        "buyer_external_identifier": 'user-1234',
    },
    checkout_session_id=checkout_session.id
)
```

> **Note:** This will only create a token once. Use `with_token` to dynamically generate a token
> for every request.

## Merchant account ID selection

Depending on the key used, you might need to explicitly define a merchant account ID to use. In our API, 
this uses the `X-GR4VY-MERCHANT-ACCOUNT-ID` header. When using the SDK, you can set the `merchant_account_id`
on every request.

```py
res = g_client.transactions.list(merchant_account_id: 'merchant-12345')
```

Alternatively, the merchant account ID can also be set when initializing the SDK.

```py
with Gr4vy(
    id="spider",
    merchant_account_id="merchant-12345",
    bearer_auth=auth.get_token(private_key)
) as g_client:
    response = g_client.transactions.list()
```

## Webhooks verification

The SDK makes it easy to verify that incoming webhooks were actually sent by Gr4vy. Once you have configured the webhook subscription with its corresponding secret, that can be verified the following way:

```py
from gr4vy.webhooks import verify_webhook

# Webhook payload and headers
payload = 'your-webhook-payload'
secret = 'your-webhook-secret'
signature_header = 'signatures-from-header'
timestamp_header = 'timestamp-from-header'
timestamp_tolerance = 300  # optional, in seconds (default: 0)

try:
    # Verify the webhook
    verify_webhook(
        payload=payload,
        secret=secret,
        signature_header=signature_header,
        timestamp_header=timestamp_header,
        timestamp_tolerance=timestamp_tolerance
    )
    print('Webhook verified successfully!')
except ValueError as error:
    print(f'Webhook verification failed: {error}')
```

### Parameters

- **`payload`**: The raw payload string received in the webhook request.
- **`secret`**: The secret used to sign the webhook. This is provided in your Gr4vy dashboard.
- **`signatureHeader`**: The `X-Gr4vy-Signature` header from the webhook request.
- **`timestampHeader`**: The `X-Gr4vy-Timestamp` header from the webhook request.
- **`timestampTolerance`**: _(Optional)_ The maximum allowed difference (in seconds) between the current time and the timestamp in the webhook. Defaults to `0` (no tolerance).



<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

<details open>
<summary>Available methods</summary>

#### [account_updater.jobs](docs/sdks/jobs/README.md)

* [create](docs/sdks/jobs/README.md#create) - Create account updater job

### [audit_logs](docs/sdks/auditlogs/README.md)

* [list](docs/sdks/auditlogs/README.md#list) - List audit log entries

### [buyers](docs/sdks/buyerssdk/README.md)

* [list](docs/sdks/buyerssdk/README.md#list) - List all buyers
* [create](docs/sdks/buyerssdk/README.md#create) - Add a buyer
* [get](docs/sdks/buyerssdk/README.md#get) - Get a buyer
* [update](docs/sdks/buyerssdk/README.md#update) - Update a buyer
* [delete](docs/sdks/buyerssdk/README.md#delete) - Delete a buyer

#### [buyers.gift_cards](docs/sdks/buyersgiftcards/README.md)

* [list](docs/sdks/buyersgiftcards/README.md#list) - List gift cards for a buyer

#### [buyers.payment_methods](docs/sdks/buyerspaymentmethods/README.md)

* [list](docs/sdks/buyerspaymentmethods/README.md#list) - List payment methods for a buyer

#### [buyers.shipping_details](docs/sdks/buyersshippingdetails/README.md)

* [create](docs/sdks/buyersshippingdetails/README.md#create) - Add buyer shipping details
* [list](docs/sdks/buyersshippingdetails/README.md#list) - List a buyer's shipping details
* [get](docs/sdks/buyersshippingdetails/README.md#get) - Get buyer shipping details
* [update](docs/sdks/buyersshippingdetails/README.md#update) - Update a buyer's shipping details
* [delete](docs/sdks/buyersshippingdetails/README.md#delete) - Delete a buyer's shipping details

### [card_scheme_definitions](docs/sdks/cardschemedefinitionssdk/README.md)

* [list](docs/sdks/cardschemedefinitionssdk/README.md#list) - List card scheme definitions

### [checkout_sessions](docs/sdks/checkoutsessions/README.md)

* [create](docs/sdks/checkoutsessions/README.md#create) - Create checkout session
* [update](docs/sdks/checkoutsessions/README.md#update) - Update checkout session
* [get](docs/sdks/checkoutsessions/README.md#get) - Get checkout session
* [delete](docs/sdks/checkoutsessions/README.md#delete) - Delete checkout session

### [digital_wallets](docs/sdks/digitalwalletssdk/README.md)

* [create](docs/sdks/digitalwalletssdk/README.md#create) - Register digital wallet
* [list](docs/sdks/digitalwalletssdk/README.md#list) - List digital wallets
* [get](docs/sdks/digitalwalletssdk/README.md#get) - Get digital wallet
* [delete](docs/sdks/digitalwalletssdk/README.md#delete) - Delete digital wallet
* [update](docs/sdks/digitalwalletssdk/README.md#update) - Update digital wallet

#### [digital_wallets.domains](docs/sdks/domains/README.md)

* [create](docs/sdks/domains/README.md#create) - Register a digital wallet domain
* [delete](docs/sdks/domains/README.md#delete) - Remove a digital wallet domain

#### [digital_wallets.sessions](docs/sdks/sessions/README.md)

* [google_pay](docs/sdks/sessions/README.md#google_pay) - Create a Google Pay session
* [apple_pay](docs/sdks/sessions/README.md#apple_pay) - Create a Apple Pay session
* [click_to_pay](docs/sdks/sessions/README.md#click_to_pay) - Create a Click to Pay session

### [gift_cards](docs/sdks/giftcardssdk/README.md)

* [get](docs/sdks/giftcardssdk/README.md#get) - Get gift card
* [delete](docs/sdks/giftcardssdk/README.md#delete) - Delete a gift card
* [create](docs/sdks/giftcardssdk/README.md#create) - Create gift card
* [list](docs/sdks/giftcardssdk/README.md#list) - List gift cards

#### [gift_cards.balances](docs/sdks/balances/README.md)

* [list](docs/sdks/balances/README.md#list) - List gift card balances

### [merchant_accounts](docs/sdks/merchantaccountssdk/README.md)

* [list](docs/sdks/merchantaccountssdk/README.md#list) - List all merchant accounts
* [create](docs/sdks/merchantaccountssdk/README.md#create) - Create a merchant account
* [get](docs/sdks/merchantaccountssdk/README.md#get) - Get a merchant account
* [update](docs/sdks/merchantaccountssdk/README.md#update) - Update a merchant account

### [payment_links](docs/sdks/paymentlinkssdk/README.md)

* [create](docs/sdks/paymentlinkssdk/README.md#create) - Add a payment link
* [list](docs/sdks/paymentlinkssdk/README.md#list) - List all payment links
* [expire](docs/sdks/paymentlinkssdk/README.md#expire) - Expire a payment link
* [get](docs/sdks/paymentlinkssdk/README.md#get) - Get payment link

### [payment_methods](docs/sdks/paymentmethodssdk/README.md)

* [list](docs/sdks/paymentmethodssdk/README.md#list) - List all payment methods
* [create](docs/sdks/paymentmethodssdk/README.md#create) - Create payment method
* [get](docs/sdks/paymentmethodssdk/README.md#get) - Get payment method
* [delete](docs/sdks/paymentmethodssdk/README.md#delete) - Delete payment method

#### [payment_methods.network_tokens](docs/sdks/paymentmethodsnetworktokens/README.md)

* [list](docs/sdks/paymentmethodsnetworktokens/README.md#list) - List network tokens
* [create](docs/sdks/paymentmethodsnetworktokens/README.md#create) - Provision network token
* [suspend](docs/sdks/paymentmethodsnetworktokens/README.md#suspend) - Suspend network token
* [resume](docs/sdks/paymentmethodsnetworktokens/README.md#resume) - Resume network token
* [delete](docs/sdks/paymentmethodsnetworktokens/README.md#delete) - Delete network token

#### [payment_methods.network_tokens.cryptogram](docs/sdks/networktokenscryptogram/README.md)

* [create](docs/sdks/networktokenscryptogram/README.md#create) - Provision network token cryptogram

#### [payment_methods.payment_service_tokens](docs/sdks/paymentmethodspaymentservicetokens/README.md)

* [list](docs/sdks/paymentmethodspaymentservicetokens/README.md#list) - List payment service tokens
* [create](docs/sdks/paymentmethodspaymentservicetokens/README.md#create) - Create payment service token
* [delete](docs/sdks/paymentmethodspaymentservicetokens/README.md#delete) - Delete payment service token

### [payment_options](docs/sdks/paymentoptionssdk/README.md)

* [list](docs/sdks/paymentoptionssdk/README.md#list) - List payment options

### [payment_service_definitions](docs/sdks/paymentservicedefinitionssdk/README.md)

* [list](docs/sdks/paymentservicedefinitionssdk/README.md#list) - List payment service definitions
* [get](docs/sdks/paymentservicedefinitionssdk/README.md#get) - Get a payment service definition
* [session](docs/sdks/paymentservicedefinitionssdk/README.md#session) - Create a session for a payment service definition

### [payment_services](docs/sdks/paymentservicessdk/README.md)

* [list](docs/sdks/paymentservicessdk/README.md#list) - List payment services
* [create](docs/sdks/paymentservicessdk/README.md#create) - Update a configured payment service
* [get](docs/sdks/paymentservicessdk/README.md#get) - Get payment service
* [update](docs/sdks/paymentservicessdk/README.md#update) - Configure a payment service
* [delete](docs/sdks/paymentservicessdk/README.md#delete) - Delete a configured payment service
* [verify](docs/sdks/paymentservicessdk/README.md#verify) - Verify payment service credentials
* [session](docs/sdks/paymentservicessdk/README.md#session) - Create a session for a payment service definition

### [payouts](docs/sdks/payouts/README.md)

* [list](docs/sdks/payouts/README.md#list) - List payouts created
* [create](docs/sdks/payouts/README.md#create) - Create a payout
* [get](docs/sdks/payouts/README.md#get) - Get a payout

### [refunds](docs/sdks/refundssdk/README.md)

* [get](docs/sdks/refundssdk/README.md#get) - Get refund

### [report_executions](docs/sdks/reportexecutionssdk/README.md)

* [list](docs/sdks/reportexecutionssdk/README.md#list) - List executed reports

### [reports](docs/sdks/reportssdk/README.md)

* [list](docs/sdks/reportssdk/README.md#list) - List configured reports
* [create](docs/sdks/reportssdk/README.md#create) - Add a report
* [get](docs/sdks/reportssdk/README.md#get) - Get a report
* [put](docs/sdks/reportssdk/README.md#put) - Update a report

#### [reports.executions](docs/sdks/executions/README.md)

* [list](docs/sdks/executions/README.md#list) - List executions for report
* [url](docs/sdks/executions/README.md#url) - Create URL for executed report
* [get](docs/sdks/executions/README.md#get) - Get executed report

### [transactions](docs/sdks/transactions/README.md)

* [list](docs/sdks/transactions/README.md#list) - List transactions
* [create](docs/sdks/transactions/README.md#create) - Create transaction
* [get](docs/sdks/transactions/README.md#get) - Get transaction
* [update](docs/sdks/transactions/README.md#update) - Manually update a transaction
* [capture](docs/sdks/transactions/README.md#capture) - Capture transaction
* [void](docs/sdks/transactions/README.md#void) - Void transaction
* [cancel](docs/sdks/transactions/README.md#cancel) - Cancel transaction
* [sync](docs/sdks/transactions/README.md#sync) - Sync transaction

#### [transactions.events](docs/sdks/events/README.md)

* [list](docs/sdks/events/README.md#list) - List transaction events

#### [transactions.refunds](docs/sdks/transactionsrefunds/README.md)

* [list](docs/sdks/transactionsrefunds/README.md#list) - List transaction refunds
* [create](docs/sdks/transactionsrefunds/README.md#create) - Create transaction refund
* [get](docs/sdks/transactionsrefunds/README.md#get) - Get transaction refund

#### [transactions.refunds.all](docs/sdks/all/README.md)

* [create](docs/sdks/all/README.md#create) - Create batch transaction refund

#### [transactions.settlements](docs/sdks/transactionssettlements/README.md)

* [get](docs/sdks/transactionssettlements/README.md#get) - Get transaction settlement
* [list](docs/sdks/transactionssettlements/README.md#list) - List transaction settlements

</details>
<!-- End Available Resources and Operations [operations] -->

<!-- Start Global Parameters [global-parameters] -->
## Global Parameters

A parameter is configured globally. This parameter may be set on the SDK client instance itself during initialization. When configured as an option during SDK initialization, This global value will be used as the default on the operations that use it. When such operations are called, there is a place in each to override the global value, if needed.

For example, you can set `merchant_account_id` to `` at SDK initialization and then you do not have to pass the same value on calls to operations like `get`. But if you want to do so you may, which will locally override the global setting. See the example code below for a demonstration.


### Available Globals

The following global parameter is available.
Global parameters can also be set via environment variable.

| Name                | Type | Description                                             | Environment               |
| ------------------- | ---- | ------------------------------------------------------- | ------------------------- |
| merchant_account_id | str  | The ID of the merchant account to use for this request. | GR4VY_MERCHANT_ACCOUNT_ID |

### Example

```python
from gr4vy import Gr4vy
import os


with Gr4vy(
    merchant_account_id="default",
    bearer_auth=os.getenv("GR4VY_BEARER_AUTH", ""),
) as g_client:

    res = g_client.merchant_accounts.get(merchant_account_id="merchant-12345")

    # Handle response
    print(res)

```
<!-- End Global Parameters [global-parameters] -->

<!-- Start Pagination [pagination] -->
## Pagination

Some of the endpoints in this SDK support pagination. To use pagination, you make your SDK calls as usual, but the
returned response object will have a `Next` method that can be called to pull down the next group of results. If the
return value of `Next` is `None`, then there are no more pages to be fetched.

Here's an example of one such pagination call:
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
<!-- End Pagination [pagination] -->

<!-- Start Retries [retries] -->
## Retries

Some of the endpoints in this SDK support retries. If you use the SDK without any configuration, it will fall back to the default retry strategy provided by the API. However, the default retry strategy can be overridden on a per-operation basis, or across the entire SDK.

To change the default retry strategy for a single API call, simply provide a `RetryConfig` object to the call:
```python
from gr4vy import Gr4vy
from gr4vy.utils import BackoffStrategy, RetryConfig
import os


with Gr4vy(
    merchant_account_id="default",
    bearer_auth=os.getenv("GR4VY_BEARER_AUTH", ""),
) as g_client:

    res = g_client.account_updater.jobs.create(payment_method_ids=[
        "ef9496d8-53a5-4aad-8ca2-00eb68334389",
        "f29e886e-93cc-4714-b4a3-12b7a718e595",
    ],
        RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False))

    assert res is not None

    # Handle response
    print(res)

```

If you'd like to override the default retry strategy for all operations that support retries, you can use the `retry_config` optional parameter when initializing the SDK:
```python
from gr4vy import Gr4vy
from gr4vy.utils import BackoffStrategy, RetryConfig
import os


with Gr4vy(
    retry_config=RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False),
    merchant_account_id="default",
    bearer_auth=os.getenv("GR4VY_BEARER_AUTH", ""),
) as g_client:

    res = g_client.account_updater.jobs.create(payment_method_ids=[
        "ef9496d8-53a5-4aad-8ca2-00eb68334389",
        "f29e886e-93cc-4714-b4a3-12b7a718e595",
    ])

    assert res is not None

    # Handle response
    print(res)

```
<!-- End Retries [retries] -->

<!-- Start Error Handling [errors] -->
## Error Handling

[`Gr4vyError`](./src/gr4vy/errors/gr4vyerror.py) is the base class for all HTTP error responses. It has the following properties:

| Property           | Type             | Description                                                                             |
| ------------------ | ---------------- | --------------------------------------------------------------------------------------- |
| `err.message`      | `str`            | Error message                                                                           |
| `err.status_code`  | `int`            | HTTP response status code eg `404`                                                      |
| `err.headers`      | `httpx.Headers`  | HTTP response headers                                                                   |
| `err.body`         | `str`            | HTTP body. Can be empty string if no body is returned.                                  |
| `err.raw_response` | `httpx.Response` | Raw HTTP response                                                                       |
| `err.data`         |                  | Optional. Some errors may contain structured data. [See Error Classes](#error-classes). |

### Example
```python
from gr4vy import Gr4vy, errors
import os
from typing import Literal


with Gr4vy(
    merchant_account_id="default",
    bearer_auth=os.getenv("GR4VY_BEARER_AUTH", ""),
) as g_client:
    res = None
    try:

        res = g_client.account_updater.jobs.create(payment_method_ids=[
            "ef9496d8-53a5-4aad-8ca2-00eb68334389",
            "f29e886e-93cc-4714-b4a3-12b7a718e595",
        ])

        assert res is not None

        # Handle response
        print(res)


    except errors.Gr4vyError as e:
        # The base class for HTTP error responses
        print(e.message)
        print(e.status_code)
        print(e.body)
        print(e.headers)
        print(e.raw_response)

        # Depending on the method different errors may be thrown
        if isinstance(e, errors.Error400):
            print(e.data.type)  # Optional[Literal["error"]]
            print(e.data.code)  # Optional[str]
            print(e.data.status)  # Optional[int]
            print(e.data.message)  # Optional[str]
            print(e.data.details)  # Optional[List[models.ErrorDetail]]
```

### Error Classes
**Primary errors:**
* [`Gr4vyError`](./src/gr4vy/errors/gr4vyerror.py): The base class for HTTP error responses.
  * [`Error400`](./src/gr4vy/errors/error400.py): The request was invalid. Status code `400`.
  * [`Error401`](./src/gr4vy/errors/error401.py): The request was unauthorized. Status code `401`.
  * [`Error403`](./src/gr4vy/errors/error403.py): The credentials were invalid or the caller did not have permission to act on the resource. Status code `403`.
  * [`Error404`](./src/gr4vy/errors/error404.py): The resource was not found. Status code `404`.
  * [`Error405`](./src/gr4vy/errors/error405.py): The request method was not allowed. Status code `405`.
  * [`Error409`](./src/gr4vy/errors/error409.py): A duplicate record was found. Status code `409`.
  * [`Error425`](./src/gr4vy/errors/error425.py): The request was too early. Status code `425`.
  * [`Error429`](./src/gr4vy/errors/error429.py): Too many requests were made. Status code `429`.
  * [`Error500`](./src/gr4vy/errors/error500.py): The server encountered an error. Status code `500`.
  * [`Error502`](./src/gr4vy/errors/error502.py): The server encountered an error. Status code `502`.
  * [`Error504`](./src/gr4vy/errors/error504.py): The server encountered an error. Status code `504`.
  * [`HTTPValidationError`](./src/gr4vy/errors/httpvalidationerror.py): Validation Error. Status code `422`. *

<details><summary>Less common errors (5)</summary>

<br />

**Network errors:**
* [`httpx.RequestError`](https://www.python-httpx.org/exceptions/#httpx.RequestError): Base class for request errors.
    * [`httpx.ConnectError`](https://www.python-httpx.org/exceptions/#httpx.ConnectError): HTTP client was unable to make a request to a server.
    * [`httpx.TimeoutException`](https://www.python-httpx.org/exceptions/#httpx.TimeoutException): HTTP request timed out.


**Inherit from [`Gr4vyError`](./src/gr4vy/errors/gr4vyerror.py)**:
* [`ResponseValidationError`](./src/gr4vy/errors/responsevalidationerror.py): Type mismatch between the response data and the expected Pydantic model. Provides access to the Pydantic validation error via the `cause` attribute.

</details>

\* Check [the method documentation](#available-resources-and-operations) to see if the error is applicable.
<!-- End Error Handling [errors] -->

<!-- Start Server Selection [server] -->
## Server Selection

### Select Server by Name

You can override the default server globally by passing a server name to the `server: str` optional parameter when initializing the SDK client instance. The selected server will then be used as the default on the operations that use it. This table lists the names associated with the available servers:

| Name         | Server                               | Variables | Description |
| ------------ | ------------------------------------ | --------- | ----------- |
| `sandbox`    | `https://api.sandbox.{id}.gr4vy.app` | `id`      |             |
| `production` | `https://api.{id}.gr4vy.app`         | `id`      |             |

If the selected server has variables, you may override its default values through the additional parameters made available in the SDK constructor:

| Variable | Parameter | Default     | Description                            |
| -------- | --------- | ----------- | -------------------------------------- |
| `id`     | `id: str` | `"example"` | The subdomain for your Gr4vy instance. |

#### Example

```python
from gr4vy import Gr4vy
import os


with Gr4vy(
    server="sandbox",
    id="example",
    merchant_account_id="default",
    bearer_auth=os.getenv("GR4VY_BEARER_AUTH", ""),
) as g_client:

    res = g_client.account_updater.jobs.create(payment_method_ids=[
        "ef9496d8-53a5-4aad-8ca2-00eb68334389",
        "f29e886e-93cc-4714-b4a3-12b7a718e595",
    ])

    assert res is not None

    # Handle response
    print(res)

```

### Override Server URL Per-Client

The default server can also be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
from gr4vy import Gr4vy
import os


with Gr4vy(
    server_url="https://api.sandbox.example.gr4vy.app",
    merchant_account_id="default",
    bearer_auth=os.getenv("GR4VY_BEARER_AUTH", ""),
) as g_client:

    res = g_client.account_updater.jobs.create(payment_method_ids=[
        "ef9496d8-53a5-4aad-8ca2-00eb68334389",
        "f29e886e-93cc-4714-b4a3-12b7a718e595",
    ])

    assert res is not None

    # Handle response
    print(res)

```
<!-- End Server Selection [server] -->

<!-- Start Custom HTTP Client [http-client] -->
## Custom HTTP Client

The Python SDK makes API calls using the [httpx](https://www.python-httpx.org/) HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with your own HTTP client instance.
Depending on whether you are using the sync or async version of the SDK, you can pass an instance of `HttpClient` or `AsyncHttpClient` respectively, which are Protocol's ensuring that the client has the necessary methods to make API calls.
This allows you to wrap the client with your own custom logic, such as adding custom headers, logging, or error handling, or you can just pass an instance of `httpx.Client` or `httpx.AsyncClient` directly.

For example, you could specify a header for every request that this sdk makes as follows:
```python
from gr4vy import Gr4vy
import httpx

http_client = httpx.Client(headers={"x-custom-header": "someValue"})
s = Gr4vy(client=http_client)
```

or you could wrap the client with your own custom logic:
```python
from gr4vy import Gr4vy
from gr4vy.httpclient import AsyncHttpClient
import httpx

class CustomClient(AsyncHttpClient):
    client: AsyncHttpClient

    def __init__(self, client: AsyncHttpClient):
        self.client = client

    async def send(
        self,
        request: httpx.Request,
        *,
        stream: bool = False,
        auth: Union[
            httpx._types.AuthTypes, httpx._client.UseClientDefault, None
        ] = httpx.USE_CLIENT_DEFAULT,
        follow_redirects: Union[
            bool, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
    ) -> httpx.Response:
        request.headers["Client-Level-Header"] = "added by client"

        return await self.client.send(
            request, stream=stream, auth=auth, follow_redirects=follow_redirects
        )

    def build_request(
        self,
        method: str,
        url: httpx._types.URLTypes,
        *,
        content: Optional[httpx._types.RequestContent] = None,
        data: Optional[httpx._types.RequestData] = None,
        files: Optional[httpx._types.RequestFiles] = None,
        json: Optional[Any] = None,
        params: Optional[httpx._types.QueryParamTypes] = None,
        headers: Optional[httpx._types.HeaderTypes] = None,
        cookies: Optional[httpx._types.CookieTypes] = None,
        timeout: Union[
            httpx._types.TimeoutTypes, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
        extensions: Optional[httpx._types.RequestExtensions] = None,
    ) -> httpx.Request:
        return self.client.build_request(
            method,
            url,
            content=content,
            data=data,
            files=files,
            json=json,
            params=params,
            headers=headers,
            cookies=cookies,
            timeout=timeout,
            extensions=extensions,
        )

s = Gr4vy(async_client=CustomClient(httpx.AsyncClient()))
```
<!-- End Custom HTTP Client [http-client] -->

<!-- Start Resource Management [resource-management] -->
## Resource Management

The `Gr4vy` class implements the context manager protocol and registers a finalizer function to close the underlying sync and async HTTPX clients it uses under the hood. This will close HTTP connections, release memory and free up other resources held by the SDK. In short-lived Python programs and notebooks that make a few SDK method calls, resource management may not be a concern. However, in longer-lived programs, it is beneficial to create a single SDK instance via a [context manager][context-manager] and reuse it across the application.

[context-manager]: https://docs.python.org/3/reference/datamodel.html#context-managers

```python
from gr4vy import Gr4vy
import os
def main():

    with Gr4vy(
        merchant_account_id="default",
        bearer_auth=os.getenv("GR4VY_BEARER_AUTH", ""),
    ) as g_client:
        # Rest of application here...


# Or when using async:
async def amain():

    async with Gr4vy(
        merchant_account_id="default",
        bearer_auth=os.getenv("GR4VY_BEARER_AUTH", ""),
    ) as g_client:
        # Rest of application here...
```
<!-- End Resource Management [resource-management] -->

<!-- Start Debugging [debug] -->
## Debugging

You can setup your SDK to emit debug logs for SDK requests and responses.

You can pass your own logger class directly into your SDK.
```python
from gr4vy import Gr4vy
import logging

logging.basicConfig(level=logging.DEBUG)
s = Gr4vy(debug_logger=logging.getLogger("gr4vy"))
```

You can also enable a default debug logger by setting an environment variable `GR4VY_DEBUG` to true.
<!-- End Debugging [debug] -->

<!-- Placeholder for Future Speakeasy SDK Sections -->

# Development

## Testing

To run the tests, install Python and Poetry, ensure to download the `private_key.pem` for the test environment, and run the following.

```sh
poetry install
poetry run pytest
```

## Contributions

While we value open-source contributions to this SDK, this library is generated programmatically. Any manual changes added to internal files will be overwritten on the next generation. 
We look forward to hearing your feedback. Feel free to open a PR or an issue with a proof of concept and we'll do our best to include it in a future release. 

### SDK Created by [Speakeasy](https://www.speakeasy.com/?utm_source=gr4vy&utm_campaign=python)
