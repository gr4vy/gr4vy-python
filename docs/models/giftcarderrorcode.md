# GiftCardErrorCode

Gift card error codes.

Gr4vy normalised gift card error codes. Keep the naming and style in line with
those in the connectors framework.

If new codes are added, append them at the end or amend public simulator
documentation: https://docs.gr4vy.com/guides/features/gift-cards/simulator

## Example Usage

```python
from gr4vy.models import GiftCardErrorCode

# Open enum: unrecognized values are captured as UnrecognizedStr
value: GiftCardErrorCode = "invalid_gift_card"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"invalid_gift_card"`
- `"expired_card"`
- `"inactive_card"`
- `"invalid_service_credentials"`
- `"invalid_amount"`
- `"incorrect_currency"`
- `"insufficient_funds"`
- `"invalid_service_configuration"`
- `"operation_canceled"`
- `"service_error"`
- `"service_network_error"`
- `"unknown_error"`
- `"max_gift_cards_reached"`
