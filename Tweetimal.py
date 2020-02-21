import tweepy
from collections import Counter 
import json
import datetime as DT
import re
from textblob import TextBlob


def extracturl(str):
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", str).split())
def polarity(text):
    text=TextBlob(extracturl(text))
    return text.sentiment.polarity


consumer_key = "YfD8MrREfrQ6sh8usT4pKzUcs" 
consumer_secret = "67sLKldEn1EJ8x1ZrbV5ye3BSylQzRAMGFoSTlCHriG3kQur9f"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
access_key = "1184009183542145025-Qyelai6cGKHVECW8FwqGxkGBdzPm4R"
access_secret = "wbj0EllQ5LIM4MCvskvZv8q8MMRxiAXo3aBdvBCvthV44"
auth.set_access_token(access_key, access_secret) 
api = tweepy.API(auth)
trends = api.trends_place(1)
username="twitter-handle"
number_of_tweets=200
MAX_TWEETS = 100
location=[]
language=[]
user=[]
t=[]
tags=[]
positive=0
negative=0
today = DT.date.today()
week_ago = today - DT.timedelta(days=7)
for tweet in tweepy.Cursor(api.search, q='bmw',result_type='popular',count=1000,since_id=week_ago).items():
    location.append(tweet.user.location)
    language.append(tweet.lang)
    user.append(tweet.user.screen_name)
    t.append(polarity(tweet.text))
    tags.extend(re.findall("[#]\w+",tweet.text))
   

while '' in location: location.remove('')
while [] in tags:tags.remove([])


for polarity in t:
    if polarity>0:
        positive+=1
    elif polarity<0:
        negative+=1
        
c=Counter(location)
u=Counter(user)
h=Counter(tags)
l=Counter(language)

print("\n::::",c,"\n::::",l,"\n::::",u)
print("\n\n\n",h)

print("Positive::::",(100*(positive/len(location))),"Negative:::",(100*negative/len(location)))





