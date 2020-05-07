
from starlette.config import Config
from os import path
from marshmallow import Schema, fields
# from marshmallow.exceptions import ValidationError
from logger import logging_decorator


@logging_decorator('config_build.log', 'manage_config', 'create_config')
def manage_config():
    class EnvConfig(Schema):
        DEPARTMENT_NUMBER = fields.Int(required=True)
        PAYGATE_URL = fields.URL(required=True)
        MONGO_DBNAME = fields.Str(required=True)
        MONGO_USER = fields.Str(required=True)
        MONGO_HOST = fields.Str(required=True)
        MONGO_PORT = fields.Int(required=True)
        MONGO_PASSWORD = fields.Str(required=True)
        REDIS_HOSTNAME = fields.Str(required=True)
        REDIS_BACKEND = fields.Str(required=True)
        CELERY_BROKER_URL = fields.Str(required=True)
        CELERY_RESULT_BACKEND = fields.Str(required=True)
        TIMEZONE = fields.Str(required=True)
        APP_SECRET_KEY = fields.Str(required=True)
        JWT_SECRET_KEY = fields.Str(required=True)

    if not path.exists(path.abspath('.env')):
        raise RuntimeError('.env file must be created and filled with information')
    data, errs = EnvConfig().load(Config('.env').file_values)
    if errs:
        raise RuntimeError(f'Errors during reading config file. Errors: {errs}')
    return data
    # return EnvConfig().load(Config('.env').file_values)


config = manage_config()
