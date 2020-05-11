from fastapi.exceptions import RequestValidationError, HTTPException

from starlette.requests import Request
from starlette.responses import JSONResponse


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
