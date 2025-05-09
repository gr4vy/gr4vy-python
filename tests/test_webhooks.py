import pytest
from gr4vy.webhooks import verify_webhook

def test_verify_webhook_signature():
    secret = "Ik4L-8FH0ihWczctcIPXZRR_8F0fPNgmhEfVBbZ3zNwqQVa1Or4tBz4Pgw2eNaVDod7H56Y268h_wohEUaWbUg"
    signature_header = "78aca0c78005107a654a957b8566fa6e0e5e06aea92d7da72a6da9e5a690d013,other"
    timestamp_header = "1744018920"
    payload = "payload"
    timestamp_tolerance = 0  # no timestamp validation

    # Should not raise any exceptions
    verify_webhook(payload, secret, signature_header, timestamp_header, timestamp_tolerance)


def test_verify_webhook_old_timestamp():
    secret = "Ik4L-8FH0ihWczctcIPXZRR_8F0fPNgmhEfVBbZ3zNwqQVa1Or4tBz4Pgw2eNaVDod7H56Y268h_wohEUaWbUg"
    signature_header = "78aca0c78005107a654a957b8566fa6e0e5e06aea92d7da72a6da9e5a690d013,other"
    timestamp_header = "1744018920"
    payload = "payload"
    timestamp_tolerance = 60  # 1 minute tolerance

    with pytest.raises(ValueError, match="Timestamp too old"):
        verify_webhook(payload, secret, signature_header, timestamp_header, timestamp_tolerance)


def test_verify_webhook_wrong_signature():
    secret = "Ik4L-8FH0ihWczctcIPXZRR_8F0fPNgmhEfVBbZ3zNwqQVa1Or4tBz4Pgw2eNaVDod7H56Y268h_wohEUaWbUg"
    signature_header = "other"
    timestamp_header = "1744018920"
    payload = "payload"
    timestamp_tolerance = 0  # no timestamp validation

    with pytest.raises(ValueError, match="No matching signature found"):
        verify_webhook(payload, secret, signature_header, timestamp_header, timestamp_tolerance)


def test_verify_webhook_invalid_timestamp():
    secret = "Ik4L-8FH0ihWczctcIPXZRR_8F0fPNgmhEfVBbZ3zNwqQVa1Or4tBz4Pgw2eNaVDod7H56Y268h_wohEUaWbUg"
    signature_header = "78aca0c78005107a654a957b8566fa6e0e5e06aea92d7da72a6da9e5a690d013,other"
    timestamp_header = "wrong"
    payload = "payload"
    timestamp_tolerance = 0  # no timestamp validation

    with pytest.raises(ValueError, match="Invalid header timestamp"):
        verify_webhook(payload, secret, signature_header, timestamp_header, timestamp_tolerance)


def test_verify_webhook_missing_signature_header():
    secret = "Ik4L-8FH0ihWczctcIPXZRR_8F0fPNgmhEfVBbZ3zNwqQVa1Or4tBz4Pgw2eNaVDod7H56Y268h_wohEUaWbUg"
    signature_header = None
    timestamp_header = "1744018920"
    payload = "payload"
    timestamp_tolerance = 0  # no timestamp validation

    with pytest.raises(ValueError, match="Missing header values"):
        verify_webhook(payload, secret, signature_header, timestamp_header, timestamp_tolerance)


def test_verify_webhook_missing_timestamp_header():
    secret = "Ik4L-8FH0ihWczctcIPXZRR_8F0fPNgmhEfVBbZ3zNwqQVa1Or4tBz4Pgw2eNaVDod7H56Y268h_wohEUaWbUg"
    signature_header = "78aca0c78005107a654a957b8566fa6e0e5e06aea92d7da72a6da9e5a690d013,other"
    timestamp_header = None
    payload = "payload"
    timestamp_tolerance = 0  # no timestamp validation

    with pytest.raises(ValueError, match="Missing header values"):
        verify_webhook(payload, secret, signature_header, timestamp_header, timestamp_tolerance)
