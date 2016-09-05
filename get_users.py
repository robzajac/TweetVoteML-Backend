import twitter
import sys
sys.path.insert(0, '/path/to/keys.py/directory/')

from keys import *

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
		trump_user_ids.append(user.id)
	temp_set = set(trump_user_ids)
	trump_set |= temp_set

# Hillary data
for i in range(1, 51):
	hillary_users = api.GetUsersSearch(term="#ImWithHer", page=i)
	hill_user_ids = []
	for user in hillary_users:
		hill_user_ids.append(user.id)
	temp_set = set(hill_user_ids)
	hillary_set |= temp_set

print "TRUMP: " + str(len(trump_set))
print "HILL: " + str(len(hillary_set))

# Write to Trump file
f_trump = open('data/maga-data.txt','w')

for trump_user in trump_set:
	f_trump.write(str(trump_user) + '\n')

f_trump.close()

# Write to Hillary file
f_hill = open('data/iwh-data.txt', 'w')

for hill_user in hillary_set:
	f_hill.write(str(hill_user) + '\n')

f_hill.close()
