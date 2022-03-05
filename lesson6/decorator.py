from functools import wraps
import inspect
import sys
import os
sys.path.append(os.path.join(os.getcwd(), '..'))
from logs.config_client_log import LOGGER


def log(func):
    @wraps(func)
    def call(*args, **kwargs):
        res = func(*args, **kwargs)
        LOGGER.debug('Function {} was called from {}'.format(func.__name__, inspect.stack()[1][3]))
        LOGGER.debug('Function {}({}, {}), return {}'.format(func.__name__, args, kwargs, res))
        return res
    return call