import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tweepy as tw
import re
import nltk
from nltk.corpus import stopwords
from wordcloud import WordCloud, ImageColorGenerator
from airflow.models import Variable

def run_twitter_etl():
    #authentication (confidential)
    consumer_key= Variable.get('TWITTER_CONSUMER_KEY')
    consumer_secret= Variable.get('TWITTER_CONSUMER_SECRET')
    access_token= Variable.get('TWITTER_ACCESS_TOKEN')
    access_token_secret= Variable.get('TWITTER_ACCESS_TOKEN_SECRET')
    auth = tw.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tw.API(auth, wait_on_rate_limit=True)
    #scraping
    tweets_scrap=tw.Cursor(api.search,q='covid',lang='id').items(100)
    tweets_list=[tweet.text for tweet in tweets_scrap]
    tweet_df=pd.DataFrame(tweets_list,columns=['Text'])
    #cleaning
    def text_clean(text):
        text = re.sub('@[A-Za-z0–9]+', '', text) #Removing @mentions
        text = re.sub('#', '', text) # Removing '#' hash tag
        text = re.sub('RT[\s]+', '', text) # Removing RT
        text = re.sub('https?:\/\/\S+', '', text) # Removing hyperlink
        return text
    tweet_df['Text'] = tweet_df['Text'].apply(text_clean)
    nltk.download('stopwords')
    stop_words=stopwords.words('indonesian')
    cleaned_data=[]
    for i in range(len(tweet_df['Text'])):
        tweet=re.sub('[^a-zA-Z]',' ',tweet_df['Text'].iloc[i])
        tweet=tweet.lower().split()
        tweet=[word for word in tweet if(word not in stop_words)]
        tweet=' '.join(tweet)
        cleaned_data.append(tweet)
    #wordcloud
    allWords = ' '.join(cleaned_data)
    wordCloud = WordCloud(colormap="Accent",
                    width=1600,
                    height=800,
                    random_state=30,
                    max_font_size=200,
                    min_font_size=20).generate(allWords)
    plt.figure(figsize=(20,10), facecolor='k')
    plt.imshow(wordCloud, interpolation="bilinear")
    plt.axis('off')
    plt.show()
    plt.savefig('wordcloud.png', facecolor='k', bbox_inches='tight')

def run_twitter_post():
    #authentication (confidential)
    consumer_key= Variable.get('TWITTER_CONSUMER_KEY')
    consumer_secret= Variable.get('TWITTER_CONSUMER_SECRET')
    access_token= Variable.get('TWITTER_ACCESS_TOKEN')
    access_token_secret= Variable.get('TWITTER_ACCESS_TOKEN_SECRET')
    auth = tw.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tw.API(auth, wait_on_rate_limit=True)
    #post
    api.update_with_media('wordcloud.png','[Testing] Covid wordcloud for today')
