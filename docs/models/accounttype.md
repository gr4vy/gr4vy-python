# AccountType

Specify whether this is a `checking` or `savings` account

## Example Usage

```python
from gr4vy.models import AccountType

# Open enum: unrecognized values are captured as UnrecognizedStr
value: AccountType = "checking"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"checking"`
- `"savings"`
