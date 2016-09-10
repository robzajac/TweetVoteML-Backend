import keys

from pymongo import MongoClient


def init_users():
    # MONGO_URL = os.environ.get('MONGOHQ_URL')
    client = MongoClient(keys.MONGO_URL)

    # Initialize the database
    db = client.app56172051
    iwh_collection = db.iwh_users.find()
    maga_collection = db.maga_users.find()

    for maga_user in maga_collection:
        user_doc = {"tweets": []}
        db.maga_users.update_one({"id": maga_user['id']},
                                 {"$set": user_doc},
                                 upsert=True)

    for iwh_user in iwh_collection:
        user_doc = {"tweets": []}
        db.iwh_users.update_one({"id": iwh_user['id']},
                                {"$set": user_doc},
                                upsert=True)

init_users()
