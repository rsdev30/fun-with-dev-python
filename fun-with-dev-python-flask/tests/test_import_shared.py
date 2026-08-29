"""
Integration tests to verify the shared project can be imported by the Flask app.

These tests attempt two methods:
- Dynamically adding the shared project directory to sys.path and importing
- Importing the package as if it were installed (skip if not installed)
"""

import sys
from pathlib import Path
import importlib
import pytest


def test_import_shared_via_sys_path():
    # Locate repository root relative to this test file
    repo_root = Path(__file__).resolve().parents[2]
    shared_path = repo_root / 'fun-with-dev-python-shared'
    assert shared_path.exists(), f"Shared project path does not exist: {shared_path}"

    # Temporarily add to sys.path and import
    sys.path.insert(0, str(shared_path))
    try:
        mod = importlib.import_module('fun_with_dev_python_shared.sorting.bubble_sort')
        assert hasattr(mod, 'bubble_sort')
    finally:
        # clean up
        sys.path.pop(0)


def test_import_shared_installed_or_skip():
    try:
        importlib.import_module('fun_with_dev_python_shared')
    except Exception:
        pytest.skip('fun_with_dev_python_shared not installed in environment')
    # If import succeeds, verify sorting modules
    mod = importlib.import_module('fun_with_dev_python_shared.sorting')
    assert hasattr(mod, 'bubble_sort')
    assert hasattr(mod, 'merge_sort')
    assert hasattr(mod, 'quick_sort')
