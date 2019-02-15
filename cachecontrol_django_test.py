"""Tests for cachecontrol-django."""

# pylint: disable=redefined-outer-name

import pytest

from cachecontrol_django import DjangoCache


@pytest.fixture
def django_cache(mocker):
    """Mock Django cache."""
    return mocker.patch("cachecontrol_django.cache")


@pytest.fixture
def prepare_key(mocker):
    """Mock prepare_key."""
    prepare_key = mocker.patch.object(DjangoCache, "prepare_key")
    prepare_key.return_value = "prepared key"
    return prepare_key


def test_prepare_key():
    """Test prepare_key."""
    normal_cache = DjangoCache()
    hashing_cache = DjangoCache(key_hash_algorithm="sha512")
    previous_hashed_keys = []
    for key in ["abc", "", "x" * 300]:
        assert normal_cache.prepare_key(key) == key
        hashed_key = hashing_cache.prepare_key(key)
        assert hashed_key != key
        assert hashed_key not in previous_hashed_keys
        previous_hashed_keys.append(hashed_key)


def test_set(django_cache, prepare_key):
    """Test set."""
    cache = DjangoCache()
    cache.set("abc", "def")
    prepare_key.assert_called_once_with("abc")
    django_cache.set.assert_called_once_with("prepared key", "def")


def test_get(django_cache, prepare_key):
    """Test get."""
    django_cache.get.return_value = "def"
    cache = DjangoCache()
    assert cache.get("abc") == "def"
    prepare_key.assert_called_once_with("abc")
    django_cache.get.assert_called_once_with("prepared key")


def test_delete(django_cache, prepare_key):
    """Test delete."""
    cache = DjangoCache()
    cache.delete("abc")
    prepare_key.assert_called_once_with("abc")
    django_cache.delete.assert_called_once_with("prepared key")
