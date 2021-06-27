import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tweepy as tw
import re
from nltk.corpus import stopwords
from wordcloud import WordCloud, ImageColorGenerator

#API
consumer_key= '381Ft3ejVmHqzKvdRRi1w0AU3'
consumer_secret= 'chYg6MJBS1D5Esybprdi1lgs1hB1puFq1NpbWfZpoVu1vZ3Kx7'
access_token= '1264992766724956164-levtRzn2xocodJEvAWJ69AQmPiLyeh'
access_token_secret= '7jnZ3XaICV751yViEoubFpXX5A4wt2YiuVppd9NVdegQv'

auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)

#Scraping
tweets_covid=tw.Cursor(api.search,q='covid',lang='id').items(10000)
tweets_list=[tweet.text for tweet in tweets_covid]
tweet_df=pd.DataFrame(tweets_list,columns=['Text'])

#Cleaning
def cleanTxt(text):
    text = re.sub('@[A-Za-z0–9]+', '', text) #Removing @mentions
    text = re.sub('#', '', text) # Removing '#' hash tag
    text = re.sub('RT[\s]+', '', text) # Removing RT
    text = re.sub('https?:\/\/\S+', '', text) # Removing hyperlink
    return text
tweet_df['Text'] = tweet_df['Text'].apply(cleanTxt)

#Stop words
nltk.download('stopwords')
stop_words=stopwords.words('indonesian')
cleaned_data=[]
for i in range(len(tweet_df['Text'])):
   tweet=re.sub('[^a-zA-Z]',' ',tweet_df['Text'].iloc[i])
   tweet=tweet.lower().split()
   tweet=[word for word in tweet if(word not in stop_words)]
   tweet=' '.join(tweet)
   cleaned_data.append(tweet)

#Wordcloud
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
plt.savefig('wordcloud_covid.png', facecolor='k', bbox_inches='tight')
