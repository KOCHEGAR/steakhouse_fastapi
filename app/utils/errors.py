from fastapi.exceptions import RequestValidationError
from pymongo.errors import ServerSelectionTimeoutError
from starlette.exceptions import HTTPException
from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.status import HTTP_422_UNPROCESSABLE_ENTITY, HTTP_500_INTERNAL_SERVER_ERROR


def http_error_handler(request: Request, exc: HTTPException) -> JSONResponse:
    err = {exc.status_code: exc.detail}
    return JSONResponse({"errors": [exc.detail]}, status_code=exc.status_code)


def handle_db_connection_error(req: Request, exc: ServerSelectionTimeoutError):
    return JSONResponse({"errors": ['DB connection error']}, status_code=HTTP_500_INTERNAL_SERVER_ERROR)


def handle_422(req: Request, exc: RequestValidationError):
    errs = {'errors': []}

    print('errs ', exc.errors())
    print('err body ', exc.body)
    if not exc.body:
        errs['errors'].append('Request body is empty')
    else:
        for err in exc.errors():
            err_field_name = err['loc'][-1]
            err_field_value = exc.body.get(err_field_name, err_field_name)

            if err_field_name == err_field_value:
                errs['errors'].append(f"{err_field_name} - {err['msg']}")
            else:
                errs['errors'].append(f"{err_field_name}: ({err_field_value}) - {err['msg']}")
    return JSONResponse(errs, status_code=HTTP_422_UNPROCESSABLE_ENTITY)


class SteakhouseException(HTTPException):
    def __init__(self, err_str, code=400):
        self.status_code = code
        self.detail = err_str
