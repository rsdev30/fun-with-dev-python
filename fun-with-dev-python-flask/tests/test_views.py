import pytest
from Fun_With_Dev_Flask import app
import Fun_With_Dev_Flask.views as views


@pytest.fixture
def client():
    app.testing = True
    with app.test_client() as client:
        yield client


def test_pages_render(client):
    routes = ['/', '/home', '/contact', '/about', '/algorithms', '/algorithms/bubble-sort']
    for r in routes:
        resp = client.get(r)
        assert resp.status_code == 200
        assert 'text/html' in resp.content_type


def test_sort_helpers():
    assert views._bubble_sort([3, 1, 2]) == [1, 2, 3]
    assert views._merge_sort([5, 3, 1, 4]) == sorted([5, 3, 1, 4])
    assert views._quick_sort([3, 2, 2, 1]) == sorted([3, 2, 2, 1])


# --- /api/sort ---
def test_api_sort_bubble(client):
    r = client.post('/api/sort', json={'algorithm': 'bubble', 'data': [5, 1, 3]})
    assert r.status_code == 200
    j = r.get_json()
    assert j['algorithm'] == 'bubble'
    assert j['result'] == [1, 3, 5]


def test_api_sort_merge_desc(client):
    r = client.post('/api/sort', json={'algorithm': 'merge', 'data': [1, 4, 2], 'order': 'desc'})
    assert r.status_code == 200
    j = r.get_json()
    assert j['result'] == sorted([1, 4, 2], reverse=True)


def test_api_sort_builtin_strings(client):
    r = client.post('/api/sort', json={'algorithm': 'unknown', 'data': ['b', 'a']})
    assert r.status_code == 200
    assert r.get_json()['result'] == ['a', 'b']


def test_api_sort_bad_data_type(client):
    r = client.post('/api/sort', json={'algorithm': 'builtin', 'data': 'notalist'})
    assert r.status_code == 400
    assert 'error' in r.get_json()


def test_api_sort_uncomparable_elements(client):
    # mixing int and str should cause a sort failure in Python3 and return 400
    r = client.post('/api/sort', json={'algorithm': 'builtin', 'data': [1, 'a']})
    assert r.status_code == 400
    assert 'error' in r.get_json()


# --- /api/search ---
def test_api_search_linear_found(client):
    r = client.post('/api/search', json={'algorithm': 'linear', 'data': [1, 2, 3], 'target': 2})
    assert r.status_code == 200
    j = r.get_json()
    assert j['algorithm'] == 'linear'
    assert j['found'] is True
    assert j['index'] == 1


def test_api_search_linear_not_found(client):
    r = client.post('/api/search', json={'algorithm': 'linear', 'data': [1, 2, 3], 'target': 4})
    assert r.status_code == 200
    j = r.get_json()
    assert j['found'] is False


def test_api_search_binary_found_and_not_found(client):
    r = client.post('/api/search', json={'algorithm': 'binary', 'data': [3, 1, 2], 'target': 2})
    assert r.status_code == 200
    j = r.get_json()
    assert j['algorithm'] == 'binary'
    assert j['found'] is True
    assert j.get('sorted') is True

    r2 = client.post('/api/search', json={'algorithm': 'binary', 'data': [3, 1, 2], 'target': 99})
    assert r2.status_code == 200
    j2 = r2.get_json()
    assert j2['found'] is False


def test_api_search_bad_data(client):
    r = client.post('/api/search', json={'algorithm': 'linear', 'data': 'notalist', 'target': 1})
    assert r.status_code == 400
    assert 'error' in r.get_json()


# --- /api/datastructures/stack ---
def test_stack_operations(client):
    # init
    r = client.post('/api/datastructures/stack', json={'operation': 'init', 'stack': []})
    assert r.status_code == 200
    j = r.get_json()
    assert j['operation'] == 'init'

    # push
    r2 = client.post('/api/datastructures/stack', json={'operation': 'push', 'stack': [], 'value': 5})
    assert r2.status_code == 200
    j2 = r2.get_json()
    assert 5 in j2['stack']

    # pop
    r3 = client.post('/api/datastructures/stack', json={'operation': 'pop', 'stack': [1, 2, 3]})
    assert r3.status_code == 200
    j3 = r3.get_json()
    assert j3['result'] == 3

    # peek
    r4 = client.post('/api/datastructures/stack', json={'operation': 'peek', 'stack': [9]})
    assert r4.status_code == 200
    j4 = r4.get_json()
    assert j4['result'] == 9


def test_stack_bad_payload(client):
    r = client.post('/api/datastructures/stack', json={'operation': 'push', 'stack': {}})
    assert r.status_code == 400
    assert 'error' in r.get_json()


# --- /api/datastructures/queue ---
def test_queue_operations(client):
    # init
    r = client.post('/api/datastructures/queue', json={'operation': 'init', 'queue': []})
    assert r.status_code == 200

    # enqueue
    r2 = client.post('/api/datastructures/queue', json={'operation': 'enqueue', 'queue': [], 'value': 'x'})
    assert r2.status_code == 200
    assert 'x' in r2.get_json()['queue']

    # dequeue
    r3 = client.post('/api/datastructures/queue', json={'operation': 'dequeue', 'queue': [1, 2, 3]})
    assert r3.status_code == 200
    assert r3.get_json()['result'] == 1

    # peek
    r4 = client.post('/api/datastructures/queue', json={'operation': 'peek', 'queue': [7]})
    assert r4.status_code == 200
    assert r4.get_json()['result'] == 7


def test_queue_bad_payload(client):
    r = client.post('/api/datastructures/queue', json={'operation': 'enqueue', 'queue': 'notalist'})
    assert r.status_code == 400
    assert 'error' in r.get_json()
