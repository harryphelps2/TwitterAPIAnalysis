import tweepy
from tweepy import OAuthHandler

CONSUMER_KEY = 'I1Ycv8XOnLO5qRQWzTlRfpLck'
CONSUMER_SECRET = '9o1KPQAz3IKhfFKpgmJVmWd98mKbcfygZRJiJjsrlliVqAVpl1'
OAUTH_TOKEN = '1023683241851727877-c1GgatpwJevVM5AJCWtib7ByQTbwXz'
OAUTH_TOKEN_SECRET = 'eadjIwcAQwIlMy9Spip9ObkvU5nqkHdzkUxpCxCscNb4V'

auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

api = tweepy.API(auth)

for status in tweepy.Cursor(api.home_timeline).items(10):
    print(status.text)