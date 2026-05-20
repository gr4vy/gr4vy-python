# Source

The platform that the Paze session is being created for. Defaults to `web`.

## Example Usage

```python
from gr4vy.models import Source

# Open enum: unrecognized values are captured as UnrecognizedStr
value: Source = "web"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"web"`
- `"mobile"`
