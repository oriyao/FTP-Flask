from flask import render_template, request, url_for, redirect
from app import app

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')
