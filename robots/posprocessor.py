from saver import Saver
import pandas as pd

saver = Saver()

clean_tweets = pd.DataFrame(list(saver.get_collection('cleanTweets2')))
analy_tweets = pd.DataFrame(list(saver.get_collection('analyTweets')))

combined = pd.concat([clean_tweets, analy_tweets], axis=1)
combined.columns = ['idClean', 'idtweet', 'created_at', 'text', 'idAnaly', 'idtweetAnaly', 'score', 'magnitude']
combined = combined.drop(columns=['idClean','idtweet', 'idAnaly', 'idtweetAnaly'])


def separe_date(data):
    day = []
    hour = []
    for i, row in data.iterrows():
        date = str(row['created_at'])
        date = date.split()
        day.append(date[2])
        hour.append(date[3])
        
    return [day, hour]


row_list = separe_date(combined)

combined['day'] = row_list[0]
combined['hour'] = row_list[1]

data_set = combined.drop('created_at', axis=1)

def organize_score(data):
    score = []
    for i, row in data.iterrows():
        if row['score'] > -0.25 and row['score'] < 0.25:
            score.append('Neutral')
        elif row['score'] <= -0.25:
            score.append('Negative')
        elif row['score'] >= 0.25:
            score.append('Positive')
        
    return score


data_sets = organize_score(data_set)

data_set['score_label'] = data_sets


with open('tweets_analyzed.csv', 'w') as datas:
    csvdata_set = data_set.to_csv()
    datas.write(csvdata_set)