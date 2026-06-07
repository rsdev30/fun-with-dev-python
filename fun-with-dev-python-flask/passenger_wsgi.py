import sys, os

# Ensure the app directory is in sys.path
sys.path.insert(0, os.path.dirname(__file__))

# Activate virtual environment if used
venv_path = os.path.join(os.path.dirname(__file__), 'venv', 'bin', 'activate_this.py')
if os.path.exists(venv_path):
    with open(venv_path) as f:
        exec(f.read(), {'__file__': venv_path})

# Import the Flask app
from app import app as application  # Passenger looks for 'application'