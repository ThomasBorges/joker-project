from pymongo import MongoClient

class Saver():

    def __init__(self, column_name):
        self.client = MongoClient('localhost', 27017)
        self.db = self.client.jokerdb
        self.columns_rt_Tweets = self.db.rtTweets
        
    def columnInsertTweets(self, obj):
        self.columns_rt_Tweets.insert_one(obj).inserted_id
        
       