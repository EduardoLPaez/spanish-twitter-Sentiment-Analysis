import pandas as pd
import langid
from langdetect import detect

# thse functions determine the language of the input text.
# in this case tweets. 
# there are two for the original testing purposes and later expansion and improvement possibilities
def langid_safe(tweet):
    try:
        return langid.classify(tweet)[0]
    except Exception as e:
        print('error in 1')
        pass

def langdetect_safe(tweet):
    try: 
        return detect(tweet)
    except Exception as e:
        print('error in 2')
        pass


# this function just putsthem together and is called from main.py
def cleaning(tweets, ext_):
    tweets['lang_langid'] = tweets['tweets'].apply(langid_safe) 
    tweets['lang_langdetect'] = tweets['tweets'].apply(langdetect_safe)
    
    return tweets

