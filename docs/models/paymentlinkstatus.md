# PaymentLinkStatus

## Example Usage

```python
from gr4vy.models import PaymentLinkStatus

# Open enum: unrecognized values are captured as UnrecognizedStr
value: PaymentLinkStatus = "active"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"active"`
- `"completed"`
- `"expired"`
- `"processing"`
