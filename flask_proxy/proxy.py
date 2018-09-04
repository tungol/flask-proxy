import requests
from flask import Flask

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/<path:path>')
def get_dir(path):
    r = requests.get(path)
    return r.text