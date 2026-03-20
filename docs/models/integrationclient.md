# IntegrationClient

## Example Usage

```python
from gr4vy.models import IntegrationClient

# Open enum: unrecognized values are captured as UnrecognizedStr
value: IntegrationClient = "redirect"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"redirect"`
- `"web"`
- `"android"`
- `"ios"`
