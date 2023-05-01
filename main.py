from secrets import *

import tweepy
from pymongo import MongoClient

client = MongoClient("mongodb://dio:dio@localhost:27017/")

db = client.my_test

tweets_collection = db.tweets

tweets_collection.insert_one({"author": "teste", "text": "text qualquer"})

tweets = tweets_collection.find({})

print(list(tweets))

BRAZIL_WDE_ID = 23424768

auth = tweepy.OAuthHundler(consumer_key=CONSUMER_KEY, consumer_secret=CONSUMER_SECRET)

auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

trends = api.trends_place(BRAZIL_WDE_ID)

for tweet in trends:
    print(tweet)

