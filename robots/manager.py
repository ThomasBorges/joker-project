import json
import pandas as pd
from listener import Listener
from saver import Saver
from preprocessor import Preprocessor

with open('credentials/twitter-api.json') as json_file:
    #Open credentials and insert api keys
    twitter_apiKeys = json.load(json_file)


def start_to_listen():
    print("\n ===== Hey there, I'll start to listen to tweets about Joker ===== \n")
    print(" Press ctrl+C when you want me to stop!! ")
    mylistener = Listener(twitter_apiKeys)  
    mylistener.set_authentication()
    mylistener.start_listening()


# def start_to_search():
#     mySearcher = Searcher(twitter_apiKeys)
#     mySearcher.set_authentication()
#     mySearcher.start_to_search()

def start_to_preprocess():
    newSaver = Saver()
    pp = Preprocessor()
    data = pd.DataFrame(list(newSaver.getCollectionRealTimeTweets()))
    pp.clean_frame(data)
    #use this if you want to create a csv file to visualize
    # with open('tmpcsv.csv', 'w') as tmpcsv:
    # tmpcsv.writelines(data.to_csv())
    