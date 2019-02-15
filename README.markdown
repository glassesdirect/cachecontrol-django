# cachecontrol-django

A cache provider for [CacheControl](https://cachecontrol.readthedocs.io/) using Django's caching mechanism.

[![PyPI](https://img.shields.io/pypi/v/cachecontrol-django.svg)](https://pypi.org/project/cachecontrol-django/) ![](https://img.shields.io/pypi/pyversions/cachecontrol-django.svg) [![Build Status](https://img.shields.io/travis/com/glassesdirect/cachecontrol-django.svg)](https://travis-ci.com/glassesdirect/cachecontrol-django) [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

# Installation

```
pip install cachecontrol-django
```

# Usage

```python
import requests
from cachecontrol import CacheControl
from cachecontrol_django import DjangoCache

session = CacheControl(requests.session(), cache=DjangoCache())
session.get("https://www.glassesdirect.co.uk/")
```

## Working Around Key Length Errors

If you see errors about key length (such as "MemcachedKeyLengthError: Key length is > 250"), you can ask DjangoCache to hash the keys it uses by specifying a `key_hash_algorithm`:

```python
long_url = 'https://www.glassesdirect.co.uk/?q=' + ('x' * 250)
session = CacheControl(
    requests.session(),
    cache=DjangoCache(key_hash_algorithm='sha512')
)
session.get(long_url)
```

Note that when hashing these keys, there is a very small chance of a hash collision causing a request for one URL to return the content of another.
