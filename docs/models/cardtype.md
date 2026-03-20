# CardType

## Example Usage

```python
from gr4vy.models import CardType

# Open enum: unrecognized values are captured as UnrecognizedStr
value: CardType = "credit"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"credit"`
- `"debit"`
- `"prepaid"`
