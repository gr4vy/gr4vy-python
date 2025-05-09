from joserfc import jwk, jwt
import pytest
# from freezegun import freeze_time
# from datetime import datetime, timedelta
from gr4vy.auth import get_embed_token, get_token, JWTScope, update_token
# from src.config import SDK_METADATA

private_key = """-----BEGIN PRIVATE KEY-----
MIHuAgEAMBAGByqGSM49AgEGBSuBBAAjBIHWMIHTAgEBBEIBABM9jQu+HT87oIik
O6DiJjYeghr3V+VMBVNU2hCM3X/OAS6TUTylMbnjDnwWdmu7anVSnjvEY1a4KxQ9
WZ8E/PKhgYkDgYYABABRdv5VAtOsGb6THxeK/p7RAARPm6Zwb7FF4sZAYkkSB7h0
2jpj3UHSpyl92BQkiF/xakz7hMMD1A0ZTn5SuXWp3AG9qPHO3eB9WrZhPGYixwyo
XNjhnPEDhmkItKXteke9iBOTOOXB7AFQSh7EXRBmhBs4u3ZlTmrl+8VdBc3+jwAY
rw==
-----END PRIVATE KEY-----"""

# thumbprint = "va-SLs5AxJNfqKXD8LI5Y38BflpNvjZjY4RSWz66U1w"

# embed_params = {
#     "amount": 9000,
#     "currency": "USD",
#     "buyerExternalIdentifier": "user-123",
#     "connectionOptions": {
#         "stripe-card": {
#             "stripe_connect": {
#                 "key": "value",
#             },
#         },
#     },
#     "metadata": {
#         "camelCaseKey": "value1",
#         "snake_case_key": "value2",
#     },
#     "cartItems": [
#         {
#             "name": "Joust Duffle Bag",
#             "quantity": 1,
#             "unitAmount": 9000,
#             "taxAmount": 0,
#             "categories": ["Gear", "Bags", "Test"],
#         },
#     ],
# }

# checkout_session_id = "0ebde6a1-f66c-43ea-bb8b-73751864c604"


@pytest.mark.asyncio
async def test_get_token_creates_valid_signed_jwt():
    token = await get_token(
        private_key=private_key,
        scopes=[JWTScope.READ_ALL, JWTScope.WRITE_ALL],
        expires_in=3600,
    )

    decoded = jwt.decode(token, private_key)

    assert decoded.claims["scopes"] == ["*.read", "*.write"]
    assert "iat" in decoded.claims
    assert "nbf" in decoded.claims
    assert "exp" in decoded.claims
    assert "iss" in decoded.claims
    assert decoded.claims["iss"].startswith("Gr4vy Python SDK")


# @pytest.mark.asyncio
# async def test_get_token_accepts_optional_embed_data():
#     token = await get_token(
#         private_key=private_key,
#         scopes=[JWTScope.Embed],
#         embed_params=embed_params,
#     )

#     decoded = jwt.decode(token, private_key, algorithms=["ES512"], options={"verify_signature": False})

#     conn_options = embed_params.get("connectionOptions", embed_params.get("connection_options"))
#     expected = snakecase_keys(embed_params, exclude=["metadata"])
#     expected["connection_options"] = conn_options

#     assert decoded["scopes"] == ["embed"]
#     assert decoded["embed"] == expected


# @pytest.mark.asyncio
# async def test_get_token_ignores_embed_data_without_embed_scope():
#     token = await get_token(
#         private_key=private_key,
#         scopes=[JWTScope.ReadAll],
#         embed_params=embed_params,
#     )

#     decoded = jwt.decode(token, private_key, algorithms=["ES512"], options={"verify_signature": False})

#     assert decoded["scopes"] == ["*.read"]
#     assert "embed" not in decoded


# @pytest.mark.asyncio
# async def test_get_embed_token_creates_jwt_for_embed():
#     token = await get_embed_token(
#         private_key=private_key,
#         embed_params=embed_params,
#     )

#     decoded = jwt.decode(token, private_key, algorithms=["ES512"], options={"verify_signature": False})

#     conn_options = embed_params.get("connectionOptions", embed_params.get("connection_options"))
#     expected = snakecase_keys(embed_params, exclude=["metadata"])
#     expected["connection_options"] = conn_options

#     assert decoded["scopes"] == ["embed"]
#     assert decoded["embed"] == expected


# @pytest.mark.asyncio
# async def test_get_embed_token_takes_optional_checkout_session_id():
#     token = await get_embed_token(
#         private_key=private_key,
#         embed_params=embed_params,
#         checkout_session_id=checkout_session_id,
#     )

#     decoded = jwt.decode(token, private_key, algorithms=["ES512"], options={"verify_signature": False})

#     assert decoded["checkout_session_id"] == checkout_session_id


# @pytest.mark.asyncio
# @freeze_time(datetime.utcnow())
# async def test_update_token_resigns_with_new_signature_and_expiration():
#     original_token = await get_token(private_key=private_key, expires_in="1m")

#     with freeze_time(datetime.utcnow() + timedelta(seconds=90)):
#         new_token = await update_token(
#             private_key=private_key,
#             token=original_token,
#             expires_in="1m",
#         )

#     original_decoded = jwt.decode(original_token, options={"verify_signature": False})
#     new_decoded = jwt.decode(new_token, options={"verify_signature": False})

#     assert new_decoded["scopes"] == original_decoded["scopes"]
#     assert new_decoded["iat"] > original_decoded["iat"]
#     assert new_decoded["exp"] > original_decoded["exp"]
#     assert new_decoded["nbf"] > original_decoded["nbf"]


# @pytest.mark.asyncio
# @freeze_time(datetime.utcnow())
# async def test_update_token_allows_embed_token_update_with_new_params():
#     original_token = await get_embed_token(
#         private_key=private_key,
#         embed_params=embed_params,
#         checkout_session_id=checkout_session_id,
#         expires_in="1m",
#     )

#     new_embed_params = {
#         "amount": 1299,
#         "currency": "USD",
#     }

#     with freeze_time(datetime.utcnow() + timedelta(seconds=90)):
#         new_token = await update_token(
#             private_key=private_key,
#             token=original_token,
#             expires_in="1m",
#             embed_params=new_embed_params,
#         )

#     original_decoded = jwt.decode(original_token, options={"verify_signature": False})
#     new_decoded = jwt.decode(new_token, options={"verify_signature": False})

#     assert new_decoded["embed"] == new_embed_params
#     assert new_decoded["checkout_session_id"] == original_decoded["checkout_session_id"]