import twitter
import keys
import codecs


def get_tweets():
    api = twitter.Api(consumer_key=keys.CONSUMER_KEY,
                      consumer_secret=keys.CONSUMER_SECRET,
                      access_token_key=keys.ACCESS_TOKEN,
                      access_token_secret=keys.ACCESS_SECRET,
                      sleep_on_rate_limit=True)

    dates = ['2016-09-04', '2016-09-05',
             '2016-09-06', '2019-09-07',
             '2019-09-08', '2019-09-09',
             '2019-09-10']

    trump_texts = []
    hillary_texts = []

    # Pull tweets from Twitter
    for i in range(0, len(dates) - 1):
        day1 = dates[i]
        day2 = dates[i + 1]

        trump_tweets = api.GetSearch(term='#MakeAmericaGreatAgain',
                                     until=day2,
                                     since=day1,
                                     count=100)

        for tweet in trump_tweets:
            trump_texts.append(tweet.text)

        hillary_tweets = api.GetSearch(term='#ImWithHer',
                                       until=day2,
                                       since=day1,
                                       count=100)

        for tweet in hillary_tweets:
            hillary_texts.append(tweet.text)

    for i in range(0, len(trump_texts)):
        filename = 'train_data2/trump/trump-' + str(i) + '.txt'
        f = codecs.open(filename, 'w', 'utf-8')
        f.write(trump_texts[i])
        f.write('\n')
        f.close()

    for i in range(0, len(hillary_texts)):
        filename = 'train_data2/hillary/hillary-' + str(i) + '.txt'
        f = codecs.open(filename, 'w', 'utf-8')
        f.write(hillary_texts[i])
        f.write('\n')
        f.close()

get_tweets()
