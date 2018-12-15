from flask import render_template, request, url_for, redirect
from app import app

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/demolove/')
def demolove():
    return render_template('./demo/love.html')


@app.route('/oriyao/')
def oriyao():
    return render_template('./demo/oriyao.html')

@app.route('/item/')
def item():
    return render_template('./item/item.html')