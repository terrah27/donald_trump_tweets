import jsonpickle
import tweepy
import pandas as pd

# Variables that contains the user credentials to access Twitter API
ACCESS_TOKEN = '1321649599-t6viRHmWMOqmfPK3tEwJuURiIyCqfpkQlqSlZT4'
ACCESS_SECRET = 'XtxaaF20tHfvcCIDweKTPuVrO3Z7qB8pbmtJmLhKTnk1R'
CONSUMER_KEY = 'EsBXbH3McMXEeFhBupoFhDDwo '
CONSUMER_SECRET = 'RSmyfCvrUaD1JogEBOSsQ5nUez4eAwF7QONnFZnAxUte2gFirI'


# Setup access API
def connect_to_twitter_OAuth():
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

    api = tweepy.API(auth)
    return api


# Create API object
api = connect_to_twitter_OAuth()


def get_save_tweets(filepath, api, query, max_tweets=1000000, lang='pt'):
    tweetCount = 0

    # Open file and save tweets
    with open(filepath, 'w') as f:

        # Send the query
        for tweet in tweepy.Cursor(api.search,
                                   q=query,
                                   lang=lang).items(max_tweets):

            # Convert to JSON format
            f.write(jsonpickle.encode(tweet._json, unpicklable=False) + '\n')
            tweetCount += 1

        # Display how many tweets we have collected
        print("Downloaded {0} tweets".format(tweetCount))


query = '#Haddad OR #Haddad13 OR #HaddadSim OR' \
        '#EleNao OR #EleNunca OR #Bolsonaro OR' \
        '#Bolsonaro17 OR #SomosTodosBolsonaro OR #Bolsonaro2019 OR' \
        '"haddad" OR "bolsonaro"'

# Get those tweets
get_save_tweets('tweets.json', api, query)
