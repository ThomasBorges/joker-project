import json
from listener import Listener

with open('credentials/twitter-api.json') as json_file:
    #Open credentials and insert api keys
    apiKeys = json.load(json_file)


tweet_listener = Listener(apiKeys)  
tweet_listener.set_authentication()