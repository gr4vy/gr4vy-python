# PaymentLinkIntent

## Example Usage

```python
from gr4vy.models import PaymentLinkIntent

# Open enum: unrecognized values are captured as UnrecognizedStr
value: PaymentLinkIntent = "authorize"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"authorize"`
- `"capture"`
- `"prefer_authorize"`
