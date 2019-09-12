import flask
import os
import random
import requests, requests_oauthlib
import json

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
    
    random_index = random.randint(0, len(json_body['response']['hits'])-1)
    return flask.render_template(
        "ari_page.html", 
        song_name = json_body['response']['hits'][random_index]['result']['title_with_featured'], 
        song_url = json_body['response']['hits'][random_index]['result']['url'], 
        song_art = json_body['response']['hits'][random_index]['result']['header_image_thumbnail_url']
    )

app.run(
    port=int(os.getenv('PORT', 8080)),
    host=os.getenv('IP', '0.0.0.0'),
    debug = True
    )