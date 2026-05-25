# TransactionType

## Example Usage

```python
from gr4vy.models import TransactionType

# Open enum: unrecognized values are captured as UnrecognizedStr
value: TransactionType = "PURCHASE"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"PURCHASE"`
- `"CARD_ON_FILE"`
- `"BOTH"`
