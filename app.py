import flask
import os
import random

app = flask.Flask(__name__)

@app.route('/')
def index():
    return flask.render_template("")
    