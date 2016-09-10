import twitter
import keys
from sklearn.externals import joblib


api = twitter.Api(consumer_key=keys.CONSUMER_KEY2,
                  consumer_secret=keys.CONSUMER_SECRET2,
                  access_token_key=keys.ACCESS_TOKEN2,
                  access_token_secret=keys.ACCESS_SECRET2,
                  sleep_on_rate_limit=True)


def process_username(username):
    # Load model from hard drive
    text_clf = joblib.load('model/tweets_classifier.joblib.pk1')

    # Get tweets
    tweets = api.GetUserTimeline(screen_name=username, count=200)

    texts = []
    for tweet in tweets:
        texts.append(tweet.text)

    # 0 for Hillary, 1 for Trump
    predicted = text_clf.predict(texts)

    trump_count = 0
    hillary_count = 0

    for i in range(0, len(texts)):
        if predicted[i] == 0:
            hillary_count += 1
        else:
            trump_count += 1

    # 0 for Hillary, 1 for Trump
    orientation = 0

    if trump_count >= hillary_count:
        orientation = 1

    ratio = max(trump_count, hillary_count) * 1.0 / len(texts)

    # Calculatino to get number of tweets for each candidate
    print trump_count
    print hillary_count
    print ratio
