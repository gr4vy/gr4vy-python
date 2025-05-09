# CheckoutSessions
(*checkout_sessions*)

## Overview

### Available Operations

* [create](#create) - Create checkout session
* [get](#get) - Get checkout session
* [update](#update) - Update checkout session
* [delete](#delete) - Delete checkout session

## create

Create a new checkout session.

### Example Usage

```python
from datetime import date
from gr4vy import Gr4vy, models
from gr4vy.utils import parse_datetime
import os


with Gr4vy(
    bearer_auth=os.getenv("GR4VY_BEARER_AUTH", ""),
) as g_client:

    res = g_client.checkout_sessions.create(request_body=models.CheckoutSessionUpdate(
        cart_items=[
            models.CartItem(
                name="GoPro HD",
                quantity=2,
                unit_amount=1299,
                discount_amount=0,
                tax_amount=0,
                external_identifier="goprohd",
                sku="GPHD1078",
                product_url="https://example.com/catalog/go-pro-hd",
                image_url="https://example.com/images/go-pro-hd.jpg",
                categories=[
                    "camera",
                    "travel",
                    "gear",
                ],
                product_type=models.ProductType.PHYSICAL,
                seller_country="GB",
            ),
        ],
        metadata={
            "cohort": "cohort-a",
            "order_id": "order-12345",
        },
        buyer=models.GuestBuyerInput(
            display_name="John Doe",
            external_identifier="buyer-12345",
            billing_details=models.BillingDetailsInput(
                first_name="John",
                last_name="Doe",
                email_address="john@example.com",
                phone_number="+1234567890",
                address=models.Address(
                    city="San Jose",
                    country="US",
                    postal_code="94560",
                    state="California",
                    state_code="US-CA",
                    house_number_or_name="10",
                    line1="Stafford Appartments",
                    line2="29th Street",
                    organization="Gr4vy",
                ),
                tax_id=models.TaxID(
                    value="12345678931",
                    kind=models.TaxIDKind.ID_NIK,
                ),
            ),
            shipping_details=models.ShippingDetailsCreate(
                first_name="John",
                last_name="Doe",
                email_address="john@example.com",
                phone_number="+1234567890",
                address=models.Address(
                    city="San Jose",
                    country="US",
                    postal_code="94560",
                    state="California",
                    state_code="US-CA",
                    house_number_or_name="10",
                    line1="Stafford Appartments",
                    line2="29th Street",
                    organization="Gr4vy",
                ),
            ),
        ),
        airline=models.Airline(
            booking_code="X36Q9C",
            issued_address="123 Broadway, New York",
            issued_at=parse_datetime("2013-07-16T19:23:00.000+00:00"),
            issuing_carrier_code="A3",
            legs=[
                models.AirlineLeg(
                    arrival_airport="LAX",
                    arrival_at=parse_datetime("2013-07-16T19:23:00.000+00:00"),
                    arrival_city="Los Angeles",
                    arrival_country="US",
                    carrier_code="BA",
                    coupon_number="15885566",
                    departure_airport="LHR",
                    departure_at=parse_datetime("2013-07-16T19:23:00.000+00:00"),
                    departure_city="London",
                    departure_country="GB",
                    departure_tax_amount=1200,
                    fare_amount=129900,
                    fare_basis_code="FY",
                    fee_amount=1200,
                    flight_class="E",
                    flight_number="101",
                    route_type=models.RouteType.ROUND_TRIP,
                    stop_over=False,
                    tax_amount=1200,
                ),
            ],
            passenger_name_record="JOHN L",
            passengers=[
                models.AirlinePassenger(
                    age_group=models.AgeGroup.ADULT,
                    date_of_birth=date.fromisoformat("2013-07-16"),
                    email_address="john@example.com",
                    first_name="John",
                    frequent_flyer_number="15885566",
                    last_name="Luhn",
                    passport_number="11117700225",
                    phone_number="+1234567890",
                    ticket_number="BA1236699999",
                    title="Mr.",
                    country_code="US",
                ),
            ],
            reservation_system="Amadeus",
            restricted_ticket=False,
            ticket_delivery_method=models.TicketDeliveryMethod.ELECTRONIC,
            ticket_number="123-1234-151555",
            travel_agency_code="12345",
            travel_agency_invoice_number="EG15555155",
            travel_agency_name="ACME Agency",
            travel_agency_plan_name="B733",
        ),
        expires_in=3600,
    ))

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                       | Type                                                                                            | Required                                                                                        | Description                                                                                     |
| ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| `timeout_in_seconds`                                                                            | *Optional[float]*                                                                               | :heavy_minus_sign:                                                                              | N/A                                                                                             |
| `merchant_account_id`                                                                           | *OptionalNullable[str]*                                                                         | :heavy_minus_sign:                                                                              | The ID of the merchant account to use for this request.                                         |
| `request_body`                                                                                  | [OptionalNullable[models.CreateCheckoutSessionBody]](../../models/createcheckoutsessionbody.md) | :heavy_minus_sign:                                                                              | N/A                                                                                             |
| `retries`                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                | :heavy_minus_sign:                                                                              | Configuration to override the default retry behavior of the client.                             |

### Response

**[models.CheckoutSession](../../models/checkoutsession.md)**

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
| `timeout_in_seconds`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |                                                                     |
| `merchant_account_id`                                               | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | The ID of the merchant account to use for this request.             |                                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.CheckoutSession](../../models/checkoutsession.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| errors.Error400          | 400                      | application/json         |
| errors.Error401          | 401                      | application/json         |
| errors.Error403          | 403                      | application/json         |
| errors.Error403Forbidden | 403                      | application/json         |
| errors.Error403Active    | 403                      | application/json         |
| errors.Error404          | 404                      | application/json         |
| errors.Error405          | 405                      | application/json         |
| errors.Error409          | 409                      | application/json         |
| errors.Error425          | 425                      | application/json         |
| errors.Error429          | 429                      | application/json         |
| errors.Error500          | 500                      | application/json         |
| errors.Error502          | 502                      | application/json         |
| errors.Error504          | 504                      | application/json         |
| errors.APIError          | 4XX, 5XX                 | \*/\*                    |

## update

Update the information stored on a checkout session.

### Example Usage

```python
from datetime import date
from gr4vy import Gr4vy, models
from gr4vy.utils import parse_datetime
import os


with Gr4vy(
    bearer_auth=os.getenv("GR4VY_BEARER_AUTH", ""),
) as g_client:

    res = g_client.checkout_sessions.update(session_id="4137b1cf-39ac-42a8-bad6-1c680d5dab6b", cart_items=[
        {
            "name": "GoPro HD",
            "quantity": 2,
            "unit_amount": 1299,
            "discount_amount": 0,
            "tax_amount": 0,
            "external_identifier": "goprohd",
            "sku": "GPHD1078",
            "product_url": "https://example.com/catalog/go-pro-hd",
            "image_url": "https://example.com/images/go-pro-hd.jpg",
            "categories": [
                "camera",
                "travel",
                "gear",
            ],
            "product_type": models.ProductType.PHYSICAL,
            "seller_country": "GB",
        },
        {
            "name": "GoPro HD",
            "quantity": 2,
            "unit_amount": 1299,
            "discount_amount": 0,
            "tax_amount": 0,
            "external_identifier": "goprohd",
            "sku": "GPHD1078",
            "product_url": "https://example.com/catalog/go-pro-hd",
            "image_url": "https://example.com/images/go-pro-hd.jpg",
            "categories": [
                "camera",
                "travel",
                "gear",
            ],
            "product_type": models.ProductType.PHYSICAL,
            "seller_country": "GB",
        },
        {
            "name": "GoPro HD",
            "quantity": 2,
            "unit_amount": 1299,
            "discount_amount": 0,
            "tax_amount": 0,
            "external_identifier": "goprohd",
            "sku": "GPHD1078",
            "product_url": "https://example.com/catalog/go-pro-hd",
            "image_url": "https://example.com/images/go-pro-hd.jpg",
            "categories": [
                "camera",
                "travel",
                "gear",
            ],
            "product_type": models.ProductType.PHYSICAL,
            "seller_country": "US",
        },
    ], metadata={
        "cohort": "cohort-a",
        "order_id": "order-12345",
    }, buyer=models.GuestBuyerInput(
        display_name="John Doe",
        external_identifier="buyer-12345",
        billing_details=models.BillingDetailsInput(
            first_name="John",
            last_name="Doe",
            email_address="john@example.com",
            phone_number="+1234567890",
            address=models.Address(
                city="San Jose",
                country="US",
                postal_code="94560",
                state="California",
                state_code="US-CA",
                house_number_or_name="10",
                line1="Stafford Appartments",
                line2="29th Street",
                organization="Gr4vy",
            ),
            tax_id=models.TaxID(
                value="12345678931",
                kind=models.TaxIDKind.MY_NRIC,
            ),
        ),
        shipping_details=models.ShippingDetailsCreate(
            first_name="John",
            last_name="Doe",
            email_address="john@example.com",
            phone_number="+1234567890",
            address=models.Address(
                city="San Jose",
                country="US",
                postal_code="94560",
                state="California",
                state_code="US-CA",
                house_number_or_name="10",
                line1="Stafford Appartments",
                line2="29th Street",
                organization="Gr4vy",
            ),
        ),
    ), airline={
        "booking_code": "X36Q9C",
        "issued_address": "123 Broadway, New York",
        "issued_at": parse_datetime("2013-07-16T19:23:00.000+00:00"),
        "issuing_carrier_code": "A3",
        "legs": [
            {
                "arrival_airport": "LAX",
                "arrival_at": parse_datetime("2013-07-16T19:23:00.000+00:00"),
                "arrival_city": "Los Angeles",
                "arrival_country": "US",
                "carrier_code": "BA",
                "coupon_number": "15885566",
                "departure_airport": "LHR",
                "departure_at": parse_datetime("2013-07-16T19:23:00.000+00:00"),
                "departure_city": "London",
                "departure_country": "GB",
                "departure_tax_amount": 1200,
                "fare_amount": 129900,
                "fare_basis_code": "FY",
                "fee_amount": 1200,
                "flight_class": "E",
                "flight_number": "101",
                "route_type": models.RouteType.ROUND_TRIP,
                "stop_over": False,
                "tax_amount": 1200,
            },
            {
                "arrival_airport": "LAX",
                "arrival_at": parse_datetime("2013-07-16T19:23:00.000+00:00"),
                "arrival_city": "Los Angeles",
                "arrival_country": "US",
                "carrier_code": "BA",
                "coupon_number": "15885566",
                "departure_airport": "LHR",
                "departure_at": parse_datetime("2013-07-16T19:23:00.000+00:00"),
                "departure_city": "London",
                "departure_country": "GB",
                "departure_tax_amount": 1200,
                "fare_amount": 129900,
                "fare_basis_code": "FY",
                "fee_amount": 1200,
                "flight_class": "E",
                "flight_number": "101",
                "route_type": models.RouteType.ROUND_TRIP,
                "stop_over": False,
                "tax_amount": 1200,
            },
        ],
        "passenger_name_record": "JOHN L",
        "passengers": [
            {
                "age_group": models.AgeGroup.ADULT,
                "date_of_birth": date.fromisoformat("2013-07-16"),
                "email_address": "john@example.com",
                "first_name": "John",
                "frequent_flyer_number": "15885566",
                "last_name": "Luhn",
                "passport_number": "11117700225",
                "phone_number": "+1234567890",
                "ticket_number": "BA1236699999",
                "title": "Mr.",
                "country_code": "US",
            },
            {
                "age_group": models.AgeGroup.ADULT,
                "date_of_birth": date.fromisoformat("2013-07-16"),
                "email_address": "john@example.com",
                "first_name": "John",
                "frequent_flyer_number": "15885566",
                "last_name": "Luhn",
                "passport_number": "11117700225",
                "phone_number": "+1234567890",
                "ticket_number": "BA1236699999",
                "title": "Mr.",
                "country_code": "US",
            },
            {
                "age_group": models.AgeGroup.ADULT,
                "date_of_birth": date.fromisoformat("2013-07-16"),
                "email_address": "john@example.com",
                "first_name": "John",
                "frequent_flyer_number": "15885566",
                "last_name": "Luhn",
                "passport_number": "11117700225",
                "phone_number": "+1234567890",
                "ticket_number": "BA1236699999",
                "title": "Mr.",
                "country_code": "US",
            },
        ],
        "reservation_system": "Amadeus",
        "restricted_ticket": False,
        "ticket_delivery_method": models.TicketDeliveryMethod.ELECTRONIC,
        "ticket_number": "123-1234-151555",
        "travel_agency_code": "12345",
        "travel_agency_invoice_number": "EG15555155",
        "travel_agency_name": "ACME Agency",
        "travel_agency_plan_name": "B733",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                           | Type                                                                                                                                                                | Required                                                                                                                                                            | Description                                                                                                                                                         | Example                                                                                                                                                             |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `session_id`                                                                                                                                                        | *str*                                                                                                                                                               | :heavy_check_mark:                                                                                                                                                  | The ID of the checkout session.                                                                                                                                     | 4137b1cf-39ac-42a8-bad6-1c680d5dab6b                                                                                                                                |
| `timeout_in_seconds`                                                                                                                                                | *Optional[float]*                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                  | N/A                                                                                                                                                                 |                                                                                                                                                                     |
| `merchant_account_id`                                                                                                                                               | *OptionalNullable[str]*                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                  | The ID of the merchant account to use for this request.                                                                                                             |                                                                                                                                                                     |
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
| `timeout_in_seconds`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |                                                                     |
| `merchant_account_id`                                               | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | The ID of the merchant account to use for this request.             |                                                                     |
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