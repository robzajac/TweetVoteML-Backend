# TweetVoteML - http://tweetvoteml.herokuapp.com

We decided to see who Twitter users are voting for in the 2016 election based on their tweets.

## How it Works
We used Twitter's API to find Twitter users who have tweeted #MakeAmericaGreatAgain or #ImWithHer. Our app labeled these users as Trump or Hillary supporters respectively. We then pulled 200 tweets from each person, labeled them as "Trump" or "Hillary", and added them to our database in MongoDB. This approach gave us over 100,000 tweets in our training set.

Our app vectorized each tweet to obtain a raw count of words that appeared in "Trump" tweets and "Hillary" tweets. It learned to recognize words that appear most often in tweets from either side using a logistic regression classifier in Scikit-Learn.

On the frontend, we take in any public Twitter user and fetch their most recent 200 tweets. Our model classifies each tweet and we obtain a ratio of "Trump" tweets to "Hillary" tweets for the user. The ratio represents who we think the user will vote for and how likely we think our prediction is. 

## Repo Contents
Scripts to pull tweets from users, dump our Mongo database to local text files, train our model, and process a username given to the app on the frontend.

## Technologies Used
Flask, Scikit-Learn, MongoDB, Twitter API

## Credits
Frontend built by William Brown.
See frontend at: https://github.com/wibrown/TweetVoteML

Built at PennApps XIV.
