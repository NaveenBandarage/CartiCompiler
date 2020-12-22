from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

#export FLASK_APP=testFlask.py
#flask run
#this is how you deploy to the web.