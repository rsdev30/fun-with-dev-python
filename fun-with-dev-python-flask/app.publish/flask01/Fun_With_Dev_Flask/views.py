"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from Fun_With_Dev_Flask import app

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
def bubble_sort():
    """Renders the bubble sort page."""
    return render_template(
        'bubble_sort.html',
        title='Bubble Sort',
        year=datetime.now().year,
        message='Your bubble sort implementation page.'
    )