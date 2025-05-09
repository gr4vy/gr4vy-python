import os
import secrets
from typing import Optional
from pathlib import Path
from gr4vy import Gr4vy, auth

def load_private_key() -> str:
    """
    Loads the private key from an environment variable or a file.
    """
    private_key = os.getenv("PRIVATE_KEY")

    if not private_key:
        filename = Path(__file__).resolve().parent / "../../private_key.pem"
        with open(filename, "r", encoding="utf-8") as file:
            private_key = file.read()

    return private_key


def create_gr4vy_client(private_key: str, merchant_account_id: Optional[str] = None) -> Gr4vy:
    """
    Creates a Gr4vy client instance.
    """
    return Gr4vy(
        server="sandbox",
        id="e2e",
        merchant_account_id=merchant_account_id,
        bearer_auth=auth.with_token(private_key=private_key),
    )


def setup_environment() -> Gr4vy:
    """
    Sets up the test environment by creating a merchant account and payment service.
    """
    # Load the private key
    private_key = load_private_key()

    # Create an admin client
    admin_client = create_gr4vy_client(private_key)

    # Generate a random merchant account ID
    merchant_account_id = secrets.token_hex(8)

    # Create a merchant account
    merchant_account = admin_client.merchant_accounts.create(
        id=merchant_account_id,
        display_name=merchant_account_id,
    )

    # Create a merchant client for the new merchant account
    merchant_client = create_gr4vy_client(private_key, merchant_account.id)

    # Setup a payment service
    merchant_client.payment_services.create(
        accepted_countries=["US"],
        accepted_currencies=["USD"],
        display_name="Payment service",
        payment_service_definition_id="mock-card",
        fields=[{"key": "merchant_id", "value": "test"}],
    )

    return merchant_client


def cleanup_environment() -> None:
    """
    Cleans up the test environment. Currently a no-op.
    """
