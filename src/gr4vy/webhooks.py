import hmac
import hashlib
import time
from typing import Optional

def verify_webhook(
    payload: str,
    secret: str,
    signature_header: Optional[str],
    timestamp_header: Optional[str],
    timestamp_tolerance: int
) -> None:
    """
    Verifies a webhook signature.

    :param payload: The payload that was sent in the webhook.
    :param secret: The secret that was used to sign the webhook.
    :param signature_header: The header that contains the signature.
    :param timestamp_header: The header that contains the timestamp.
    :param timestamp_tolerance: The tolerance for the timestamp in seconds.
    :raises ValueError: If the signature or timestamp is invalid.
    """
    if not signature_header or not timestamp_header:
        raise ValueError("Missing header values")

    try:
        timestamp = int(timestamp_header)
    except ValueError as exc:
        raise ValueError("Invalid header timestamp") from exc

    signatures = signature_header.split(",")
    expected_signature = hmac.new(
        secret.encode(),
        f"{timestamp}.{payload}".encode(),
        hashlib.sha256
    ).hexdigest()

    if expected_signature not in signatures:
        raise ValueError("No matching signature found")

    if timestamp_tolerance and timestamp < time.time() - timestamp_tolerance:
        raise ValueError("Timestamp too old")
