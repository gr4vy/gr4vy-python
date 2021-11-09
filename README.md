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
in a secure location but in this code sample we simply read the file from disk.

```python
from gr4vy import Gr4vyClient
client = Gr4vyClient("gr4vyInstance","location_of_key_file")
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

token = client.GenerateEmbedToken(embed)
```

You can now pass this token to your frontend where it can be used to
authenticate Gr4vy Embed.

The `buyer_id` and/or `buyer_external_identifier` fields can be used to allow
the token to pull in previously stored payment methods for a user. A buyer
needs to be created before it can be used in this way.

```python
  from gr4vy import Gr4vyClient
  from gr4vy import BuyerRequest
  client = Gr4vyClient("spider","private_key.pem")

  buyer_request = BuyerRequest(display_name = "Jane Smith")

  new_buyer = client.AddBuyer(buyer_request)

  embed = {
    "amount": 1299,
    "currency": "USD",
    "buyerId": new_buyer.id,
  }

  embed_token = client.GenerateEmbedToken(embed)

  print("Embed token: {}".format(embed_token))
```

## Initialization

The client can be initialized with the Gr4vy ID (`gr4vyId`) and the location of the private key

```python
  client = Gr4vyClient("gr4vyId","private_key.pem")
```

Alternatively, instead of the `gr4vyId` it can be initialized with the `baseUrl`
of the server to use directly.

```python
  client = Gr4vyClientWithBaseUrl("https://*gr4vyId*.gr4vy.app","private_key.pem")
```

Your API private key can be created in your admin panel on the **Integrations**
tab.


## Making API calls

This library conveniently maps every API path to a seperate function. For
example, `GET /buyers?limit=100` would be:

```python
  client.ListBuyers(2)
```

To create, the API requires a request object for that resource that is conventiently
named `Gr4vy<Resource>Request`.  To update, the API requires a request object
for that resource that is named `Gr4vy<Resource>Update`.

For example, to create a buyer you will need to pass a `Gr4vyBuyerRequest` object to
the `AddBuyer` method.

```python
  from gr4vy import BuyerRequest

  buyer_request = BuyerRequest(display_name = "Jane Smith")
  new_buyer = client.AddBuyer(buyer_request)

```

So to update a buyer you will need to pass in the `Gr4vyBuyerUpdate` to the
`UpdateBuyer` method.

```python
  buyer_request = BuyerUpdate(display_name = "Jane Changed")
  buyer_update = client.UpdateBuyer(buyer_id, buyer_request)
```

## Response

Every resolved API call returns the requested resource, errors are printed to the console


```python
  print(client.ListBuyers())
```

## Logging & Debugging

The SDK makes it easy possible to log responses to the console.

```python
  print(client.ListBuyers())
```

This will output the request parameters and response to the console as follows.

```sh
{"items":[{"id":"b8433347-a16f-46b5-958f-d681876546a6","type":"buyer","display_name":"Jane Smith","external_identifier":None,"created_at":"2021-04-22T06:51:16.910297+00:00","updated_at":"2021-04-22T07:18:49.816242+00:00"}],"limit":1,"next_cursor":"fAA0YjY5NmU2My00NzY5LTQ2OGMtOTEyNC0xODVjMDdjZTY5MzEAMjAyMS0wNC0yMlQwNjozNTowNy4yNTMxMDY","previous_cursor":None}
```

## Development

### Adding new APIs

To add new APIs, run the following command to update the models and APIs based
on the API spec.

```sh
./openapi-generator-generate.sh
```

Run the tests to ensure the changes do not break any existing tests. Using PyTest. In test.py update the following lines with your gr4vy id and the location of the private key file


```python
gr4vy_id = "YOURGR4VYID"
private_key_location = "PRIVATE_KEY_LOCATION"
```

```sh
pytest -v
```

### Publishing

This project is published to PyPi.

## License

This library is released under the [MIT License](LICENSE).
