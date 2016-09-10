import twitter
import keys

from pymongo import MongoClient


def get_users_tweets():
    # MONGO_URL = os.environ.get('MONGOHQ_URL')
    client = MongoClient(keys.MONGO_URL)

    # Initialize the database
    db = client.app56172051
    iwh_users = db.iwh_users.find()
    maga_users = db.maga_users.find()

    api = twitter.Api(consumer_key=keys.CONSUMER_KEY2,
                      consumer_secret=keys.CONSUMER_SECRET2,
                      access_token_key=keys.ACCESS_TOKEN2,
                      access_token_secret=keys.ACCESS_SECRET2,
                      sleep_on_rate_limit=True)

    for maga_user in maga_users:
        try:
            maga_tweets = api.GetUserTimeline(user_id=maga_user['id'],
                                              count=200,
                                              include_rts=False,
                                              exclude_replies=True)
            tweets_text = []

            for tweet in maga_tweets:
                tweets_text.append(tweet.text)

            for tweet in tweets_text:
                update_tweet = {"$addToSet": {"tweets": tweet}}
                db.maga_users.update_one(maga_user,
                                         update_tweet)
        except twitter.error.TwitterError:
            print "Hit an error"

    for iwh_user in iwh_users:
        try:
            iwh_tweets = api.GetUserTimeline(user_id=iwh_user['id'],
                                             count=200,
                                             include_rts=False,
                                             exclude_replies=True)
            tweets_text = []

            for tweet in iwh_tweets:
                tweets_text.append(tweet.text)

            for tweet in tweets_text:
                update_tweet = {"$addToSet": {"tweets": tweet}}
                db.iwh_users.update_one(iwh_user,
                                        update_tweet)
        except twitter.error.TwitterError:
            print "Hit an error"

get_users_tweets()
