from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
from saver import Saver
import pandas as pd 
import time
import os


class Analyser():
    
    def __init__(self):

        os.environ['GOOGLE_APPLICATION_CREDENTIALS']="credentials/google-nlp-api.json"
        # Instantiates a client
        self.client = language.LanguageServiceClient()

        self.saver = Saver()


    
   
    def sentiment_analyses(self, data):
        invalid_language=0
        #requestmin=0
        #requestday=0

        print('=== It can take a while, so grab a coffee! ===')
        for i, row in data.iterrows():
            #if requestday == 800000: break   // don't know if this is
            # if requestmin == 600: 
            #     time.sleep(61)
            #     requestmin = 0

            text = row['text']
            document = types.Document(
                content=text,
                type=enums.Document.Type.PLAIN_TEXT)  
            try:
                sentiment = self.client.analyze_sentiment(document=document).document_sentiment
            except:
                print('invalid language')
                invalid_language+=1
                pass
            #requestmin+=1
            #requestday+=1

            analy_data = {
                'id_str':row['id_str'],
                'score':sentiment.score,
                'magnitude':sentiment.magnitude
            }
            print(invalid_language)
            self.saver.set_collection_analyzed_tweets(analy_data)