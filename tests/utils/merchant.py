"""Merchant-scoped client plus the identifiers a suite may need."""

from dataclasses import dataclass

from gr4vy import Gr4vy


@dataclass(frozen=True)
class TestMerchant:
    """A merchant-scoped Gr4vy client and the identifiers used to build it."""

    client: Gr4vy
    merchant_account_id: str
    private_key: str
