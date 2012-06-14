import os
import tweepy
import requests
import datetime

consumer_key = os.environ.get('consumer_key')
consumer_secret = os.environ.get('consumer_secret')

access_token = os.environ.get('access_token')
access_token_secret = os.environ.get('access_token_secret')

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

status_code = requests.get('http://www.unboxedconsulting.com/people/carl-whittaker').status_code
status_response = 'YES' if status_code == 200 else 'NO'

api.update_status(status_response + ' http://www.doescarlhaveacaricatureyet.com ' + datetime.datetime.now().strftime('%y-%m-%y %H:%M'))
