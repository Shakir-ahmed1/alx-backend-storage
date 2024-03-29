#!/usr/bin/env python3
""" writing strings to redis """
import redis
import uuid
from typing import Union, Callable, Any
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """ a decorator that adds functionality to a functin """
    key = method.__qualname__
    @wraps(method)
    def wrapper_function(self: Any, *args: Any, **kwargs: Any) -> Any:
        """ a wrapped function that increments the key """
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper_function


def call_history(method: Callable) -> Callable:
    """ a decorator that stores the history of inputs and outputs """
    input_key = method.__qualname__ + ":inputs"
    output_key = method.__qualname__ + ":outputs"
    @wraps(method)
    def wrapper_function(self: Any, *args: Any, **kwargs: Any) -> Any:
        """ a wrapped function that stores the input and output lists """
        self._redis.rpush(input_key, str(args))
        output = method(self, *args, **kwargs)
        self._redis.rpush(output_key, output)
        return output
    return wrapper_function


class Cache:
    """ a Cache that has a store """
    def __init__(self):
        """ initializes the cache"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ stores the data in Redis """
        id = str(uuid.uuid4())
        self._redis.set(id, data)
        return id

    def get(self, key: str, fn: Union[Callable, None] = None) -> Any:
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


def replay(method):
    """ replays history """
    rd = redis.Redis()
    qname = method.__qualname__
    outputs = rd.lrange(qname+':outputs', 0, -1)
    inputs = rd.lrange(qname+':inputs', 0, -1)
    print(f'{qname} was called {len(inputs)} times:')
    for a in zip(inputs, outputs):
        print(f"Cache.store(*{a[0].decode()}) -> {a[1].decode()}")
