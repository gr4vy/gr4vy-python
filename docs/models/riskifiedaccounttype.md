# RiskifiedAccountType

The customer account types recommended by Riskified.

## Example Usage

```python
from gr4vy.models import RiskifiedAccountType

# Open enum: unrecognized values are captured as UnrecognizedStr
value: RiskifiedAccountType = "guest"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"guest"`
- `"registered"`
- `"premium"`
- `"business"`
