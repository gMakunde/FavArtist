import flask
import os
import random
import requests, requests_oauthlib
import json

app = flask.Flask(__name__)


@app.route('/')
def index():
    gen_url = "https://api.genius.com/search?q=Ari%20Lennox"
    twit_url = "https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=arilennox&include_rts=false"
    gen_auth = os.getenv('Genius_Authorization')
    twit_key = os.getenv('Twitter_Key')
    twit_secret = os.getenv('Twitter_Secret')
    twit_token = os.getenv('Twitter_Token')
    twit_token_secret = os.getenv('Twitter_Token_Secret')
    twit_oauth = requests_oauthlib.OAuth1(
        twit_key,
        twit_secret,
        twit_token,
        twit_token_secret,
    )
    genius_headers = { 
        "Authorization":"Bearer" + gen_auth
    }
    gen_response = requests.get(gen_url, headers=genius_headers)
    twit_response = requests.get(twit_url, auth=twit_oauth)
    gen_json_body = gen_response.json()
    twit_json_body = twit_response.json()
    
    gen_random_index = random.randint(0, len(gen_json_body['response']['hits'])-1)
    twit_random_index = random.randint(0, len(twit_json_body)-1)
    
    print(json.dumps(twit_json_body, indent=2))

    return flask.render_template(
        "ari_page.html", 
        song_name = gen_json_body['response']['hits'][gen_random_index]['result']['title_with_featured'], 
        song_url = gen_json_body['response']['hits'][gen_random_index]['result']['url'], 
        song_art = gen_json_body['response']['hits'][gen_random_index]['result']['header_image_thumbnail_url'],
        tweet_id = str(twit_json_body[twit_random_index]['id'])
    )

app.run(
    port=int(os.getenv('PORT', 8080)),
    host=os.getenv('IP', '0.0.0.0'),
    debug = True
    )
