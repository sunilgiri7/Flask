#program to run a app in local host

from flask import Flask
###WSGI Application
app = Flask(__name__)


@app.route('/')
def welcome():
    return"Welcome to my code"

if __name__=='__main__':
    app.run(debug=True)