from fastapi.openapi.constants import REF_PREFIX
from fastapi.openapi.utils import validation_error_definition, validation_error_response_definition

validation_error_definition["properties"] = {
    "field": {"title": "Error field", "type": "string"}
}

validation_error_response_definition["properties"] = {
    "errors": {
        "title": "Errors",
        "type": "array",
        "items": {"$ref": REF_PREFIX + "ValidationError", "type": "string"},
    }
}


class DocInfo:
    def __init__(self, descr='', summ='', res_descr='', status_code=200, resp_model=None, **kwargs):
        self.description = descr
        self.summary = summ
        self.response_description = res_descr
        self.status_code = status_code
        self.response_model = resp_model

        for key, val in kwargs.items():
            setattr(self, key, val)
