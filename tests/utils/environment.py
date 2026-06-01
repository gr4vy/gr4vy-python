"""Shared E2E harness.

Every test module provisions its OWN merchant account (random id) with a
``mock-card`` payment service, so modules are fully isolated and safe to run in
parallel across CI shards. The merchant-scoped client is wrapped with
:class:`JsonInterceptorClient` for forward-compat injection and endpoint-reach
tracking.
"""

import logging
import os
import secrets
from pathlib import Path
from typing import Optional

import httpx

from gr4vy import Gr4vy, auth

from utils.client import JsonInterceptorClient
from utils.merchant import TestMerchant

API_BASE_URL = "https://api.sandbox.e2e.gr4vy.app"

_logger = logging.getLogger("gr4vy")


def load_private_key() -> str:
    """Resolve the signing key: ``PRIVATE_KEY`` env var first, then ``private_key.pem``."""
    private_key = os.getenv("PRIVATE_KEY")
    if private_key:
        return private_key

    pem = Path(__file__).resolve().parents[2] / "private_key.pem"
    if pem.exists():
        return pem.read_text(encoding="utf-8")

    raise RuntimeError(
        "No signing key found: set PRIVATE_KEY or place private_key.pem in the repo root."
    )


def create_client(private_key: str, merchant_account_id: Optional[str] = None) -> Gr4vy:
    """Build a Gr4vy client with the forward-compat + HTTP-recording transport.

    Conservative timeouts make a stalled connection fail the test fast rather than
    hang a shard until the CI job-level timeout kills it.
    """
    base = httpx.Client(timeout=httpx.Timeout(30.0, connect=10.0))
    return Gr4vy(
        client=JsonInterceptorClient(base),
        server="sandbox",
        id="e2e",
        merchant_account_id=merchant_account_id,
        bearer_auth=auth.with_token(private_key=private_key),
        debug_logger=_logger,
    )


def setup_merchant() -> TestMerchant:
    """Provision an isolated merchant account + mock-card service.

    Call once per test module (see the ``merchant`` fixture in ``conftest.py``).
    """
    private_key = load_private_key()
    admin = create_client(private_key)

    merchant_account_id = secrets.token_hex(8)
    admin.merchant_accounts.create(
        id=merchant_account_id, display_name=merchant_account_id
    )

    client = create_client(private_key, merchant_account_id)
    client.payment_services.create(
        display_name="Payment service",
        payment_service_definition_id="mock-card",
        fields=[{"key": "merchant_id", "value": "test"}],
        accepted_currencies=["USD"],
        accepted_countries=["US"],
        active=True,
    )

    return TestMerchant(
        client=client,
        merchant_account_id=merchant_account_id,
        private_key=private_key,
    )
