# Simple web application using Flask framework
from flask import Flask

Flaskapp = Flask(__name__)

@Flaskapp.route("/")
def hello_world():
    return "<p>Hello, Weishen!</p>"

if __name__ == '__main__':
   Flaskapp.run(host="0.0.0.0", port=8080)