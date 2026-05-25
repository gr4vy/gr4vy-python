# Intent

Primary intent of the checkout session.

## Example Usage

```python
from gr4vy.models import Intent

# Open enum: unrecognized values are captured as UnrecognizedStr
value: Intent = "REVIEW_AND_PAY"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"REVIEW_AND_PAY"`
- `"EXPRESS_CHECKOUT"`
- `"ADD_CARD"`
