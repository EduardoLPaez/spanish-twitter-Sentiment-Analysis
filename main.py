import pandas as pd 
import numpy as np

# sentiment library + related
# language detection.. could be korean for al we know
from language import cleaning # this should create a csv of the casified text
from classifier import SentimentClassifier

clf = SentimentClassifier()
def sentiment(df):
    df['sentiment'] = df.query("lang_langdetect == 'es'")['tweets'].apply(clf.predict)
    # df['sentiment_classification'] = df['sentiment'].apply(sentiment_split)
    return df

# twitter api module.
import tweepy
from important import access_toekn, access_token_secret, consumer_key, consumer_secret

def increment_(frame):
    temp_list = []
    for i in frame['sentiment']:
        if i >= .6:
            temp_list.append(i)
        elif i <= .6 and i >= .31:
            temp_list.append(i)
        else:
            temp_list.append(i)
    frame['increment'] = temp_list
    return frame

def twitter_query(query_, ext_ = 'test' , metions_ = 200):
    # authentifications for twiter api
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_toekn, access_token_secret)
    api = tweepy.API(auth)

    # bellow VVV may have memory issues, check for posible optimizations. 
    # tweets = [status for status in tweepy.Cursor(api.search, q = query_).items(metions_)]
    tweets = api.search([query_],count = metions_) # baseline, not good enough
    end_ = pd.DataFrame(
        data = {
            'tweets' : [tweet.text for tweet in tweets], 
            'datetime' : [tweet.created_at for tweet in tweets]
            }
        )
    class_ = cleaning(end_, ext_)
    class_ = sentiment(class_) 
    return increment_(class_)