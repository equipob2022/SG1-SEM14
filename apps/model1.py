import streamlit as st
from tweepy import tweepy
from textblob import TextBlob
from wordcloud import WordCloud, ImageColorGenerator
from nltk.tokenize import WordPunctTokenizer
import pandas as pd
import numpy as np
import re
from strings import string
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
import nltk
from nltk.corpus import stopwords
nltk.download("stopwords")
def app():
    st.title('Model 1 - SVR')
