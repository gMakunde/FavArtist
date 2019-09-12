import flask
import os
import random
import requests, requests_oauthlib
import json
from collections import namedtuple

app = flask.Flask(__name__)


@app.route('/')
def index():
    url = "https://api.genius.com/search?q=Ari%20Lennox"
    auth = os.getenv('Genius_Authorization')
    my_headers = { 
        "Authorization":"Bearer "+ auth
    }
    response = requests.get(url, headers=my_headers)
    json_body = response.json()
    song_data = namedtuple("song_data", "song_title song_art song_url")
    song_data_list = []
    for i in range(len(json_body['response']['hits'])):
        song_data_list.append(song_data(json_body['response']['hits'][i]['result']['title_with_featured'], json_body['response']['hits'][i]['result']['song_art_image_url'], json_body['response']['hits'][i]['result']['url']))
    print(song_data_list)
    #return flask.render_template("")
    
index()
"""
app.run(
    port=int(os.getenv('PORT', 8080)),
    host=os.getenv('IP', '0.0.0.0'),
    debug = True
    )
    """