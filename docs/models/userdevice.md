# UserDevice

The platform that is being used to access the website.

## Example Usage

```python
from gr4vy.models import UserDevice

# Open enum: unrecognized values are captured as UnrecognizedStr
value: UserDevice = "desktop"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"desktop"`
- `"mobile"`
