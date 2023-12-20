# Gr4vy SDK for Python

Gr4vy provides any of your payment integrations through one unified API. For
more details, visit [gr4vy.com](https://gr4vy.com).

## Installation

To add Gr4vy to your project simply install with pip:

```python
pip install gr4vy
```

Add import:

```python
import gr4vy
```

## Getting Started

To make your first API call, you will need to [request](https://gr4vy.com) a
Gr4vy instance to be set up. Please contact our sales team for a demo.

Once you have been set up with a Gr4vy account you will need to head over to the
**Integrations** panel and generate a private key. We recommend storing this key
in a secure location but in this code sample, we simply read the file from disk.
For multi-merchant environments, an optional merchant ID can be provided as well.

```python
from gr4vy import Gr4vyClient
client = Gr4vyClient("gr4vy_instance","location_of_key_file", "sandbox_or_production", "my-merchant-id)
client.ListBuyers()
```

## Gr4vy Embed

To create a token for Gr4vy Embed, call the `client.GetEmbedToken(embed)`
function with the amount, currency, and optional buyer information for Gr4vy
Embed.

```python
embed = {
  "amount": 1299,
  "currency": "USD",
  "buyerExternalIdentifier": "user-12345",
}

token = client.generate_embed_token(embed)
```

You can now pass this token to your frontend where it can be used to
authenticate Gr4vy Embed.

The `buyer_id` and/or `buyer_external_identifier` fields can be used to allow
the token to pull in previously stored payment methods for a user. A buyer
needs to be created before it can be used in this way.

```python
  from gr4vy import Gr4vyClient

  client = Gr4vyClient("gr4vy_instance","private_key.pem", "production")

  buyer_request = {"display_name": "Jane Smith"}

  new_buyer = client.create_new_buyer(**buyer_request).get('id')
  embed_data = {
    "amount": 1299,
    "currency": "USD",
    "buyerId": new_buyer,
  }

  embed_token = client.generate_embed_token(embed_data=embed_data)

  print("Embed token: {}".format(embed_token))
```
Checkout sessions can also be passed within an Embed token:

```python
  from gr4vy import Gr4vyClient

  client = Gr4vyClient("gr4vy_instance","private_key.pem", "production")

  checkout_session_id = client.create_new_checkout_session().get("id")
  
  embed_data = {
    "amount": 1299,
    "currency": "USD",
  }

  embed_token = client.generate_embed_token(
        embed_data=embed_data, checkout_session_id=checkout_session_id
    )

  print("Embed token: {}".format(embed_token))
```



## Initialization

The client can be initialized with the Gr4vy ID (`gr4vyId`), the location of the private key, and the environment attempting to access.

```python
  client = Gr4vyClient("gr4vyId","private_key.pem", "sandbox")
```

Alternatively, instead of the `gr4vyId` it can be initialized with the `baseUrl`
of the server to use directly and the environment attempting to access.

```python
  client = Gr4vyClientWithBaseUrl("https://*gr4vyId*.gr4vy.app","private_key.pem", "sandbox")
```

Your API private key can be created in your admin panel on the **Integrations**
tab.

## Multi Merchant
Setting the Merchant ID for requests can be set on the client:

```python
  client = Gr4vyClient("gr4vyId","private_key.pem", "sandbox", merchant_account_id="merchant-id")
```

## Making API calls

This library conveniently maps every API path to a separate function. For
example, `GET /buyers?limit=100` would be:

```python
  client.list_buyers({"limit=100"})
```

To create, the API requires a request object for that resource. This is created by creating a dictionary object for the request.

For example, to create a buyer:

```python
  from gr4vy import BuyerRequest

  buyer_request = {"display_name": "Jane Smith"}
  new_buyer = client.add_buyer(**buyer_request)

```

To update a buyer:

```python
  buyer_id: "buyer_uuid_from_gr4vy"
  buyer_request = {"display_name": "Jane Changed")
  buyer_update = client.update_buyer(buyer_id, **buyer_request)
```

## Response

Every resolved API call returns the requested resource, errors are printed to the console


```python
  print(client.list_buyers())
```

## Logging & Debugging

The SDK makes it possible to log responses to the console.

```python
  print(client.list_buyers())
```

This will output the request parameters and response to the console as follows.

```sh
{"items":[{"id":"b8433347-a16f-46b5-958f-d681876546a6","type":"buyer","display_name":"Jane Smith","external_identifier":None,"created_at":"2021-04-22T06:51:16.910297+00:00","updated_at":"2021-04-22T07:18:49.816242+00:00"}],"limit":1,"next_cursor":"fAA0YjY5NmU2My00NzY5LTQ2OGMtOTEyNC0xODVjMDdjZTY5MzEAMjAyMS0wNC0yMlQwNjozNTowNy4yNTMxMDY","previous_cursor":None}
```

### Publishing

This project is published on PyPi. 

To roll a new release, update the version in `pyproject.toml` and tag a new release. GitHub actions will handle the release to PyPI.

## License

This library is released under the [MIT License](LICENSE).
