import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
from main import twitter_query
import altair as alt

def overall(frame):
    temp = frame['sentiment'].mean()
    if temp >= 6:
        return 'positive'
    elif temp <= 6 and temp >= 3.1:
        return 'neutral'
    else:
        return 'negative'

def main():
    st.title('Twitter Sentiment Analysis(spanish)')

    # VV pass bellow through spellcheck.
    st.markdown('''This project utilizes the twitter API tweepy to look up the latest 200 tweets
    for a given keyword. at current the program utilizes aylotts's sentipy model for
    classifying the tweets' sentiment. \n
    - The program will determine which if any tweets are in Spanish \n 
        for the given keyword. then does a sentiment analysis on \n
        those that are in Spanish. \n
    - Future plans include adding analysis options for other languages.\n 
    ''')

    text_in = st.text_input('please write a keyword.', 'keyword')
    if text_in != 'keyword':
        df = twitter_query(text_in)

        st.text(f'\nthe overall sentiment for {text_in} is {overall(df)} ')
        # need more perty graphics.......I regret nothing......
        st.altair_chart(
            alt.Chart(df).mark_bar().encode(
                alt.X("sentiment", bin=True),
                y='count()',
            )
        )
        

if __name__ == '__main__':
    main()