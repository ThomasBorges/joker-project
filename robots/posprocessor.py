from saver import Saver
import pandas as pd


class Posprocessor():

    def __init__(self):
        self.saver = Saver()

        self.clean_tweets = pd.DataFrame(list(self.saver.get_collection('cleanTweets'))) #change here the name of database
        self.analy_tweets = pd.DataFrame(list(self.saver.get_collection('analyTweets')))

    def start_to_posprocess(self):
        print('Starting process')
        
        combined = self.combine_and_drop()
        
        row_list = self.separe_date(combined)
    
        combined['hour'] = row_list

        data_set = combined.copy()

        data_sets = self.organize_score(data_set)

        data_set['score_label'] = data_sets

        with open('tweets_analyzed.csv', 'w') as datas:
            csvdata_set = data_set.to_csv()
            datas.write(csvdata_set)

        print('\ncsv created')


    def combine_and_drop(self):
        combined = pd.concat([self.clean_tweets, self.analy_tweets], axis=1)
        combined.columns = ['idClean', 'idtweet', 'created_at', 'text', 'idAnaly', 'idtweetAnaly', 'score', 'magnitude']
        combined = combined.drop(columns=['idClean','idtweet', 'idAnaly', 'idtweetAnaly'])
        
        return combined


    def separe_date(self, data):
        hour = []
        for i, row in data.iterrows():
            date = str(row['created_at'])
            date = date.split()
            hour.append(date[3])
            
        return hour


    def organize_score(self, data):
        score = []
        for i, row in data.iterrows():
            if row['score'] > -0.25 and row['score'] < 0.25:
                score.append('Neutral')
            elif row['score'] <= -0.25:
                score.append('Negative')
            elif row['score'] >= 0.25:
                score.append('Positive')
            
        return score


    