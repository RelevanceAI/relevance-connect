import requests
from relevance_connect.core.auth import Auth

def handle_response(response):
    try:
        return response.json()
    except:
        return response.text

class RelevanceCode:
    def __init__(
        self,
        code: str,
        name: str,
        requirements: list[str],
        description: str = "",
        inputs={},
        code_type: str = "python",
        long_output_mode: bool = False,
        timeout: int = 300,
        id: str = None,
        auth: Auth = None,
    ):
        """
        :param name: name of the integration
        :param description: description of the integration
        :param inputs: inputs of the integration
        :param id: id of the integration
        :param auth: auth object
        """
        self.code = code
        self.name = name
        self.description = description
        self._inputs = inputs
        self.steps = []
        # generate random id if none provided
        self.random_id = False
        if id is None:
            import uuid
            id = str(uuid.uuid4())
            self.random_id = True
        self.id = id
        self.code_type = code_type
        self.long_output_mode = long_output_mode
        self.timeout = timeout
        self.auth: Auth = config.auth if auth is None else auth

    def _add_steps(self):
        if code_type == "python":
            step_json = {
                "transformation": "python_code_transformation",
                "name": self.name,
                "params": {
                    "code": self.code,
                    "packages": self.requirements,
                }
            }
            if self.long_output_mode:
                step_json["params"]["long_output_mode"] = self.long_output_mode
            if self.timeout:
                step_json["params"]["timeout"] = self.timeout
            self.steps.append(step_json)

    def _trigger_json(
        self, values: dict = {}, return_state: bool = True, public: bool = False
    ):
        data = {
            "return_state": return_state,
            "studio_override": {
                "public": public,
                "transformations": {
                    "steps": self._transform_steps(self.steps)
                },
                "params_schema": {
                    "properties": self._inputs
                },
            },
            "params": values,
        }
        data["studio_id"] = self.id
        data["studio_override"]["studio_id"] = self.id
        return data

    def tool_json(self):
        data = {
            "title": self.name,
            "description": self.description,
            "version": "latest",
            "project": self.auth.project,
            "public": False,
            "state_mapping" : {
                "text" : "params.text"
            },
            "params_schema": {
                "properties": self._inputs
            },
            "transformations": {
                "steps": self._transform_steps(self.steps)
            },
        }
        data["studio_id"] = self.id
        return data

    def run(self, inputs={}, full_response: bool = False):
        url = f"{self.auth.url}/latest/studios/{self.auth.project}"
        response = requests.post(
            f"{url}/trigger",
            json=self._trigger_json(inputs),
            headers=self.auth.headers,
        )
        res = handle_response(response)
        if isinstance(res, dict):
            if ("errors" in res and res["errors"]) or full_response:
                return res
            elif "output" in res:
                return res["output"]
        return res


    def save(self):
        url = f"{self.auth.url}/latest/studios"
        response = requests.post(
            f"{url}/bulk_update",
            json={"updates": [self.tool_json()]},
            headers=self.auth.headers,
        )
        res = handle_response(response)
        print("Tool deployed successfully to id ", self.id)
        return self.id