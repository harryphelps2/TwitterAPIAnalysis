import json
import tweepy
from tweepy import OAuthHandler


CONSUMER_KEY = 'I1Ycv8XOnLO5qRQWzTlRfpLck'
CONSUMER_SECRET = '9o1KPQAz3IKhfFKpgmJVmWd98mKbcfygZRJiJjsrlliVqAVpl1'
OAUTH_TOKEN = '1023683241851727877-c1GgatpwJevVM5AJCWtib7ByQTbwXz'
OAUTH_TOKEN_SECRET = 'eadjIwcAQwIlMy9Spip9ObkvU5nqkHdzkUxpCxCscNb4V'

auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

api = tweepy.API(auth)

DUB_WOE_ID = 560743
LON_WOE_ID = 44418

dub_trends = api.trends_place(DUB_WOE_ID)
lon_trends = api.trends_place(LON_WOE_ID)

dub_trends_set = set([trend['name']
                    for trend in dub_trends[0]['trends']])

lon_trends_set = set([trend['name']
                    for trend in lon_trends[0]['trends']])

common_trends = set.intersection(dub_trends_set, lon_trends_set)

print(common_trends)