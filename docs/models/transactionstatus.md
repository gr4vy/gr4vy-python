# TransactionStatus

## Example Usage

```python
from gr4vy.models import TransactionStatus

# Open enum: unrecognized values are captured as UnrecognizedStr
value: TransactionStatus = "processing"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"processing"`
- `"authorization_succeeded"`
- `"authorization_declined"`
- `"authorization_failed"`
- `"authorization_voided"`
- `"authorization_void_pending"`
- `"capture_succeeded"`
- `"capture_pending"`
- `"buyer_approval_pending"`
