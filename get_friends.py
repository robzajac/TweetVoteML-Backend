import twitter
from keys import *

api = twitter.Api(consumer_key=CONSUMER_KEY,
				  consumer_secret=CONSUMER_SECRET,
				  access_token_key=ACCESS_TOKEN,
				  access_token_secret=ACCESS_SECRET,
				  sleep_on_rate_limit=True)

