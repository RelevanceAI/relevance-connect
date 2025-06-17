# The Json schema of the inputs

All inputs have the following fields:
- input_name: str.
- type: str.
- title: str.
- description: str
- default: str.
- required: bool.

## Text Input
```json
{
    "name": "text",
    "type": "string",
    "description": "A text input",
    "default": "Hello, world!"
}
```
