import pandas as pd 
import re 
from nltk.tokenize import WordPunctTokenizer
from saver import Saver


class Preprocessor():
    def __init__(self):
        self.saver = Saver()


    def clean_frame(self, data):

        for index, rows in data.iterrows():
            user_removed = re.sub(r'@[A-Za-z0-9]+','',rows['text'])
            link_removed = re.sub('https?://[A-Za-z0-9./]+','',user_removed)
            # number_removed = re.sub('[^a-zA-Z]', ' ', link_removed) //can use this to remove punctuation
            lower_case_tweet= link_removed.lower()
            tok = WordPunctTokenizer()
            words = tok.tokenize(lower_case_tweet)
            clean_tweet = (' '.join(words)).strip()
            rows['text'] = clean_tweet
        
        # clean_data = data.drop(columns=['id_str']) //can use this to drop specific column
        self.clean_data_to_saver(data)


    def clean_data_to_saver(self, clean_data):
    
        for index, rows in clean_data.iterrows():
            data_dict = {
                'id_str':rows['id_str'],
                'created_at':rows['created_at'],
                'text':rows['text']
            }

            self.saver.setCollectionCleanTweets(data_dict)



