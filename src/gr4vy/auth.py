import uuid
import enum
import base64
import textwrap
import json
from jose import jwk
from cryptography.hazmat.primitives import hashes, serialization
import jwt
from typing import Optional, Dict, Any, Union
from datetime import datetime, timedelta, timezone
from ._version import __user_agent__

class JWTScope(str, enum.Enum):
    READ_ALL = "*.read"
    WRITE_ALL = "*.write"
    EMBED = "embed"
    ANTI_FRAUD_SERVICE_DEFINITIONS_READ = "anti-fraud-service-definitions.read"
    ANTI_FRAUD_SERVICE_DEFINITIONS_WRITE = "anti-fraud-service-definitions.write"
    ANTI_FRAUD_SERVICES_READ = "anti-fraud-services.read"
    ANTI_FRAUD_SERVICES_WRITE = "anti-fraud-services.write"
    API_LOGS_READ = "api-logs.read"
    API_LOGS_WRITE = "api-logs.write"
    APPLE_PAY_CERTIFICATES_READ = "apple-pay-certificates.read"
    APPLE_PAY_CERTIFICATES_WRITE = "apple-pay-certificates.write"
    AUDIT_LOGS_READ = "audit-logs.read"
    AUDIT_LOGS_WRITE = "audit-logs.write"
    BUYERS_READ = "buyers.read"
    BUYERS_WRITE = "buyers.write"
    BUYERS_BILLING_DETAILS_READ = "buyers.billing-details.read"
    BUYERS_BILLING_DETAILS_WRITE = "buyers.billing-details.write"
    CARD_SCHEME_DEFINITIONS_READ = "card-scheme-definitions.read"
    CARD_SCHEME_DEFINITIONS_WRITE = "card-scheme-definitions.write"
    CHECKOUT_SESSIONS_READ = "checkout-sessions.read"
    CHECKOUT_SESSIONS_WRITE = "checkout-sessions.write"
    CONNECTIONS_READ = "connections.read"
    CONNECTIONS_WRITE = "connections.write"
    DIGITAL_WALLETS_READ = "digital-wallets.read"
    DIGITAL_WALLETS_WRITE = "digital-wallets.write"
    FLOWS_READ = "flows.read"
    FLOWS_WRITE = "flows.write"
    GIFT_CARD_SERVICE_DEFINITIONS_READ = "gift-card-service-definitions.read"
    GIFT_CARD_SERVICE_DEFINITIONS_WRITE = "gift-card-service-definitions.write"
    GIFT_CARD_SERVICES_READ = "gift-card-services.read"
    GIFT_CARD_SERVICES_WRITE = "gift-card-services.write"
    GIFT_CARDS_READ = "gift-cards.read"
    GIFT_CARDS_WRITE = "gift-cards.write"
    MERCHANT_ACCOUNTS_READ = "merchant-accounts.read"
    MERCHANT_ACCOUNTS_WRITE = "merchant-accounts.write"
    PAYMENT_LINKS_READ = "payment-links.read"
    PAYMENT_LINKS_WRITE = "payment-links.write"
    PAYMENT_METHOD_DEFINITIONS_READ = "payment-method-definitions.read"
    PAYMENT_METHOD_DEFINITIONS_WRITE = "payment-method-definitions.write"
    PAYMENT_METHODS_READ = "payment-methods.read"
    PAYMENT_METHODS_WRITE = "payment-methods.write"
    PAYMENT_OPTIONS_READ = "payment-options.read"
    PAYMENT_OPTIONS_WRITE = "payment-options.write"
    PAYMENT_SERVICE_DEFINITIONS_READ = "payment-service-definitions.read"
    PAYMENT_SERVICE_DEFINITIONS_WRITE = "payment-service-definitions.write"
    PAYMENT_SERVICES_READ = "payment-services.read"
    PAYMENT_SERVICES_WRITE = "payment-services.write"
    PAYOUTS_READ = "payouts.read"
    PAYOUTS_WRITE = "payouts.write"
    REPORTS_READ = "reports.read"
    REPORTS_WRITE = "reports.write"
    ROLES_READ = "roles.read"
    ROLES_WRITE = "roles.write"
    TRANSACTIONS_READ = "transactions.read"
    TRANSACTIONS_WRITE = "transactions.write"
    USERS_ME_READ = "users.me.read"
    USERS_ME_WRITE = "users.me.write"
    VAULT_FORWARD_READ = "vault-forward.read"
    VAULT_FORWARD_WRITE = "vault-forward.write"
    VAULT_FORWARD_AUTHENTICATIONS_READ = "vault-forward-authentications.read"
    VAULT_FORWARD_AUTHENTICATIONS_WRITE = "vault-forward-authentications.write"
    VAULT_FORWARD_CONFIGS_READ = "vault-forward-configs.read"
    VAULT_FORWARD_CONFIGS_WRITE = "vault-forward-configs.write"
    VAULT_FORWARD_DEFINITIONS_READ = "vault-forward-definitions.read"
    VAULT_FORWARD_DEFINITIONS_WRITE = "vault-forward-definitions.write"
    WEBHOOK_SUBSCRIPTIONS_READ = "webhook-subscriptions.read"
    WEBHOOK_SUBSCRIPTIONS_WRITE = "webhook-subscriptions.write"

JWTScopes = Union[list[JWTScope], list[str]]

def __b64e(value: bytes) -> str:
    return base64.urlsafe_b64encode(value).decode("utf8").strip("=")

def __thumbprint(private_key: str) -> str:
    private_key_pem = textwrap.dedent(private_key).encode()
    serialized_pem = serialization.load_pem_private_key(private_key_pem, password=None)
    key = jwk.construct(serialized_pem, algorithm="ES512").to_dict() # type: ignore
    claims = {k: v for k, v in key.items() if k in {"kty", "crv", "x", "y"}}
    json_claims = json.dumps(claims, separators=(",", ":"), sort_keys=True)
    digest = hashes.Hash(hashes.SHA256())
    digest.update(json_claims.encode("utf8"))
    return str(__b64e(digest.finalize()))

def with_token(private_key: str, scopes: Optional[JWTScopes] = None, expires_in: int = 3600):
    """Generates a new token for every API request.

    Args:
        private_key (str): The RSA private key in string-PEM format.
        scopes (Optional[JWTScopes], optional): List of scopes. If not set, all access will be set as default
        expires_in (int, optional): The expiration time in seconds. Defaults to 3600.
    """
    def callback() -> str:
        return get_token(private_key, scopes, expires_in)
    return callback

def get_token(
    private_key: str,
    scopes: Optional[JWTScopes] = None,
    expires_in: int = 3600,
    embed_params: Optional[Dict[str, Any]] = None,
    checkout_session_id: Optional[str] = None,
) -> str:
    """Generates a token for an API request.

    Args:
        private_key (str): The RSA private key in string-PEM format.
        scopes (Optional[JWTScopes], optional): List of scopes. If not set, all access will be set as default
        expires_in (int, optional): The expiration time in seconds. Defaults to 3600.
        embed_params (Optional[Dict[str, Any]], optional): An optional list of Embed params to pin. Defaults to None.
        checkout_session_id (Optional[str], optional): An optional checkout session ID to link the transaction to. Defaults to None.

    Returns:
        str: A bearer auth token
    """
    if not scopes:
        scopes = [JWTScope.READ_ALL, JWTScope.WRITE_ALL]

    claims: Dict[str, Any] = {
        "scopes": scopes,
        "iss": __user_agent__,
        "iat": datetime.now(tz=timezone.utc),
        "nbf": datetime.now(tz=timezone.utc),
        "exp": datetime.now(tz=timezone.utc) + timedelta(seconds=expires_in),
        "jti": str(uuid.uuid4()),
    }

    if checkout_session_id:
        claims["checkout_session_id"] = checkout_session_id

    if JWTScope.EMBED in scopes and embed_params:
        claims["embed"] = embed_params

    token = jwt.encode(claims, private_key, algorithm="ES512", headers={"kid": __thumbprint(private_key)})
    return token

def update_token(
    token: str,
    private_key: str,
    scopes: Optional[JWTScopes] = None,
    expires_in: int = 3600,
    embed_params: Optional[Dict[str, Any]] = None,
    checkout_session_id: Optional[str] = None,
) -> str:
    """Updates an existing token with a new signature, and optionally new data.

    Args:
        token (str): The previously generated token.
        private_key (str): The RSA private key in string-PEM format.
        scopes (Optional[JWTScopes], optional): List of scopes. If not set, all access will be set as default
        expires_in (int, optional): The expiration time in seconds. Defaults to 3600.
        embed_params (Optional[Dict[str, Any]], optional): An optional list of Embed params to pin. Defaults to None.
        checkout_session_id (Optional[str], optional): An optional checkout session ID to link the transaction to. Defaults to None.

    Returns:
        str: A bearer auth token
    """
    claims: Dict[str, Any] = jwt.decode(token, private_key, algorithms=["ES512"], options={"verify_signature": False})
    previous_scopes: JWTScopes = claims.get("scopes") or []

    return get_token(
        private_key,
        scopes or previous_scopes,
        expires_in,
        embed_params or claims.get("embed"),
        checkout_session_id or claims.get("checkout_session_id"),
    )


def get_embed_token(
    private_key: str,
    embed_params: Optional[Dict[str, Any]] = None,
    checkout_session_id: Optional[str] = None,
) -> str:
    """Generates a token for use with Embed.

    Args:
        private_key (str): The RSA private key in string-PEM format.
        embed_params (Optional[Dict[str, Any]], optional): An optional list of Embed params to pin. Defaults to None.
        checkout_session_id (Optional[str], optional): An optional checkout session ID to link the transaction to. Defaults to None.

    Returns:
        str: A bearer auth token
    """
    return get_token(
        private_key,
        scopes=[JWTScope.EMBED],
        expires_in=3600,
        embed_params=embed_params,
        checkout_session_id=checkout_session_id,
    )
