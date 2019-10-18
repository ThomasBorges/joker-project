import pandas as pd 
import re 
from nltk.tokenize import WordPunctTokenizer
from saver import Saver

newSaver = Saver()
data = pd.DataFrame(list(newSaver.getCollectionRealTimeTweets()))

#uncomment if you want to visualize with a csv file
# with open('tmpcsv.csv', 'w') as tmpcsv:
#     tmpcsv.writelines(data.to_csv())


def clean_frame(data):

    for index, rows in data.iterrows():
        user_removed = re.sub(r'@[A-Za-z0-9]+','',rows['text'])
        link_removed = re.sub('https?://[A-Za-z0-9./]+','',user_removed)
        # number_removed = re.sub('[^a-zA-Z]', ' ', link_removed)
        lower_case_tweet= link_removed.lower()
        tok = WordPunctTokenizer()
        words = tok.tokenize(lower_case_tweet)
        clean_tweet = (' '.join(words)).strip()
        rows['text'] = clean_tweet
    
    # clean_data = data.drop(columns=['id_str'])
    return data


clean_data = clean_frame(data)


def clean_data_to_saver(clean_data):
 
    for index, rows in clean_data.iterrows():
        data_dict = {
            'id_str':rows['id_str'],
            'created_at':rows['created_at'],
            'text':rows['text']
        }

        newSaver.setCollectionCleanTweets(data_dict)


clean_data_to_saver(clean_data)
