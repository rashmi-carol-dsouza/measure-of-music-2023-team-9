from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, send_from_directory, jsonify
import json
app = Flask(__name__)


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

@app.route('/collaborators', methods=['GET'])
def collaborators():
    # access request data
    data = request.get_json()
    requestedgenreId = data["target_genre"]
    careerStage = data["career_stage"]
    target_country = data["target_country"]
    name = data["target_genre"]
    originalGenreId = data["my_genre"]

    # Return dummy data
    with open('db.json') as f:
        data = json.load(f)

    return data

if __name__ == '__main__':
   app.run()