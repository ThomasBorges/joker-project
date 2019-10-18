from pymongo import MongoClient

class Saver():

    def __init__(self):
        self.client = MongoClient('localhost', 27017)
        self.db = self.client.jokerdb

        #columns
        self.coll_rt_Tweets = self.db.realTimeTweets2
        self.coll_s_Tweets = self.db.searchedTweets
        self.coll_clean_tweets = self.db.cleanTweets
        
    def setCollectionRealTimeTweets(self, data):
        self.coll_rt_Tweets.insert_one(data).inserted_id

    # def columnInsertSearchedTweets(self, obj):
    #     self.columns_s_Tweets.insert_one(obj).inserted_id

    def setCollectionCleanTweets(self, data):
        self.coll_clean_tweets.insert_one(data).inserted_id
       

    def getCollectionRealTimeTweets(self):
        return self.db.get_collection('realTimeTweets2').find({})
        
