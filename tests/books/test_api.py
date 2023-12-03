import requests
import pytest


def pytest_namespace():
    return {'last_id': None}


def test_get_all():
    response = requests.get("http://127.0.0.1:8000/books")
    assert response.status_code == 200


def test_add_book():
    response = requests.post("http://127.0.0.1:8000/books/",
                             json={
                                 "title": "string",
                                 "description": "string"
                             })
    assert response.status_code == 201
    pytest.last_id = response.json()['id']


def test_get_single():
    response = requests.get(f"http://127.0.0.1:8000/books/{pytest.last_id}")
    assert response.status_code == 200


def test_update_book():
    response = requests.put(f"http://127.0.0.1:8000/books/{pytest.last_id}",
                            json={
                                "title": "updated string",
                                "description": "string"
                            })
    assert response.status_code == 201


def test_delete_book():
    response = requests.delete(f"http://127.0.0.1:8000/books/{pytest.last_id}")
    assert response.status_code == 200


def test_get_single_error():
    response = requests.get(
        f"http://127.0.0.1:8000/books/{pytest.last_id + 1}")
    assert response.status_code == 404


def test_add_book_error():
    response = requests.post("http://127.0.0.1:8000/books/",
                             json={
                                 "title": 1,
                                 "description": 1
                             })
    assert response.status_code == 422


def test_update_book_error():
    response = requests.put(f"http://127.0.0.1:8000/books/{pytest.last_id + 1}",
                            json={
                                "title": "updated string",
                                "description": "string"
                            })
    assert response.status_code == 404


def test_delete_book_error():
    response = requests.delete(
        f"http://127.0.0.1:8000/books/{pytest.last_id + 1}")
    assert response.status_code == 404
