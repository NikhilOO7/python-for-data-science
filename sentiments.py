import tweepy

from textblob import TextBlob

consumer_key = 'mZTUTgjwzujV1TnbUcG7htJAT'

consumer_secret = 'WWyKReMcKLCpdTnsjeyUrTFiTg4cowB8uCd94UIlTZ3Cm9rynK'

access_token = '1562516754-dV5SYxvpS8jAodMMnEOi1GBDXykyK8bq7k0tRJM'

access_token_secret = 'LHj0WwPFaCi27ASHEJlLkDTY8U0msIKhYPoeUorriidS9'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Narender Modi')


for tweet in public_tweets:

	print(tweet.text)

	analysis = TextBlob(tweet.text)

	print(analysis.sentiment)

	print()