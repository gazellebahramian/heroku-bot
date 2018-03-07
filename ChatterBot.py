# Dependencies
import tweepy
import json
import time

# Twitter API Keys
consumer_key = "jy5gVE4OAByPWWTZL6tFp8CtX"
consumer_secret = "foqDmvGgaX34VrGbDnz7xlfVpCkTFr5l78RgywqguaU3m3rgSF"
access_token = "969400010327523328-nKELrQFcIFTbAazfWYcqbGV4nQwQUCw"
access_token_secret = "R34KjYlYUjqgcO6JQOHfGejSAwKVug3AEu1q2n8wXpJdA"

# Setup Tweepy API Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())


# Create a function that tweets
# CODE GOES HERE