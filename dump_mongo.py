import keys
import codecs
import os

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
            filename = 'train_data/trump/trump' + str(trump_count) + '.txt'
            # Obtaining the train/test data split
            if trump_count < 36714:
                f = codecs.open(filename, 'w', 'utf-8')
                f.write(tweet)
                f.write('\n')
                f.close()
            else:
                os.remove(filename)
                new_file = 'test_data/trump/trump' + str(trump_count) + '.txt'
                f = codecs.open(new_file, 'w', 'utf-8')
                f.write(tweet)
                f.write('\n')
                f.close()

            trump_count += 1

    for iwh_user in iwh_users.find():
        for tweet in iwh_user['tweets']:
            filename = 'train_data/hillary/hillary' + str(hillary_count) + '.txt'
            # Obtaining the train/test data split
            if hillary_count < 49127:
                f = codecs.open(filename, 'w', 'utf-8')
                f.write(tweet)
                f.write('\n')
                f.close()
            else:
                os.remove(filename)
                new_file = 'test_data/hillary/hillary' + str(trump_count) + '.txt'
                f = codecs.open(new_file, 'w', 'utf-8')
                f.write(tweet)
                f.write('\n')
                f.close()

dump_mongo()
