import twitter
import os
import pymongo

from pymongo import MongoClient
from keys import *

def get_users():
	MONGO_URL = os.environ.get('MONGOHQ_URL')
	client = MongoClient(MONGO_URL)

	# Initialize the database
	db = client.app56172051
	iwh_collection = db.iwh_users
	maga_collection = db.maga_users

	api = twitter.Api(consumer_key=CONSUMER_KEY,
					  consumer_secret=CONSUMER_SECRET,
					  access_token_key=ACCESS_TOKEN,
					  access_token_secret=ACCESS_SECRET,
					  sleep_on_rate_limit=True)

	trump_set = set()
	hillary_set = set()

	# Trump data
	for i in range(1, 51):
		trump_users = api.GetUsersSearch(term="#MakeAmericaGreatAgain", page=i)
		trump_user_ids = []
		for user in trump_users:
			# trump_user_ids.append(user.id)
			user_doc = {"name": user.name,
					"id": user.id}
			maga_collection.insert_one(user_doc)
		temp_set = set(trump_user_ids)
		trump_set |= temp_set

	# Hillary data
	for i in range(1, 51):
		hillary_users = api.GetUsersSearch(term="#ImWithHer", page=i)
		hill_user_ids = []
		for user in hillary_users:
			# hill_user_ids.append(user.id)
			user_doc = {"name": user.name,
					"id": user.id}
			iwh_collection.insert_one(user_doc)
		temp_set = set(hill_user_ids)
		hillary_set |= temp_set

	print "TRUMP: " + str(len(trump_set))
	print "HILL: " + str(len(hillary_set))