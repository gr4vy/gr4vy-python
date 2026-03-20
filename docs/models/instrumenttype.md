# InstrumentType

## Example Usage

```python
from gr4vy.models import InstrumentType

# Open enum: unrecognized values are captured as UnrecognizedStr
value: InstrumentType = "pan"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"pan"`
- `"card_token"`
- `"redirect"`
- `"redirect_token"`
- `"googlepay"`
- `"applepay"`
- `"network_token"`
- `"plaid"`
- `"bank"`
