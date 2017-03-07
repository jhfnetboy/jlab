#!/usr/bin
# encoding=utf-8

import sys
import time
import os
from flask import Flask, request, redirect, url_for
from werkzeug import security
reload(sys)
sys.setdefaultencoding("utf-8")


# 1.using flask to build a little web page to get txt
# 2.use python interface to analysis the txt file and show the result in pages

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = set(['txt'])
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def defaultWeb():
    '''
    run a server return the default
    '''
    user_agent = request.headers.get('User-Agent')
    #return " <p>Your browser is %s</p>  " % user_agent
    return 'Hello !<br/>Here is the default web page of jTech NLP lab'+"'"+'s!'


@app.route('/nlp', methods=['GET', 'POST'])
def upload_file2():
    '''
    get a txt file then process it and show the result
    '''
    from flask import render_template
    if (request.method == 'POST') and (request):
        #print request
        print request.form.get("upfile")
        return 'hi'
    else:
        return render_template('upload.html')
    return time.strftime("%H:%M:%S", time.localtime(time.time()))

@app.route('/u', methods=['GET', 'POST'])
def upload_file():
    up_page = '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form action="" method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = str(time.time())
            process_txt(file.read())
            #print file.read()
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename+'.txt'))
            return redirect(url_for('upload_file',filename=filename))
    return up_page


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


def process_txt(content):
    '''
    get txt content
    :return a statstic list and a word cloud png:
    '''
    if not content:
        return False


# curl -F 'file=@"foo.png";filename="bar.png"' 127.0.0.1:5000
# curl -F 'file=@"test.txt"' 127.0.0.1:5000/nlp


if __name__ == '__main__':
    app.run(debug=True)