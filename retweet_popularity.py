import json
import tweepy
from tweepy import OAuthHandler
from collections import Counter
from prettytable import PrettyTable
from operator import itemgetter

CONSUMER_KEY = 'I1Ycv8XOnLO5qRQWzTlRfpLck'
CONSUMER_SECRET = '9o1KPQAz3IKhfFKpgmJVmWd98mKbcfygZRJiJjsrlliVqAVpl1'
OAUTH_TOKEN = '1023683241851727877-c1GgatpwJevVM5AJCWtib7ByQTbwXz'
OAUTH_TOKEN_SECRET = 'eadjIwcAQwIlMy9Spip9ObkvU5nqkHdzkUxpCxCscNb4V'

auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

api = tweepy.API(auth)

count = 150
query = 'Ireland'

#Get all tweets for the search query
results = [status for status in tweepy.Cursor(api.search, q=query).items(count)]

min_retweets = 10

pop_tweets = [status
                for status in results
                    if status._json['retweet_count'] > min_retweets]
            
        
tweet_tups = [(tweet._json['text'].encode('utf-8'), tweet._json['retweet_count'])
                for tweet in pop_tweets]

most_popular_tups = sorted(tweet_tups, key=itemgetter(1), reverse=True)[:5]

table = PrettyTable(field_names=['Text', 'Retweet Count'])
for key, val in most_popular_tups:
    table.add_row([key, val])
table.max_width['Text'] = 50
table.align['Text'], table.align['Retweet Count'] = 'l', 'r'
print(table)
    