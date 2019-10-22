from pymongo import MongoClient

class Saver():

    def __init__(self):
        self.client = MongoClient('localhost', 27017)
        self.db = self.client.testejoker

        #columns
        self.coll_rt_tweets = self.db.realTimeTweets
        self.coll_s_tweets = self.db.searchedTweets
        self.coll_clean_tweets = self.db.cleanTweets
        self.coll_analyzed_tweets = self.db.analyTweets
        
    def set_collection_real_time_tweets(self, data):
        self.coll_rt_tweets.insert_one(data).inserted_id

    # def set_coll_seacherd_tweets(self, obj):
    #     self.columns_s_tweets.insert_one(obj).inserted_id

    def set_collection_clean_tweets(self, data):
        self.coll_clean_tweets.insert_one(data).inserted_id
       
    def set_collection_analyzed_tweets(self, data):
        self.coll_analyzed_tweets.insert_one(data).inserted_id

    def get_collection(self, collection):
        return self.db.get_collection(collection).find({})

        
