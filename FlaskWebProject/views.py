"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from FlaskWebProject import app
import requests


@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )


x = datetime.now().year
message1="11:40 AM, Sun, May 10th. 12 Citibikes Available. Temp 46 F. No Rain. A Train Manhatten 5mins, 25mins. C Train Manhatten 10mins, 30mins. BTC $243.34." + str(x)

@app.route('/latest')
def latest():
    """Renders the latest page."""
    return render_template(
        'latest.html',
        title='Latest',
        year=datetime.now().year,
        message= message1
    )

message1="11:40 AM, Sun, May 10th. 12 Citibikes Available. Temp 46 F. No Rain. A Train Manhatten 5mins, 25mins. C Train Manhatten 10mins, 30mins. BTC $243.34.*"

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message= message1
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
