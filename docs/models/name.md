# Name

The specific event name.

## Example Usage

```python
from gr4vy.models import Name

# Open enum: unrecognized values are captured as UnrecognizedStr
value: Name = "transaction-updated-status"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"transaction-updated-status"`
- `"transaction-sync-event"`
- `"transaction-sync-failed-event"`
- `"transaction-modified-event"`
- `"transaction-api-request"`
- `"transaction-api-response"`
- `"bin-lookup-request"`
- `"three-d-secure-success"`
- `"three-d-secure-request-error"`
- `"three-d-secure-preparation-request"`
- `"three-d-secure-authentication-request"`
- `"three-d-secure-result-request"`
- `"anti-fraud-decision"`
- `"anti-fraud-decision-error"`
- `"anti-fraud-decision-skipped"`
- `"anti-fraud-webhook"`
- `"anti-fraud-transaction-status-update"`
- `"anti-fraud-transaction-status-update-error"`
- `"anti-fraud-decision-update"`
- `"anti-fraud-decision-update-error"`
- `"gift-card-redemption-succeeded"`
- `"gift-card-redemption-failed"`
- `"gift-card-refund-succeeded"`
- `"gift-card-refund-failed"`
- `"gift-card-reversal-succeeded"`
- `"payment-connector-response-transaction-authorization-succeeded"`
- `"payment-connector-response-transaction-capture-succeeded"`
- `"payment-connector-response-transaction-authorization-failed"`
- `"payment-connector-response-transaction-declined"`
- `"payment-connector-response-transaction-capture-failed"`
- `"payment-connector-response-transaction-capture-declined"`
- `"payment-connector-response-transaction-cancel-succeeded"`
- `"payment-connector-response-transaction-cancel-pending"`
- `"payment-connector-response-transaction-cancel-failed"`
- `"payment-connector-response-transaction-void-succeeded"`
- `"payment-connector-response-transaction-void-declined"`
- `"payment-connector-response-transaction-void-failed"`
- `"payment-connector-external-transaction-request"`
- `"payment-connector-report-transaction-settled"`
- `"payment-connector-report-chargeback-posted"`
- `"payment-connector-report-chargeback-reversal-posted"`
- `"payment-connector-transaction-webhook-processed"`
- `"digital-wallet-apple-pay-token-decrypted"`
- `"digital-wallet-google-pay-token-decrypted"`
- `"digital-wallet-click-to-pay-token-decrypted"`
- `"network-token-provision-succeeded"`
- `"network-token-provision-failed"`
- `"network-token-cryptogram-provision-succeeded"`
- `"network-token-cryptogram-provision-failed"`
- `"the-giving-block-transaction-conversion-succeeded"`
- `"real-time-account-update"`
- `"plaid-request-event"`
