# Analisis Netizen Indonesia

## Background
This is a mini project to create an automated twitter post using Apache Airflow 🕘 </br>
The objective of this project is to observe the daily changes of public (netizen) thoughts towards a certain topic. In the meantime, the daily visualization that will be posted is a wordcloud that represents Indonesian netizens towards the Covid-19 pandemic.

## Data Pipeline
Every 9 AM in Indonesia Local Time (WIB), Airflow will execute a container of tasks (called DAG or Directed Acyclic Graph) that include data scraping, data cleaning, wordcloud making, and twitter posting.
![Flow of Task](https://user-images.githubusercontent.com/64967317/131256569-ccdff803-1b46-4a27-9ee1-2f408f88256b.png)
The tweets data are scraped via standard twitter API, which will later be cleaned (remove stopwords using NLTK data, remove mentions, links, hashtags, etc) and visualized using wordcloud. This task will be automated everyday, which means you will see a wordcloud post in my [twitter account](https://twitter.com/FarantMatthew) every 9 AM.

## Tools that I used
### Operating System : </br>
Linux (Ubuntu WSL) 🐧 </br>
### Softwares: </br>
Python 3.8.10 🐍 </br>
Venv </br>
Apache Airflow 2.1.2 </br>
VSCode </br>
### Libraries: </br>
Airflow </br>
Datetime </br>
Numpy </br>
Pandas </br>
Matplotlib </br>
Tweepy </br>
Re </br>
NLTK </br>
Wordcloud </br>

## On Progress... 👷
I'm currently working on the sentiment analysis of the tweets and explore any other types of visualizations that I can use. So, stay tuned!

