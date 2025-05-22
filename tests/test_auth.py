from freezegun import freeze_time
from datetime import datetime, timedelta, UTC
import jwt
from gr4vy.auth import get_token, get_embed_token, update_token, with_token, JWTScope
from gr4vy._version import __user_agent__

PRIVATE_KEY = """-----BEGIN PRIVATE KEY-----
MIHuAgEAMBAGByqGSM49AgEGBSuBBAAjBIHWMIHTAgEBBEIBABM9jQu+HT87oIik
O6DiJjYeghr3V+VMBVNU2hCM3X/OAS6TUTylMbnjDnwWdmu7anVSnjvEY1a4KxQ9
WZ8E/PKhgYkDgYYABABRdv5VAtOsGb6THxeK/p7RAARPm6Zwb7FF4sZAYkkSB7h0
2jpj3UHSpyl92BQkiF/xakz7hMMD1A0ZTn5SuXWp3AG9qPHO3eB9WrZhPGYixwyo
XNjhnPEDhmkItKXteke9iBOTOOXB7AFQSh7EXRBmhBs4u3ZlTmrl+8VdBc3+jwAY
rw==
-----END PRIVATE KEY-----"""


EMBED_PARAMS = {
    "amount": 9000,
    "currency": "USD",
    "buyer_external_identifier": "user-123",
    "connection_options": {
        "stripe-card": {
            "stripe_connect": {
                "key": "value",
            },
        },
    },
    "metadata": {
        "camelCaseKey": "value1",
        "snake_case_key": "value2",
    },
    "cart_items": [
       {
            "name": "Joust Duffle Bag",
            "quantity": 1,
            "unit_amount": 9000,
            "tax_amount": 0,
            "categories": ["Gear", "Bags", "Test"],
       },
    ],
}

CHECKOUT_SESSION_ID = "0ebde6a1-f66c-43ea-bb8b-73751864c604"


def test_get_token_creates_valid_signed_jwt():
    token = get_token(
        PRIVATE_KEY,
        scopes=[JWTScope.READ_ALL, JWTScope.WRITE_ALL],
        expires_in=3600,
    )

    claims = jwt.decode(token, PRIVATE_KEY, algorithms=["ES512"])

    assert claims["scopes"] == ["*.read", "*.write"]
    assert "iat" in claims
    assert "nbf" in claims
    assert "exp" in claims
    assert "iss" in claims
    assert claims["iss"] == __user_agent__


def test_get_token_accepts_optional_embed_data():
    token = get_token(
        private_key=PRIVATE_KEY,
        scopes=[JWTScope.EMBED],
        embed_params=EMBED_PARAMS,
    )

    decoded = jwt.decode(token, PRIVATE_KEY, algorithms=["ES512"])

    assert decoded["scopes"] == ["embed"]
    assert decoded["embed"] == EMBED_PARAMS


def test_get_token_ignores_embed_data_without_embed_scope():
    token = get_token(
        private_key=PRIVATE_KEY,
        scopes=[JWTScope.READ_ALL],
        embed_params=EMBED_PARAMS,
    )

    decoded = jwt.decode(token, PRIVATE_KEY, algorithms=["ES512"])

    assert decoded["scopes"] == ["*.read"]
    assert "embed" not in decoded


def test_get_embed_token_creates_jwt_for_embed():
    token = get_embed_token(
        private_key=PRIVATE_KEY,
        embed_params=EMBED_PARAMS,
    )

    decoded = jwt.decode(token, PRIVATE_KEY, algorithms=["ES512"])

    assert decoded["scopes"] == ["embed"]
    assert decoded["embed"] == EMBED_PARAMS


def test_get_embed_token_takes_optional_checkout_session_id():
    token = get_embed_token(
        private_key=PRIVATE_KEY,
        embed_params=EMBED_PARAMS,
        checkout_session_id=CHECKOUT_SESSION_ID,
    )

    decoded = jwt.decode(token, PRIVATE_KEY, algorithms=["ES512"])

    assert decoded["checkout_session_id"] == CHECKOUT_SESSION_ID


@freeze_time(datetime.now(UTC))
def test_update_token_resigns_with_new_signature_and_expiration():
    original_token = get_token(private_key=PRIVATE_KEY, expires_in=60)

    with freeze_time(datetime.now(UTC) + timedelta(seconds=90)):
        new_token = update_token(
            private_key=PRIVATE_KEY,
            token=original_token,
            expires_in=60,
        )

    original_decoded = jwt.decode(original_token, PRIVATE_KEY, algorithms=["ES512"], options={"verify_signature": False})
    new_decoded = jwt.decode(new_token, PRIVATE_KEY, algorithms=["ES512"], options={"verify_signature": False})

    assert new_decoded["scopes"] == original_decoded["scopes"]
    assert new_decoded["iat"] > original_decoded["iat"]
    assert new_decoded["exp"] > original_decoded["exp"]
    assert new_decoded["nbf"] > original_decoded["nbf"]


# @pytest.mark.asyncio
@freeze_time(datetime.now(UTC))
def test_update_token_allows_embed_token_update_with_new_params():
    original_token = get_embed_token(
        private_key=PRIVATE_KEY,
        embed_params=EMBED_PARAMS,
        checkout_session_id=CHECKOUT_SESSION_ID,
    )

    new_embed_params = {
        "amount": 1299,
        "currency": "USD",
    }

    with freeze_time(datetime.now(UTC) + timedelta(seconds=90)):
        new_token = update_token(
            private_key=PRIVATE_KEY,
            token=original_token,
            embed_params=new_embed_params,
        )

    original_decoded = jwt.decode(original_token, PRIVATE_KEY, algorithms=["ES512"], options={"verify_signature": False})
    new_decoded = jwt.decode(new_token, PRIVATE_KEY, algorithms=["ES512"], options={"verify_signature": False})

    assert new_decoded["embed"] == new_embed_params
    assert new_decoded["checkout_session_id"] == original_decoded["checkout_session_id"]

def test_with_token():
    promise = with_token(
        private_key=PRIVATE_KEY,
    )

    token1 = promise()
    token2 = promise()

    assert token1 != token2
