# DefinitionFieldFormat

## Example Usage

```python
from gr4vy.models import DefinitionFieldFormat

# Open enum: unrecognized values are captured as UnrecognizedStr
value: DefinitionFieldFormat = "text"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"text"`
- `"multiline"`
- `"number"`
- `"timezone"`
- `"boolean"`
