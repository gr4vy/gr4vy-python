# PaymentMethodStatus

## Example Usage

```python
from gr4vy.models import PaymentMethodStatus

# Open enum: unrecognized values are captured as UnrecognizedStr
value: PaymentMethodStatus = "processing"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"processing"`
- `"buyer_approval_required"`
- `"succeeded"`
- `"failed"`
- `"paused"`
