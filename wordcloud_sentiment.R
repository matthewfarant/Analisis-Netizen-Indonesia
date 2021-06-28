#package
library(tidyverse)
library(wordcloud)
library(tidytext)
library(textclean)

#df from https://colab.research.google.com/drive/11yOLcGYp02OhZdgkDdr99h5VRFi1Rx5S#scrollTo=QEaZVxLMXCwY
df_fin %>% 
  select(-X1)->df_fin
View(df_fin)
#flip polarity
keywords<-c('positif','negatif','tinggi')
for(i in 1:nrow(df_fin)){
  if(grepl(paste(keywords, collapse="|"),
           df_fin$text[i],
           ignore.case = TRUE)&
     df_fin$pred[i]!=0){
    df_fin$pred[i]<-df_fin$pred[i]*(-1)
  }
}
#separate
text_positive<-df_fin %>% 
  filter(pred==1) %>% 
  select(text)
text_negative<-df_fin %>% 
  filter(pred==-1) %>% 
  select(text)
#cleaning
text_positive$text %>% 
  str_to_lower() %>% 
  replace_contraction() %>% 
  replace_url() %>% 
  replace_non_ascii() %>% 
  strip() -> text_positive
text_negative$text %>% 
  str_to_lower() %>% 
  replace_contraction() %>% 
  replace_url() %>% 
  replace_non_ascii() %>% 
  strip() -> text_negative
#tokenizations
enframe(text_positive,value='tweets',name = NULL) %>% 
  unnest_tokens(tweets,tweets) %>% 
  count(tweets,sort=TRUE) %>% 
  anti_join(stop_words_indo,by=c('tweets'='word')) -> wordz_positif
enframe(text_negative,value='tweets',name = NULL) %>% 
  unnest_tokens(tweets,tweets) %>% 
  count(tweets,sort=TRUE) %>% 
  anti_join(stop_words_indo,by=c('tweets'='word')) -> wordz_negatif
#wordcloud
par(mfrow=c(1,2))
wordz_positif %>% 
  with(
    wordcloud(
      words=tweets,
      freq=n,
      max.words = 60,
      random.order = FALSE,
      colors = brewer.pal(name='Dark2',12),
      scale = c(3.5,0.25)
    )
  )
wordz_negatif %>% 
  with(
    wordcloud(
      words=tweets,
      freq=n,
      max.words = 60,
      random.order = FALSE,
      colors = brewer.pal(name='Dark2',12),
      scale = c(3.5,0.25)
    )
  )


