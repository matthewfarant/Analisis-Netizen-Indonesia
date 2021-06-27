#sentiment analysis
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tweepy as tw

consumer_key= '381Ft3ejVmHqzKvdRRi1w0AU3'
consumer_secret= 'chYg6MJBS1D5Esybprdi1lgs1hB1puFq1NpbWfZpoVu1vZ3Kx7'
access_token= '1264992766724956164-levtRzn2xocodJEvAWJ69AQmPiLyeh'
access_token_secret= '7jnZ3XaICV751yViEoubFpXX5A4wt2YiuVppd9NVdegQv'

auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)

tweets_covid= tw.Cursor(api.search,q='covid',lang="id",since='2021-01-01').items(5)
[tweet.text for tweet in tweets_covid]
