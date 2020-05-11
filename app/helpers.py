from bson import ObjectId
from bson.errors import InvalidId
from pydantic import BaseModel, Field
from fastapi.openapi.utils import (
    validation_error_definition,
    validation_error_response_definition,
)
from fastapi.openapi.constants import REF_PREFIX

from starlette.exceptions import HTTPException
from starlette.requests import Request
from starlette.responses import JSONResponse
from fastapi.exceptions import RequestValidationError


class DocInfo:
    def __init__(self, descr='', summ='', res_descr='', status_code=200, resp_model=None, **kwargs):
        self.description = descr
        self.summary = summ
        self.response_description = res_descr
        self.status_code = status_code
        self.response_model = resp_model

        for key, val in kwargs.items():
            setattr(self, key, val)


class ObjectIdStr(str):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        try:
            ObjectId(str(v))
        except InvalidId:
            raise ValueError("Not a valid ObjectId")
        return str(v)


class PaginatedResult(BaseModel):
    next: int = Field(..., title='Next page (-1 if there is nowhere to paginate)')
    prev: int = Field(..., title='Previous page (-1 if there is nowhere to paginate)')
    total: int = Field(..., title='Total amount of results')


def http_error_handler(request: Request, exc: HTTPException) -> JSONResponse:
    err = {exc.status_code: exc.detail}
    return JSONResponse({"errors": [err]}, status_code=exc.status_code)


def handle_422(req: Request, exc: RequestValidationError):
    errs = {'errors': []}

    for err in exc.errors():
        err_field_name = err['loc'][-1]
        err_field_value = exc.body[err_field_name]
        errs['errors'].append({err_field_name: f"({err_field_value}) - {err['msg']}"})
    return JSONResponse(errs, status_code=422)


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