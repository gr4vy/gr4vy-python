# Mode

## Example Usage

```python
from gr4vy.models import Mode

# Open enum: unrecognized values are captured as UnrecognizedStr
value: Mode = "card"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"card"`
- `"redirect"`
- `"applepay"`
- `"googlepay"`
- `"checkout-session"`
- `"click-to-pay"`
- `"gift-card"`
- `"bank"`
- `"paze"`
