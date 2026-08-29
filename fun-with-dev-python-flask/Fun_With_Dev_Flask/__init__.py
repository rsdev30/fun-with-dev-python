"""
The flask application package.
"""

import sys
from pathlib import Path
import stat

# Add the shared project to Python path to allow imports from fun_with_dev_python_shared
shared_project_path = Path(__file__).parent.parent.parent / 'fun-with-dev-python-shared'
sys.path.insert(0, str(shared_project_path))

from flask import Flask
app = Flask(__name__)

import Fun_With_Dev_Flask.views
from fun_with_dev_python_shared.sorting import bubble_sort, merge_sort, quick_sort
