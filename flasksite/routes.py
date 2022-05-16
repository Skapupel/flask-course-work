from flask import render_template
from flasksite import app


@app.route('/')
def home():
    return render_template('index.html')