"""
Logics for work with MEXC FUTURES API
"""

__all__ = ['ping']

import atexit

import requests
from requests.exceptions import HTTPError, ConnectionError, Timeout, RequestException

from logger_conf import setup_logger

logger = setup_logger()

session = requests.Session()
logger.debug('mexc futures - session open')


class FuturesApiPath:
    """
    The class stores paths to API Endpoints
    """
    BASE = "https://api.mexc.com"
    PING = "/api/v3/ping"


def handle_exceptions(exception):
    """
    Handle exceptions raised by this function. Using for handle frequently used exceptions.
    :param exception:
    :return:
    """
    if isinstance(exception, HTTPError):
        logger.debug(f"HTTP error: {exception} (status code: {getattr(exception.response, 'status_code', None)})")
    elif isinstance(exception, ConnectionError):
        logger.debug(f"Connection error: {exception}")
    elif isinstance(exception, Timeout):
        logger.debug(f"Timeout error: {exception}")
    elif isinstance(exception, RequestException):
        logger.debug(f"Common request error: {exception}")


def ping() -> bool:
    """
    Ping Futures API. Returns True if API responds to a ping request.
    :return:
    """
    url = f'{FuturesApiPath.BASE}{FuturesApiPath.PING}'
    logger.debug(url)
    result = False
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
    except (HTTPError, ConnectionError, Timeout, RequestException) as e:
        handle_exceptions(e)
    else:
        result = True

    return result


def close_session():
    session.close()
    logger.debug('mexc futures - session closed')


atexit.register(close_session)
