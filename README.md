# FTP-Flask

## run.py
```
from app import app

if __name__ == '__main__':
    app.run()
```  
## config.py
```
LOG_SPACE = '/app/FTP'
```

## /app

### __init__.py
```
from flask import Flask
app = Flask(__name__)
app.config.from_object('config')
from app import views
```

### views.py
> conding=utf-8
from flask import render_template, request, url_for, redirect
from flask import send_from_directory
from app import appinfo_caculator
from app import space_support
from app import app


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        space_support.add_space(request.values.get('space_name'))
    return render_template('index.html', dirs=space_support.get_space())


@app.route('/space/<string:space_name>', methods=['GET', 'POST'])
def space(space_name):
    if request.method == 'POST':
        space_support.upload_file(space_name, request.files.getlist('input'))
        space_support.add_space(request.values.get('space_name'))
    return render_template(
        'index.html',
        dirs=space_support.get_space(),
        files=space_support.get_space_files(space_name),
        space_name=space_name)


@app.route('/log_analysis/<string:space_name>')
def log_analysis(space_name):
    app_infos = appinfo_caculator.analysis_space(space_name)
    return render_template('result.html', app_infos=app_infos)


@app.route('/delete_file/<string:space_name>/<string:file_name>')
def delete_file(space_name, file_name):
    space_support.delete_file(space_name, file_name)
    return redirect(url_for('space', space_name=space_name))


@app.route('/download_file/<string:space_name>/<string:file_name>')
def download_file(space_name, file_name):
    return send_from_directory(
        space_support.get_space_path(space_name),
        file_name,
        as_attachment=True)

### space_support.py
> coding=utf-8
import os
from app import app
PATH = os.getcwd() + app.config['LOG_SPACE']


def get_space():
    return os.listdir(PATH)


def get_space_files(space_name):
    return os.listdir(PATH + space_name)


def get_space_path(space_name):
    return PATH + space_name


def add_space(space_name):
    if space_name:
        if not os.path.exists(PATH + space_name):
            os.makedirs(PATH + space_name)


def upload_file(space_name, files):
    for file in files:
        file.save(PATH + space_name + '/' + file.filename)


def delete_file(space_name, file_name):
    path = PATH + space_name + '/' + file_name
    os.remove(path)
