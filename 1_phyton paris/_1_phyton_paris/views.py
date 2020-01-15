"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from _1_phyton_paris import app

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/PhotoAlbum')
def PhotoAlbum():
    """Renders the contact page."""
    return render_template(
        'PhotoAlbum.html',
        title='Photo Album',
        year=datetime.now().year,
        message='Your contact page.'
    )


