"""
This script runs the FlaskWebProject1 application using a development server.
"""

from os import environ
from Fun_With_Dev_Flask import app


def application(environ, start_response):
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
    status='200 OK'
    headers=[('Content-Type', 'text/html')]
    start_response(status, headers)
    return [b"200 OK"]

def dummy_start_response(status, response_headers, exc_info=None):
    print(f"start_response called: {status}, {response_headers}")
    return None

if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
    response = application(environ, dummy_start_response)
    print(b"".join(response).decode())