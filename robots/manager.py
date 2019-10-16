import json
from listener import Listener

with open('credentials/twitter-api.json') as json_file:
    #Open credentials and insert api keys
    twitter_apiKeys = json.load(json_file)


def start_to_listen():
    print("\n ===== Hey there, I'll start to listen to tweets about Joker ===== \n")
    print(" Press ctrl+C when you want me to stop!! ")
    mylistener = Listener(twitter_apiKeys)  
    mylistener.set_authentication()
    mylistener.start_listening()


print('test')