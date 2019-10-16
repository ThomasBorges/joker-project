from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from datetime import datetime
import json


class Listener(StreamListener):

    def __init__(self, apiKeys):
        self.consumer_key = apiKeys['consumer_key']
        self.consumer_secret = apiKeys['consumer_secret']
        self.access_token = apiKeys['access_token']
        self.access_token_secret = apiKeys['access_token_secret']
        print("OK")

    def set_authentication(self):
        self.auth = OAuthHandler(self.consumer_key, self.consumer_secret)
        self.auth.set_access_token(self.access_token, self.access_token_secret)
        print("OK!")

    def on_data(self, dados):
        tweet = json.loads(dados)
        created_at = tweet["created_at"]
        id_str = tweet["id_str"]
        text = tweet["text"]
        obj = {"created_at":created_at,"id_str":id_str,"text":text,}
        tweetind = col.insert_one(obj).inserted_id
        return True


