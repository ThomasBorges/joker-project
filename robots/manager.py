from preprocessor import Preprocessor
from posprocessor import Posprocessor
from analyser import Analyser
from listener import Listener
from saver import Saver
import pandas as pd
import json

newSaver = Saver()

def start_to_listen():
    with open('credentials/twitter-api.json') as json_file:
        #Open credentials and insert api keys
        twitter_apiKeys = json.load(json_file)

    print("\n ===== Hey there, I'll start to listen to tweets about Joker ===== \n")
    print(" Press ctrl+C when you want me to stop!! ")
    mylistener = Listener(twitter_apiKeys)  
    mylistener.set_authentication()
    mylistener.start_listening()


def start_to_preprocess():
    pp = Preprocessor()
    data = pd.DataFrame(list(newSaver.get_collection('realTimeTweets')))
    pp.clean_frame(data)

    ##use this if you want to create a csv file to visualize
    # with open('tmpcsv.csv', 'w') as tmpcsv:
    # tmpcsv.writelines(data.to_csv())


def start_to_analyse():
    an = Analyser()
    data = pd.DataFrame(list(newSaver.get_collection('cleanTweets')))
    an.sentiment_analyses(data)

def start_to_posprocess():
    pp = Posprocessor()
    pp.start_to_posprocess()
    

