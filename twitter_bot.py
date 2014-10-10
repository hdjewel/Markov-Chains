import twitter
# from os import environ
import keys

# consumer_key = environ.get("TWITTER_API_KEY")
# consumer_secret = environ.get("TWITTER_API_SECRET")
# access_token_key = environ.get("TWITTER_ACCESS_TOKEN_KEY")
# access_token_secret = environ.get("TWITTER_ACCESS_TOKEN_SECRET")

consumer_key = keys.TWITTER_API_KEY
consumer_secret = keys.TWITTER_API_SECRET
access_token_key = keys.TWITTER_ACCESS_TOKEN_KEY
access_token_secret = keys.TWITTER_ACCESS_TOKEN_SECRET

api = twitter.Api(consumer_key = consumer_key, 
                consumer_secret =  consumer_secret, 
                access_token_key = access_token_key,
                access_token_secret = access_token_secret)

print api.VerifyCredentials()


# status = api.PostUpdate('''
# I do not like them. SO you say. Try them! Try them! ANd you may. Try them and 
# worship them.
# ''')

# print status