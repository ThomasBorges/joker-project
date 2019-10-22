from nltk.tokenize import WordPunctTokenizer
from saver import Saver
import pandas as pd 
import re 


class Preprocessor():
    def __init__(self):
        self.saver = Saver()


    def clean_frame(self, data):
        print('\n---Cleaning user and links---\n')

        for index, rows in data.iterrows():
            user_removed = re.sub(r'@[A-Za-z0-9]+','',rows['text'])
            link_removed = re.sub('https?://[A-Za-z0-9./]+','',user_removed)
            # number_removed = re.sub('[^a-zA-Z]', ' ', link_removed) //you can use this to remove punctuation
            lower_case_tweet= link_removed.lower()
            tok = WordPunctTokenizer()
            words = tok.tokenize(lower_case_tweet)
            clean_tweet = (' '.join(words)).strip()
            rows['text'] = clean_tweet
        
        # clean_data = data.drop(columns=['id_str']) //you can use this to drop specific column
        self.remove_duplicates_and_save(data)


    def remove_duplicates_and_save(self, clean_data):
        print('---Removing duplicates and saving in mongo---\n')
        check_list = []
        for index, rows in clean_data.iterrows():
            if rows['text'] not in check_list: 
                check_list.append(rows['text'])
                data_dict = {
                    'id_str':rows['id_str'],
                    'created_at':rows['created_at'],
                    'text':rows['text']
                }
                self.saver.set_collection_clean_tweets(data_dict)



