# PazeSessionCompleteRequestTransactiontype

The type of transaction being completed. PURCHASE for a one-off checkout, CARD_ON_FILE to retain the card for future use, or BOTH.

## Example Usage

```python
from gr4vy.models import PazeSessionCompleteRequestTransactiontype

# Open enum: unrecognized values are captured as UnrecognizedStr
value: PazeSessionCompleteRequestTransactiontype = "PURCHASE"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"PURCHASE"`
- `"CARD_ON_FILE"`
- `"BOTH"`
