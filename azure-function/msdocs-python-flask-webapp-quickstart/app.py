from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, send_from_directory, jsonify
import json
from service.authService import authorize
from service.collaboratorsService import getCollaborators
from flask_cors import CORS
import os


app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
   print('Request for index page received')
   return render_template('index.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/hello', methods=['POST'])
def hello():
   name = request.form.get('name')

   if name:
       print('Request for hello page received with name=%s' % name)
       return render_template('hello.html', name = name)
   else:
       print('Request for hello page received with no name or blank name -- redirecting')
       return redirect(url_for('index'))

@app.route('/collaborators', methods=['POST'])
def collaborators():
    # access request data
    data = request.get_json()
    accessToken = authorize()
    print(data)

    return getCollaborators(data, accessToken)

if __name__ == '__main__':
   app.run(debug=True)