import tweepy
import pandas as pd
import json
from datetime import datetime
import s3fs

#1: ***********
#2: *************************
#3: bearer toke: ******************************************************
#4: access token: ********************************************
#5: access secret: ********************************************

import tweepy
import pandas as pd


def run_twitter_etl():
    bearer_token = "your_bearer_token"

    # Create a client connection
    client = tweepy.Client(bearer_token=bearer_token)

    # Fetch tweets using the Tweepy Client method for Twitter API v2
    response = client.get_users_tweets(id='44196397',  # elonmusk's ID
                                       tweet_fields=['created_at', 'public_metrics'],
                                       max_results=100)

    list_of_tweets = []

    if response.data:
        for tweet in response.data:
            refined_tweet = {
                "id": tweet.id,
                "text": tweet.text,
                "created_at": tweet.created_at,
                "retweet_count": tweet.public_metrics['retweet_count'],
                "like_count": tweet.public_metrics['like_count']
            }
            list_of_tweets.append(refined_tweet)

    df = pd.DataFrame(list_of_tweets)
    df.to_csv('refined_tweets.csv', index=False)


if __name__ == "__main__":
    run_twitter_etl()
