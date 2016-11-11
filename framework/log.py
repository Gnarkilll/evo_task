import os
import logging.config
from functools import wraps


base_path = os.path.dirname(__file__)
if not os.path.exists('test_report'):
    os.makedirs('test_report')
logging.config.fileConfig(base_path + '/logging.conf')
logger = logging.getLogger('UI_TESTS')


def log(function):

    @wraps(function)
    def wrapped(*args, **kwargs):
        try:
            logger.info("{0} --> {1} {2}".format(function.__name__, ['{}'.format(arg) for arg in args], kwargs))
        except RuntimeError:
            logger.warning("{0}".format(function.__name__))
        try:
            return function(*args, **kwargs)
        except Exception as exception:
            logger.warning('{0} raised exception: {1}'.format(function.__name__, exception.message))
            raise exception
    return wrapped
