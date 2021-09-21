from flask import Flask, render_template, request, flash, url_for
from werkzeug.utils import redirect, secure_filename

import urllib.request
import os


app = Flask(__name__)

UPLOAD_FOLDER = 'static/uploads/'

app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS



@app.route("/")
def my_form():
    return render_template('index.html')

@app.route("/", methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file= request.files['file']
    if file.filename == '':
        flash('No image selected for uploading')
        return redirect(request.url)
