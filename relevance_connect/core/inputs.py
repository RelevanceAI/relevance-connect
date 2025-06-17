class InputBase:
    def __init__(self, input_name, type, title:str, description:str, default=None, required:bool=True):
        self.input_name = input_name
        self.type = type
        self.description = description
        self.required = required
        self.json = {
            input_name: {
                "type": type,
                "title": title,
                "description": description,
                "frontend_metadata" : {
                    "required": required
                }
            }
        }
        if default:
            self.default = default
            self.json[input_name]["default"] = default
    
    def to_json(self):
        return self.json

class TextInput(InputBase):
    def __init__(self, input_name, title:str, description:str, default=None, required:bool=True):
        super().__init__(input_name, "string", title, description, default, required)

class LongTextInput(InputBase):
    def __init__(self, input_name, title:str, description:str, default=None, required:bool=True):
        super().__init__(input_name, "string", title, description, default, required)
        self.json[name]["frontend_metadata"]["content_type"] = "long_text"

class OptionsInput(InputBase):
    def __init__(self, input_name, title:str, options:list[str], description:str, default=None, required:bool=True):
        super().__init__(input_name, "string", title, description, default, required)
        self.json[name]["frontend_metadata"]["options"] = options

class NumberInput(InputBase):
    def __init__(self, input_name, title:str, description:str, default=None, required:bool=True):
        super().__init__(input_name, "number", title, description, default, required)

class ApiKeyInput(InputBase):
    def __init__(self, input_name, title:str, description:str, default=None, required:bool=True):
        super().__init__(input_name, "string", title, description, default, required)
        self.json[input_name]["frontend_metadata"]["content_type"] = "api_key"
        self.json[input_name]["frontend_metadata"]["is_fixed_param"] = True
        del self.json[input_name]["frontend_metadata"]["required"]
