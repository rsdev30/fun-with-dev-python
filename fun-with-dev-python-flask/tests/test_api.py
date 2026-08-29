"""
Unit tests for the Flask application.

Tests cover:
- View functions (routes)
- API endpoints for sorting
- API endpoints for searching
- API endpoints for data structures (stack, queue)
- Error handling and edge cases
"""

import pytest
import json
from Fun_With_Dev_Flask import app


@pytest.fixture
def client():
    """Create a test client for the Flask app."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


class TestPageRoutes:
    """Tests for page rendering routes."""

    def test_home_page(self, client):
        """Test home page route."""
        response = client.get('/')
        assert response.status_code == 200
        assert b'Home Page' in response.data or b'home' in response.data.lower()

    def test_home_alternate_route(self, client):
        """Test home page alternate route."""
        response = client.get('/home')
        assert response.status_code == 200

    def test_contact_page(self, client):
        """Test contact page route."""
        response = client.get('/contact')
        assert response.status_code == 200
        assert b'Contact' in response.data

    def test_about_page(self, client):
        """Test about page route."""
        response = client.get('/about')
        assert response.status_code == 200
        assert b'About' in response.data

    def test_algorithms_page(self, client):
        """Test algorithms page route."""
        response = client.get('/algorithms')
        assert response.status_code == 200
        assert b'Algorithms' in response.data

    def test_bubble_sort_page(self, client):
        """Test bubble sort page route."""
        response = client.get('/algorithms/bubble-sort')
        assert response.status_code == 200
        assert b'Bubble Sort' in response.data

    def test_nonexistent_page(self, client):
        """Test accessing a nonexistent page."""
        response = client.get('/nonexistent')
        assert response.status_code == 404


class TestSortingAPI:
    """Tests for the sorting API endpoints."""

    def test_bubble_sort_api(self, client):
        """Test bubble sort API endpoint."""
        payload = {
            'algorithm': 'bubble',
            'data': [5, 2, 8, 1, 9],
            'order': 'asc'
        }
        response = client.post('/api/sort',
                              data=json.dumps(payload),
                              content_type='application/json')
        assert response.status_code == 200
        data = json.loads(response.data)
        assert data['algorithm'] == 'bubble'
        assert data['result'] == [1, 2, 5, 8, 9]

    def test_merge_sort_api(self, client):
        """Test merge sort API endpoint."""
        payload = {
            'algorithm': 'merge',
            'data': [5, 2, 8, 1, 9],
            'order': 'asc'
        }
        response = client.post('/api/sort',
                              data=json.dumps(payload),
                              content_type='application/json')
        assert response.status_code == 200
        data = json.loads(response.data)
        assert data['algorithm'] == 'merge'
        assert data['result'] == [1, 2, 5, 8, 9]

    def test_quick_sort_api(self, client):
        """Test quick sort API endpoint."""
        payload = {
            'algorithm': 'quick',
            'data': [5, 2, 8, 1, 9],
            'order': 'asc'
        }
        response = client.post('/api/sort',
                              data=json.dumps(payload),
                              content_type='application/json')
        assert response.status_code == 200
        data = json.loads(response.data)
        assert data['algorithm'] == 'quick'
        assert data['result'] == [1, 2, 5, 8, 9]

    def test_builtin_sort_api(self, client):
        """Test builtin sort API endpoint."""
        payload = {
            'algorithm': 'builtin',
            'data': [5, 2, 8, 1, 9],
            'order': 'asc'
        }
        response = client.post('/api/sort',
                              data=json.dumps(payload),
                              content_type='application/json')
        assert response.status_code == 200
        data = json.loads(response.data)
        assert data['algorithm'] == 'builtin'
        assert data['result'] == [1, 2, 5, 8, 9]

    def test_sort_descending(self, client):
        """Test sorting in descending order."""
        payload = {
            'algorithm': 'bubble',
            'data': [5, 2, 8, 1, 9],
            'order': 'desc'
        }
        response = client.post('/api/sort',
                              data=json.dumps(payload),
                              content_type='application/json')
        assert response.status_code == 200
        data = json.loads(response.data)
        assert data['result'] == [9, 8, 5, 2, 1]

    def test_sort_empty_list(self, client):
        """Test sorting an empty list."""
        payload = {
            'algorithm': 'bubble',
            'data': [],
            'order': 'asc'
        }
        response = client.post('/api/sort',
                              data=json.dumps(payload),
                              content_type='application/json')
        assert response.status_code == 200
        data = json.loads(response.data)
        assert data['result'] == []

    def test_sort_with_duplicates(self, client):
        """Test sorting with duplicate values."""
        payload = {
            'algorithm': 'bubble',
            'data': [3, 1, 4, 1, 5, 9, 2, 6, 5],
            'order': 'asc'
        }
        response = client.post('/api/sort',
                              data=json.dumps(payload),
                              content_type='application/json')
        assert response.status_code == 200
        data = json.loads(response.data)
        assert data['result'] == [1, 1, 2, 3, 4, 5, 5, 6, 9]

    def test_sort_with_negative_numbers(self, client):
        """Test sorting with negative numbers."""
        payload = {
            'algorithm': 'bubble',
            'data': [5, -3, 0, 2, -1],
            'order': 'asc'
        }
        response = client.post('/api/sort',
                              data=json.dumps(payload),
                              content_type='application/json')
        assert response.status_code == 200
        data = json.loads(response.data)
        assert data['result'] == [-3, -1, 0, 2, 5]

    def test_sort_invalid_data_type(self, client):
        """Test sorting with invalid data type."""
        payload = {
            'algorithm': 'bubble',
            'data': 'not a list',
            'order': 'asc'
        }
        response = client.post('/api/sort',
                              data=json.dumps(payload),
                              content_type='application/json')
        assert response.status_code == 400
        data = json.loads(response.data)
        assert 'error' in data


class TestSearchAPI:
    """Tests for the search API endpoints."""

    def test_linear_search_found(self, client):
        """Test linear search when element is found."""
        payload = {
            'algorithm': 'linear',
            'data': [5, 2, 8, 1, 9],
            'target': 8
        }
        response = client.post('/api/search',
                              data=json.dumps(payload),
                              content_type='application/json')
        assert response.status_code == 200
        data = json.loads(response.data)
        assert data['found'] is True
        assert data['index'] == 2
        assert data['algorithm'] == 'linear'

    def test_linear_search_not_found(self, client):
        """Test linear search when element is not found."""
        payload = {
            'algorithm': 'linear',
            'data': [5, 2, 8, 1, 9],
            'target': 10
        }
        response = client.post('/api/search',
                              data=json.dumps(payload),
                              content_type='application/json')
        assert response.status_code == 200
        data = json.loads(response.data)
        assert data['found'] is False
        assert data['index'] is None

    def test_binary_search_found(self, client):
        """Test binary search when element is found."""
        payload = {
            'algorithm': 'binary',
            'data': [1, 2, 3, 4, 5, 8, 9],
            'target': 5
        }
        response = client.post('/api/search',
                              data=json.dumps(payload),
                              content_type='application/json')
        assert response.status_code == 200
        data = json.loads(response.data)
        assert data['found'] is True
        assert data['algorithm'] == 'binary'

    def test_binary_search_not_found(self, client):
        """Test binary search when element is not found."""
        payload = {
            'algorithm': 'binary',
            'data': [1, 2, 3, 4, 5, 8, 9],
            'target': 10
        }
        response = client.post('/api/search',
                              data=json.dumps(payload),
                              content_type='application/json')
        assert response.status_code == 200
        data = json.loads(response.data)
        assert data['found'] is False

    def test_search_empty_list(self, client):
        """Test searching in an empty list."""
        payload = {
            'algorithm': 'linear',
            'data': [],
            'target': 5
        }
        response = client.post('/api/search',
                              data=json.dumps(payload),
                              content_type='application/json')
        assert response.status_code == 200
        data = json.loads(response.data)
        assert data['found'] is False

    def test_search_invalid_algorithm(self, client):
        """Test search with invalid algorithm."""
        payload = {
            'algorithm': 'invalid',
            'data': [5, 2, 8],
            'target': 5
        }
        response = client.post('/api/search',
                              data=json.dumps(payload),
                              content_type='application/json')
        assert response.status_code == 400
        data = json.loads(response.data)
        assert 'error' in data


class TestStackAPI:
    """Tests for the stack data structure API."""

    def test_stack_push(self, client):
        """Test pushing to stack."""
        payload = {
            'operation': 'push',
            'stack': [1, 2],
            'value': 3
        }
        response = client.post('/api/datastructures/stack',
                              data=json.dumps(payload),
                              content_type='application/json')
        assert response.status_code == 200
        data = json.loads(response.data)
        assert data['operation'] == 'push'
        assert data['stack'] == [1, 2, 3]

    def test_stack_pop(self, client):
        """Test popping from stack."""
        payload = {
            'operation': 'pop',
            'stack': [1, 2, 3],
            'value': None
        }
        response = client.post('/api/datastructures/stack',
                              data=json.dumps(payload),
                              content_type='application/json')
        assert response.status_code == 200
        data = json.loads(response.data)
        assert data['operation'] == 'pop'
        assert data['stack'] == [1, 2]
        assert data['result'] == 3

    def test_stack_pop_empty(self, client):
        """Test popping from empty stack."""
        payload = {
            'operation': 'pop',
            'stack': [],
            'value': None
        }
        response = client.post('/api/datastructures/stack',
                              data=json.dumps(payload),
                              content_type='application/json')
        assert response.status_code == 200
        data = json.loads(response.data)
        assert data['operation'] == 'pop'
        assert data['result'] is None
        assert 'error' in data

    def test_stack_peek(self, client):
        """Test peeking at top of stack."""
        payload = {
            'operation': 'peek',
            'stack': [1, 2, 3],
            'value': None
        }
        response = client.post('/api/datastructures/stack',
                              data=json.dumps(payload),
                              content_type='application/json')
        assert response.status_code == 200
        data = json.loads(response.data)
        assert data['operation'] == 'peek'
        assert data['result'] == 3
        assert data['stack'] == [1, 2, 3]

    def test_stack_init(self, client):
        """Test initializing stack."""
        payload = {
            'operation': 'init',
            'stack': [1, 2, 3],
            'value': None
        }
        response = client.post('/api/datastructures/stack',
                              data=json.dumps(payload),
                              content_type='application/json')
        assert response.status_code == 200
        data = json.loads(response.data)
        assert data['operation'] == 'init'
        assert data['stack'] == [1, 2, 3]

    def test_stack_missing_stack_param(self, client):
        """Test stack operation without stack parameter."""
        payload = {
            'operation': 'push',
            'value': 5
        }
        response = client.post('/api/datastructures/stack',
                              data=json.dumps(payload),
                              content_type='application/json')
        assert response.status_code == 400
        data = json.loads(response.data)
        assert 'error' in data


class TestQueueAPI:
    """Tests for the queue data structure API."""

    def test_queue_enqueue(self, client):
        """Test enqueuing to queue."""
        payload = {
            'operation': 'enqueue',
            'queue': [1, 2],
            'value': 3
        }
        response = client.post('/api/datastructures/queue',
                              data=json.dumps(payload),
                              content_type='application/json')
        assert response.status_code == 200
        data = json.loads(response.data)
        assert data['operation'] == 'enqueue'
        assert data['queue'] == [1, 2, 3]

    def test_queue_dequeue(self, client):
        """Test dequeuing from queue."""
        payload = {
            'operation': 'dequeue',
            'queue': [1, 2, 3],
            'value': None
        }
        response = client.post('/api/datastructures/queue',
                              data=json.dumps(payload),
                              content_type='application/json')
        assert response.status_code == 200
        data = json.loads(response.data)
        assert data['operation'] == 'dequeue'
        assert data['queue'] == [2, 3]
        assert data['result'] == 1

    def test_queue_dequeue_empty(self, client):
        """Test dequeuing from empty queue."""
        payload = {
            'operation': 'dequeue',
            'queue': [],
            'value': None
        }
        response = client.post('/api/datastructures/queue',
                              data=json.dumps(payload),
                              content_type='application/json')
        assert response.status_code == 200
        data = json.loads(response.data)
        assert data['operation'] == 'dequeue'
        assert data['result'] is None
        assert 'error' in data

    def test_queue_peek(self, client):
        """Test peeking at front of queue."""
        payload = {
            'operation': 'peek',
            'queue': [1, 2, 3],
            'value': None
        }
        response = client.post('/api/datastructures/queue',
                              data=json.dumps(payload),
                              content_type='application/json')
        assert response.status_code == 200
        data = json.loads(response.data)
        assert data['operation'] == 'peek'
        assert data['result'] == 1
        assert data['queue'] == [1, 2, 3]

    def test_queue_init(self, client):
        """Test initializing queue."""
        payload = {
            'operation': 'init',
            'queue': [1, 2, 3],
            'value': None
        }
        response = client.post('/api/datastructures/queue',
                              data=json.dumps(payload),
                              content_type='application/json')
        assert response.status_code == 200
        data = json.loads(response.data)
        assert data['operation'] == 'init'
        assert data['queue'] == [1, 2, 3]

    def test_queue_invalid_data_type(self, client):
        """Test queue operation with invalid data type."""
        payload = {
            'operation': 'enqueue',
            'queue': 'not a list',
            'value': 5
        }
        response = client.post('/api/datastructures/queue',
                              data=json.dumps(payload),
                              content_type='application/json')
        assert response.status_code == 400
        data = json.loads(response.data)
        assert 'error' in data
