#twitter data scraping
library(tidyverse)
library(tidytext)
library(textclean)
library(stringr)
library(rtweet)

tweet_faisal<-get_timeline(user='@faisalbasri',n=3200)
View(tweet_faisal)

kpk_faisal<-tweet_faisal %>% 
  filter(grepl('KPK',text,ignore.case = T))

kpk_faisal$text %>% 
  str_to_lower() %>% 
  replace_contraction() %>% 
  replace_symbol() %>% 
  replace_url() %>% 
  replace_emoji() %>% 
  strip()->tweets_faisal

write.csv(tweets_faisal,'tweets_faisal.csv')
