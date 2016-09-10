import twitter
import keys

from pymongo import MongoClient


def get_users():
    # MONGO_URL = os.environ.get('MONGOHQ_URL')
    client = MongoClient(keys.MONGO_URL)

    # Initialize the database
    db = client.app56172051
    iwh_collection = db.iwh_users
    maga_collection = db.maga_users

    api = twitter.Api(consumer_key=keys.CONSUMER_KEY,
                      consumer_secret=keys.CONSUMER_SECRET,
                      access_token_key=keys.ACCESS_TOKEN,
                      access_token_secret=keys.ACCESS_SECRET,
                      sleep_on_rate_limit=True)

    # Trump data
    for i in range(1, 51):
        trump_users = api.GetUsersSearch(term="#MakeAmericaGreatAgain", page=i)
        for user in trump_users:
            user_doc = {"name": user.name,
                        "id": user.id,
                        "tweets": []}
            maga_collection.update_one(user_doc,
                                       user_doc,
                                       upsert=True)

    # Hillary data
    for i in range(1, 51):
        hillary_users = api.GetUsersSearch(term="#ImWithHer", page=i)
        for user in hillary_users:
            user_doc = {"name": user.name,
                        "id": user.id,
                        "tweets": []}
            maga_collection.update_one(user_doc,
                                       user_doc,
                                       upsert=True)
get_users()
