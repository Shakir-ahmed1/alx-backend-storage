#!/usr/bin/env python3
""" writing strings to redis """
import redis
import uuid
from typing import Union


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
