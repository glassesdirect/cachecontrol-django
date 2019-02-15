"""A cache provider for CacheControl using Django's caching mechanism."""

import hashlib
from base64 import b64encode

from cachecontrol.cache import BaseCache
from django.core.cache import cache


class DjangoCache(BaseCache):
    """A cache provider for CacheControl using Django's caching mechanism."""

    def __init__(self, key_hash_algorithm=None):
        self.hash_algorithm = key_hash_algorithm

    def prepare_key(self, key):
        """Prepare cache key."""
        if self.hash_algorithm:
            hashy = hashlib.new(self.hash_algorithm)
            hashy.update(key.encode("utf-8"))
            key = b64encode(hashy.digest())

        return key

    def get(self, key):
        return cache.get(self.prepare_key(key))

    def set(self, key, value):
        cache.set(self.prepare_key(key), value)

    def delete(self, key):
        cache.delete(self.prepare_key(key))
