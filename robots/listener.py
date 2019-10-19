from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from datetime import datetime
from saver import Saver
import json


class Listener(StreamListener):

    def __init__(self, apiKeys):
        """ This constructor make sure to attribute the keys to acess twitter api,
            also it create a instance of saver to be able to save in mongo the tweets we get,
            finally it sets the keywords and languages that will be used to filter the real-time tweets that we want.
        """
        self.consumer_key = apiKeys['consumer_key']
        self.consumer_secret = apiKeys['consumer_secret']
        self.access_token = apiKeys['access_token']
        self.access_token_secret = apiKeys['access_token_secret']

        self.savetweets = Saver()        
        self.listen_keywords = ['Joker', 'Coringa', 'Joker Movie', 'Joker Joaquin Phoenix', 'Joaquin Phoenix'] #set the words to filter here
        self.languages = ['en','pt'] #set the language here


    def set_authentication(self):
        self.auth = OAuthHandler(self.consumer_key, self.consumer_secret)
        self.auth.set_access_token(self.access_token, self.access_token_secret)

    def on_data(self, data):
        tweet = json.loads(data)
        created_at = tweet["created_at"]
        id_str = tweet["id_str"]
        text = tweet["text"]
        obj = {"created_at":created_at,"id_str":id_str,"text":text,}
        self.savetweets.set_collection_real_time_tweets(obj)
        return True

    def start_listening(self):
        self.myStream = Stream(self.auth, listener = self)
        self.myStream.filter(track=self.listen_keywords, languages=self.languages)


