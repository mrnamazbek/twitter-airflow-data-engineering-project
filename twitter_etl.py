import tweepy
import pandas as pd
import json
from datetime import datetime
import s3fs

#1: H937Qxph85S6DkicHCR8E2ZEE
#2: 5GBbBVeYYngwhH7E2eLH6uiqY9d8D3k9OB8x3zFB29p1reN0tX
#3: bearer toke: AAAAAAAAAAAAAAAAAAAAAD0wxQEAAAAAKXyFCAp1EWIgUfcQVworDt7ovmc%3Dlbz24pBSnct85npRlcZbFrp4vRccw7faC40xu8A9e06Vn7MR7T
#4: access token: 1863259480437235712-c3z1fDyNR5vwCLaZQ0PQ1hrCaJHtqA
#5: access secret: nFbnkiE9b9ywfmRshLjfUDW0VUObFPhIWkyJehnNwJasV

import tweepy
import pandas as pd


def run_twitter_etl():
    bearer_token = "AAAAAAAAAAAAAAAAAAAAAD0wxQEAAAAAKXyFCAp1EWIgUfcQVworDt7ovmc%3Dlbz24pBSnct85npRlcZbFrp4vRccw7faC40xu8A9e06Vn7MR7T"

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