import keys
import codecs

from pymongo import MongoClient


def dump_mongo():
    client = MongoClient(keys.MONGO_URL)

    # Initialize the database
    db = client.app56172051
    maga_users = db.maga_users
    iwh_users = db.iwh_users
    trump_count = 0
    hillary_count = 0

    for maga_user in maga_users.find():
        for tweet in maga_user['tweets']:
            filename = 'data/trump/trump' + str(trump_count) + '.txt'
            f = codecs.open(filename, 'w', 'utf-8')
            f.write(tweet)
            f.write('\n')
            f.close()
            trump_count += 1

    for iwh_user in iwh_users.find():
        for tweet in iwh_user['tweets']:
            filename = 'data/hillary/hillary' + str(hillary_count) + '.txt'
            f = codecs.open(filename, 'w', 'utf-8')
            f.write(tweet)
            f.write('\n')
            f.close()
            hillary_count += 1

dump_mongo()
