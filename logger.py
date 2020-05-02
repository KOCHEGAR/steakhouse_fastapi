import logging
import sys
import os
from functools import wraps
# from .exceptions import CashboxException
from logging.handlers import TimedRotatingFileHandler
FORMATTER = logging.Formatter("%(asctime)s — %(name)s — %(levelname)s — %(message)s")
LOGS_DIR = os.path.expanduser('~') + '/steakhouse_logs'

# Track logging filenames
log_filenames = []


# make logs dir
if not os.path.exists(LOGS_DIR):
    os.mkdir(LOGS_DIR)


def get_console_handler():
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(FORMATTER)
    return console_handler


def get_file_handler(filename):
    file_handler = TimedRotatingFileHandler(filename, when='D', interval=1, backupCount=10)
    file_handler.setFormatter(FORMATTER)
    return file_handler


def get_logger(filename, logger_name):
    logger = logging.getLogger(logger_name)

    if filename in log_filenames:
        return logger
    else:
        log_filenames.append(filename)

    logger.setLevel(logging.DEBUG)  # better to have too much log than not enough
    logger.addHandler(get_console_handler())
    logger.addHandler(get_file_handler(f'{LOGS_DIR}/{filename}'))
    # with this pattern, it's rarely necessary to propagate the error up to parent
    logger.propagate = False
    return logger


def logging_decorator(filename, logger_name, operation=''):
    def _logging_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            logger = get_logger(filename, logger_name)
            data_from_request = kwargs.get('valid_schema_data', '')

            log_msg = f"""
            ----------------------------------------------------
            ------> Начало исполнения операции "{operation}"
            ----------------------------------------------------
            """

            if data_from_request:
                log_msg += f'Данные с запроса: {data_from_request} \n' \
                           f'-------------------------------------'
            logger.info(log_msg)
            try:
                result = func(*args, **kwargs)
                logger.info(f"""
                Операция "{operation}" завершена
                """)
                return result
            except Exception as exc:

                msg = f'-> Возникло исключение! \n' \
                      f'-> Класс ошибки: {exc.__class__} \n' \
                      f'-> Имя класса ошибки: {exc.__class__.__name__} \n' \
                      f'-> Информация об ошибке: {exc} \n'

                logger.error(msg)

                raise
        return wrapper
    return _logging_decorator
