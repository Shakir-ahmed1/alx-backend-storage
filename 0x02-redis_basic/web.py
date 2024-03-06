import requests
import redis
import time
from functools import wraps

redis_client = redis.Redis()

def count_calls(method):
    @wraps(method)
    def wrapper(*args, **kwargs):
        url = kwargs.get('url')
        if url:
            key = f"count:{url}"
            redis_client.incr(key)
        return method(*args, **kwargs)
    return wrapper

def cache_with_expiry(expiration_time):
    def decorator(method):
        @wraps(method)
        def wrapper(*args, **kwargs):
            url = kwargs.get('url')
            if url:
                key = f"cache:{url}"
                cached_data = redis_client.get(key)
                if cached_data:
                    return cached_data.decode('utf-8')
                else:
                    response = method(*args, **kwargs)
                    redis_client.setex(key, expiration_time, response)
                    return response
            else:
                return method(*args, **kwargs)
        return wrapper
    return decorator

@count_calls
@cache_with_expiry(10)
def get_page(url: str) -> str:
    response = requests.get(f"http://slowwly.robertomurray.co.uk/delay/5000/url/{url}")
    return response.text

if __name__ == "__main__":
    url = "example.com"
    for i in range(5):
        print(get_page(url))
        time.sleep(2)  # Sleep for 2 seconds between each request
