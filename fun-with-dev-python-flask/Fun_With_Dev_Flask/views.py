"""
Routes and views for the flask application.

Added REST API endpoints under /api for sorting, searching, and basic data structure operations.
"""

import sys
from pathlib import Path
from datetime import datetime
from flask import render_template, request, jsonify
from Fun_With_Dev_Flask import app

# Add the shared project to Python path to allow imports from fun_with_dev_python_shared
shared_project_path = Path(__file__).parent.parent.parent / 'fun-with-dev-python-shared'
sys.path.insert(0, str(shared_project_path))

from fun_with_dev_python_shared.sorting.bubble_sort import bubble_sort
from fun_with_dev_python_shared.sorting.merge_sort import merge_sort
from fun_with_dev_python_shared.sorting.quick_sort import quick_sort
@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        './index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )

@app.route('/algorithms')
def algorithms():
    """Renders the algorithms page."""
    return render_template(
        'algorithms.html',
        title='Algorithms',
        year=datetime.now().year,
        message='Your algorithms page.'
    )


@app.route('/algorithms/bubble-sort')
def bubble_sort_page():
    """Renders the bubble sort page."""
    return render_template(
        'bubble_sort.html',
        title='Bubble Sort',
        year=datetime.now().year,
        message='Your bubble sort implementation page.'
    )

# --- REST API endpoints for algorithms (delegated to shared.sorting) ---


@app.route('/api/sort', methods=['POST'])
def api_sort():
    """Sort array with specified algorithm.
    Request JSON: { "algorithm": "bubble|merge|quick|builtin", "data": [...], "order": "asc|desc" }
    """
    payload = request.get_json(force=True)
    alg = (payload.get('algorithm') or 'builtin').lower()
    data = payload.get('data') or []
    order = (payload.get('order') or 'asc').lower()

    if not isinstance(data, list):
        return jsonify({ 'error': 'data must be a list' }), 400

    # ensure elements are comparable; attempt to sort using Python semantics
    try:
        if alg == 'bubble':
            result = bubble_sort(data)
        elif alg == 'merge':
            result = merge_sort(data)
        elif alg == 'quick':
            result = quick_sort(data)
        else:
            result = sorted(data)
    except Exception as e:
        return jsonify({ 'error': f'sort failed: {str(e)}' }), 400

    if order == 'desc':
        result = list(reversed(result))

    return jsonify({ 'algorithm': alg, 'result': result })


@app.route('/api/search', methods=['POST'])
def api_search():
    """Search for target in array.
    Request JSON: { "algorithm": "linear|binary", "data": [...], "target": value }
    Response: { "found": bool, "index": int or null, "algorithm": str }
    """
    payload = request.get_json(force=True)
    alg = (payload.get('algorithm') or 'linear').lower()
    data = payload.get('data') or []
    target = payload.get('target')

    if not isinstance(data, list):
        return jsonify({ 'error': 'data must be a list' }), 400

    if alg == 'linear':
        for i, v in enumerate(data):
            if v == target:
                return jsonify({ 'algorithm': 'linear', 'found': True, 'index': i })
        return jsonify({ 'algorithm': 'linear', 'found': False, 'index': None })

    if alg == 'binary':
        # binary search requires sorted data; produce a sorted copy and track index mapping
        try:
            sorted_data = sorted(data)
        except Exception as e:
            return jsonify({ 'error': f'cannot sort data for binary search: {str(e)}' }), 400
        lo = 0
        hi = len(sorted_data) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if sorted_data[mid] == target:
                return jsonify({ 'algorithm': 'binary', 'found': True, 'index': mid, 'sorted': True })
            elif sorted_data[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return jsonify({ 'algorithm': 'binary', 'found': False, 'index': None, 'sorted': True })

    return jsonify({ 'error': 'unsupported algorithm' }), 400


@app.route('/api/datastructures/stack', methods=['POST'])
def api_stack():
    """Simple stack simulation. Payload: { "operation": "push|pop|peek|init", "stack": [...], "value": optional }
    Returns the new stack and result for pop/peek.
    """
    payload = request.get_json(force=True) or {}

    if not isinstance(payload, dict):
        return jsonify({ 'error': 'invalid payload' }), 400

    if 'stack' not in payload:
        return jsonify({ 'error': 'stack must be provided and must be a list' }), 400

    op = (payload.get('operation') or 'init').lower()
    stack = payload.get('stack')
    value = payload.get('value', None)

    if not isinstance(stack, list):
        return jsonify({ 'error': 'stack must be a list' }), 400

    if op == 'push':
        stack.append(value)
        return jsonify({ 'operation': 'push', 'stack': stack })
    if op == 'pop':
        if not stack:
            return jsonify({ 'operation': 'pop', 'stack': stack, 'result': None, 'error': 'empty' })
        val = stack.pop()
        return jsonify({ 'operation': 'pop', 'stack': stack, 'result': val })
    if op == 'peek':
        val = stack[-1] if stack else None
        return jsonify({ 'operation': 'peek', 'stack': stack, 'result': val })
    if op == 'init':
        return jsonify({ 'operation': 'init', 'stack': stack })

    return jsonify({ 'error': 'unsupported operation' }), 400


@app.route('/api/datastructures/queue', methods=['POST'])
def api_queue():
    """Simple queue simulation. Payload: { "operation": "enqueue|dequeue|peek|init", "queue": [...], "value": optional }
    Returns the new queue and result for dequeue/peek.
    """
    payload = request.get_json(force=True)
    op = (payload.get('operation') or 'init').lower()
    queue = payload.get('queue') or []
    value = payload.get('value', None)

    if not isinstance(queue, list):
        return jsonify({ 'error': 'queue must be a list' }), 400

    if op == 'enqueue':
        queue.append(value)
        return jsonify({ 'operation': 'enqueue', 'queue': queue })
    if op == 'dequeue':
        if not queue:
            return jsonify({ 'operation': 'dequeue', 'queue': queue, 'result': None, 'error': 'empty' })
        val = queue.pop(0)
        return jsonify({ 'operation': 'dequeue', 'queue': queue, 'result': val })
    if op == 'peek':
        val = queue[0] if queue else None
        return jsonify({ 'operation': 'peek', 'queue': queue, 'result': val })
    if op == 'init':
        return jsonify({ 'operation': 'init', 'queue': queue })

    return jsonify({ 'error': 'unsupported operation' }), 400
