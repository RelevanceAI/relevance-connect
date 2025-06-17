# The Json schema of the inputs

All inputs have the following fields:
- input_name: str. The variable name of the input. This is the reference name of the input in the code.
- type: str. The type of the input.
- title: str. The title of the input.
- description: str. The description of the input.
- default: any. The default value of the input.
- required: bool. Whether the input is required.

## Text Input
```json
{
    "name": "text",
    "type": "string",
    "description": "A text input",
    "default": "Hello, world!"
}
```

## API Key Input
This is a special type of input that is used to store API keys. It is not shown to the user. This requires the additional metadata field of `is_fixed_param` to be set to true and `content_type` to be set to `api_key`.
```json
{
    "name": "api_key",
    "type": "string",
    "description": "An API key input",
    "metadata": {
        "content_type": "api_key",
        "is_fixed_param": true
    }
}
```

## Long Text Input
This is a special type of input that is used to store long text. This requires the additional field of `metadata.content_type` to be set to `long_text`.
```json
{
    "name": "long_text",
    "type": "string",
    "description": "A long text input",
    "metadata": {
        "content_type": "long_text",
    }
}
```

## Number Input

```json
{
    "name": "number",
    "type": "number",
    "description": "A number input",
    "min": 0
}
```

## Text List Input
This is a special type of input that is used to store a list of text. This requires the additional field of `items.type` to be set to `string`.
```json
{
    "name": "text_list",
    "type": "array",
    "description": "A text list input",
    "items": {
        "type": "string"
    }
}
```

## JSON Input
This is a special type of input that is used to store JSON objects. This has the additional field of `properties` which is the json schema of the object.
```json 
{
    "name": "json",
    "type": "object",
    "description": "A JSON input",
    "default": {},
    "properties": {
        "data": {
            "type": "object"
        }
    }
}
```

## JSON List Input
This is a special type of input that is used to store a list of JSON objects. This requires the additional field of `items.type` to be set to `object`.
```json
{
    "name": "json_list",
    "type": "array",
    "description": "A JSON list input",
    "items": {
        "type": "object",
    }
}
```

## Options Input
This is a special type of input that is used to store a list of options. This requires the additional field of `enum` to be set to the list of options.
```json
{
    "name": "options",
    "type": "string",
    "description": "A options input",
    "enum": ["Yes", "No"]
}
```

## File URL Input
This is a special type of input that is used to store file URLs, the frontend is a file uploader. This requires the additional metadata field of `content_type` to be set to `file_url`.
```json
{
    "name": "file_url",
    "type": "string",
    "description": "A file URL input",
    "metadata": {
        "content_type": "file_url",
        "accepted_file_types": ["pdf", "docx", "txt"]
    }
}
```