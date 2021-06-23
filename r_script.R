#twitter data scraping
library(tidyverse)
library(tidytext)
library(textclean)
library(stringr)
library(rtweet)

tweet_faisal<-get_timeline(user='@faisalbasri',n=3200)
View(tweet_faisal)
