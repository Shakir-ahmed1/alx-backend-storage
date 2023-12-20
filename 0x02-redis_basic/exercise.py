#!/usr/bin/env python3
""" writing strings to redis """
import redis
import uuid
from typing import Union, Callable, Any


class Cache:
    """ a Cache that has a store """
    def __init__(self):
        """ initializes the cache"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ stores the data in Redis """
        id = str(uuid.uuid4())
        self._redis.set(id, data)
        return id

    def get(self, key: str, fn: Union[Callable, None] =None) -> Any:
        """ gets the desired element"""
        a = self._redis.get(key)
        if a is None or fn is None:
            return a
        else:
            value = fn(a)
            return value

    def get_str(self, key: str) -> str:
        """ gets the desired element"""
        a = self._redis.get(key)
        return str(a)

    def get_int(self, key: str) -> int:
        """ gets the desired element"""
        a = self._redis.get(key)
        return int(a)

cache = Cache()

TEST_CASES = {
    b"foo": None,
    123: int,
    "bar": lambda d: d.decode("utf-8")
}

for value, fn in TEST_CASES.items():
    key = cache.store(value)
    assert cache.get(key, fn=fn) == value
