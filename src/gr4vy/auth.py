# import uuid
# import enum
# from typing import List, Optional, Dict, Any
# from datetime import datetime, timedelta, timezone

# from joserfc import jwk, jwt


# class EmbedParams:
#     def __init__(
#         self,
#         amount: int,
#         currency: str,
#         buyer_id: Optional[str] = None,
#         buyer_external_identifier: Optional[str] = None,
#         metadata: Optional[Dict[str, str]] = None,
#         cart_items: Optional[List[Dict[str, Any]]] = None,
#         merchant_account_id: Optional[str] = None,
#         connection_options: Optional[Dict[str, Any]] = None,
#     ):
#         self.amount = amount
#         self.currency = currency
#         self.buyer_id = buyer_id
#         self.buyer_external_identifier = buyer_external_identifier
#         self.metadata = metadata
#         self.cart_items = cart_items
#         self.merchant_account_id = merchant_account_id
#         self.connection_options = connection_options


# class JWTScope(enum.StrEnum):
#     READ_ALL = "*.read"
#     WRITE_ALL = "*.write"
#     EMBED = "embed"
#     ANTI_FRAUD_SERVICE_DEFINITIONS_READ = "anti-fraud-service-definitions.read"
#     ANTI_FRAUD_SERVICE_DEFINITIONS_WRITE = "anti-fraud-service-definitions.write"
#     ANTI_FRAUD_SERVICES_READ = "anti-fraud-services.read"
#     ANTI_FRAUD_SERVICES_WRITE = "anti-fraud-services.write"
#     AUDIT_LOGS_READ = "audit-logs.read"
#     BUYERS_READ = "buyers.read"
#     BUYERS_WRITE = "buyers.write"
#     BUYERS_BILLING_DETAILS_READ = "buyers.billing-details.read"
#     BUYERS_BILLING_DETAILS_WRITE = "buyers.billing-details.write"
#     CARD_SCHEME_DEFINITIONS_READ = "card-scheme-definitions.read"
#     CHECKOUT_SESSIONS_READ = "checkout-sessions.read"
#     CHECKOUT_SESSIONS_WRITE = "checkout-sessions.write"
#     CONNECTIONS_READ = "connections.read"
#     CONNECTIONS_WRITE = "connections.write"
#     DIGITAL_WALLETS_READ = "digital-wallets.read"
#     DIGITAL_WALLETS_WRITE = "digital-wallets.write"
#     FLOWS_READ = "flows.read"
#     FLOWS_WRITE = "flows.write"
#     GIFT_CARD_SERVICE_DEFINITIONS_READ = "gift-card-service-definitions.read"
#     GIFT_CARD_SERVICES_READ = "gift-card-services.read"
#     GIFT_CARD_SERVICES_WRITE = "gift-card-services.write"
#     GIFT_CARDS_READ = "gift-cards.read"
#     GIFT_CARDS_WRITE = "gift-cards.write"
#     MERCHANT_ACCOUNT_READ = "merchant-accounts.reads"
#     MERCHANT_ACCOUNT_WRITE = "merchant-accounts.write"
#     PAYMENT_METHOD_DEFINITIONS_READ = "payment-method-definitions.read"
#     PAYMENT_METHOD_READ = "payment-methods.read"
#     PAYMENT_METHOD_WRITE = "payment-methods.write"
#     PAYMENT_OPTIONS_READ = "payment-options.read"
#     PAYMENT_SERVICE_DEFINITIONS_READ = "payment-service-definitions.read"
#     PAYMENT_SERVICES_READ = "payment-services.read"
#     PAYMENT_SERVICES_WRITE = "payment-services.write"
#     REPORTS_READ = "reports.read"
#     REPORTS_WRITE = "reports.write"
#     TRANSACTIONS_READ = "transactions.read"
#     TRANSACTIONS_WRITE = "transactions.write"
#     VAULT_FORWARD_WRITE = "vault-forward.write"


# type JWTScopes = list[JWTScope] | list[str]


# def with_token(private_key: str, scopes: Optional[JWTScopes] = None, expires_in: int = 3600):
#     if not private_key:
#         raise ValueError("Private key is null, undefined or empty")

#     if not scopes:
#         scopes = [JWTScope.READ_ALL, JWTScope.WRITE_ALL]

#     async def generate_token():
#         return get_token(private_key, scopes, expires_in)

#     return generate_token()


# def get_token(
#     private_key: str,
#     scopes: Optional[JWTScopes] = None,
#     expires_in: int = 3600,
#     embed_params: Optional[EmbedParams] = None,
#     checkout_session_id: Optional[str] = None,
# ) -> str:
#     if not scopes:
#         scopes = [JWTScope.READ_ALL, JWTScope.WRITE_ALL]

#     key = jwk.RSAKey.import_key(private_key)

#     # key_id = key.thumbprint()
#     claims = {
#         "scopes": scopes,
#         "iss": "Gr4vy Python SDK",
#         "nbf": datetime.now(tz=timezone.utc),
#         "exp": datetime.now(tz=timezone.utc) + timedelta(expires_in),
#         "jti": str(uuid.uuid4()),
#     }

#     if checkout_session_id:
#         claims["checkout_session_id"] = checkout_session_id

#     if JWTScope.EMBED in scopes and embed_params:
#         claims["embed"] = embed_params

#     headers = {
#         "alg": "ES512",
#         # "kid": "1234",
#     }

#     return jwt.encode(
#         headers,
#         claims,
#         key,
#         algorithms=["ES512"]
#     )


# async def update_token(
#     token: str,
#     private_key: str,
#     scopes: Optional[JWTScopes] = None,
#     expires_in: int = 3600,
#     embed_params: Optional[EmbedParams] = None,
#     checkout_session_id: Optional[str] = None,
# ) -> str:
#     decoded_token = jwt.decode(token, private_key, algorithms=["ES512"])
#     claims: Dict[str, Any] = decoded_token.claims
#     previous_scopes: JWTScopes = claims.get("scopes") or []

#     return get_token(
#         private_key,
#         scopes or previous_scopes,
#         expires_in,
#         embed_params or claims.get("embed"),
#         checkout_session_id or claims.get("checkout_session_id"),
#     )


# async def get_embed_token(
#     private_key: str,
#     embed_params: Optional[EmbedParams] = None,
#     checkout_session_id: Optional[str] = None,
# ) -> str:
#     return get_token(
#         private_key,
#         scopes=[JWTScope.EMBED],
#         expires_in=3600,
#         embed_params=embed_params,
#         checkout_session_id=checkout_session_id,
#     )
