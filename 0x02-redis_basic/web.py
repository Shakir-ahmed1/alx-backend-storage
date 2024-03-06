#!/usr/bin/env python3
""" implementation of web caching with expiry """
import redis
import requests
from functools import wraps

r = redis.Redis()


def url_access_count(func):
    """decorator for get_page function"""
    @wraps(func)
    def wrapper(url):
        """wrapper function"""

        key = url
        cached_value = r.get(key)
        key_count = "count:{" + url + "}"
        if cached_value:
            print("using chached")
            r.incr(key_count)
            return cached_value.decode("utf-8")
        html_content = func(url)

        r.set(key_count, 1, ex=10)
        r.set(key, html_content, ex=10)
        return html_content
    return wrapper


@url_access_count
def get_page(url: str) -> str:
    """ gets the page"""
    results = requests.get(url)
    return results.text


# if __name__ == "__main__":
#     get_page('http://google.com')
#     get_page('http://google.com')
#     get_page('http://google.com')
#     get_page('http://google.com')
