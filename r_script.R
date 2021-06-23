## twitter data scraping
library(tidyverse)
library(tidytext)
library(textclean)
library(stringr)
library(rtweet)
library(wordcloud)
library(igraph)
library(ggraph)

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
head(tweets_faisal)
## wordcloud
enframe(tweets_faisal,value='tweets',name = NULL) %>% 
  unnest_tokens(tweets,tweets) %>% 
  count(tweets,sort=TRUE) %>% 
  anti_join(stop_words_indo,by=c('tweets'='word')) -> wordz
wordz %>% 
  filter(!(tweets %in% c('at','number','kian','e','and','d','dr','no','rp')))->wordz
stop_words_indo<-read.table('https://raw.githubusercontent.com/masdevid/ID-Stopwords/master/id.stopwords.02.01.2016.txt',header=T)

wordz %>% 
  with(
    wordcloud(
      words=tweets,
      freq=n,
      max.words = 200,
      random.order = FALSE,
      colors = brewer.pal(name='Dark2',12),
      scale = c(3.5,0.25)
    )
  )

## tokenization

kpk_faisal %>% 
  select(text) %>% 
  unnest_tokens(bigram,text,token='ngrams',n=2)->bigram_faisal
bigram_faisal %>% 
  separate(bigram,c('word1','word2'),sep=' ')->bigram_separated
bigram_separated %>% 
  filter(!word1 %in% stop_words_indo$word) %>% 
  filter(!word2 %in% stop_words_indo$word)->bigram_filtered
bigram_filtered %>% 
  count(word1,word2,sort=T) %>% 
  filter(word1!='https' & word2!='https')->bigram_counts

## netword
bigram_graph<-bigram_counts %>% 
  filter(n>1) %>% 
  graph_from_data_frame()
set.seed(123)
ggraph(bigram_graph,layout='fr')+
  geom_edge_link()+
  geom_node_point()+
  geom_node_text(aes(label = name), vjust = 1, hjust = 1)
View(bigram_counts)
