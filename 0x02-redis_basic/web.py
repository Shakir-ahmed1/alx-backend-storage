import requests
import redis
import time
from typing import Callable

redis_client = redis.Redis(host='localhost', port=6379, db=0)

def get_page(url: str) -> str:
    """Fetches the HTML content of a URL and caches it with expiration time of 10 seconds. """
    cached_content = redis_client.get(url)
    if cached_content:
        return cached_content.decode('utf-8')

    response = requests.get(url)
    html_content = response.text
    redis_client.setex(url, 10, html_content)
    count_key = f"count:{url}"
    redis_client.incr(count_key)

    return html_content

def cache_and_track(func: Callable) -> Callable:
    """Decorator for caching and tracking the number of times a URL is accessed."""
    def wrapper(url: str) -> str:
        """Wrapper function for caching and tracking."""
        # Check if the URL content is cached
        cached_content = redis_client.get(url)
        if cached_content:
            return cached_content.decode('utf-8')
        html_content = func(url)
        redis_client.setex(url, 10, html_content)
        count_key = f"count:{url}"
        redis_client.incr(count_key)

        return html_content
    return wrapper

@cache_and_track
def get_page_cached(url: str) -> str:
    """Fetches the HTML content of a URL, caching it with an expiration time of 10 seconds. """
    response = requests.get(url)
    return response.text

if __name__ == "__main__":
    url = "http://slowwly.robertomurray.co.uk/delay/1000/url/https://www.example.com"
    
    start_time = time.time()
    html_content = get_page(url)

    start_time = time.time()
    html_content_cached = get_page_cached(url)
