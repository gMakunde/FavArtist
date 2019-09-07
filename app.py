import flask
import os
import random
import requests, requests_oauthlib
import json

app = flask.Flask(__name__)
url = "https://api.genius.com/search?q=Ari%20Lennox"
my_headers = { 
    "Authorization":"Bearer blarg"
    
}
response = requests.get(url, headers=my_headers)
json_body = response.json()
print(json_body)

@app.route('/')
def index():
    return flask.render_template("")
    