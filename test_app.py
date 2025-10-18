from app import api
import pytest


def test_get():
    my_api = api()
    my_api["POST"](1)

    result = my_api["GET"]()
    expected = {
        "code": 200,
        "data": [1],
    }
    assert result == expected


def test_post():
    my_api = api()
    my_api["POST"](1)
    
    result = my_api["POST"](2)
    expected = {
        "code": 201,
        "data": [1, 2],
    }
    assert result == expected


def test_post_error():
    my_api = api()
    my_api["POST"](1)

    result = my_api["POST"](1)
    expected = {
        "code": 500,
        "error": "1 already exists",
    }
    assert result == expected
