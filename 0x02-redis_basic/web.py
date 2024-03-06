#!/usr/bin/env python3
""" A module that implement expiring web cache """

import redis
import requests
from typing import Callable
from functools import wraps

redis = redis.Redis()


def wrap_requests(func: Callable) -> Callable:
    """ decorator wrapper """

    @wraps(func)
    def wrapper(url):
        """ wrapper for decorator """
        redis.incr(f"count:{url}")
        cached_response = redis.get(f"cached:{url}")
        if cached_response:
            return cached_response.decode('utf-8')
        result = func(url)
        redis.setex(f"cached:{url}", 10, result)
        return result

    return wrapper


@wrap_requests
def get_page(url: str) -> str:
    """get page using url """
    response = requests.get(url)
    return response.text