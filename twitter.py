import tweepy
import pandas as pd
import time


def twitter_process(consumer_key, consumer_secret):
    auth = tweepy.AppAuthHandler(consumer_key, consumer_secret)
    api = tweepy.API(auth)
    tweets_list = []
    start_time = time.time()
    tweet_count = 0
    for tweet in tweepy.Cursor(api.search_tweets, q='bieber').items():
        tweets_list.append(tweet)
        tweet_count = tweet_count + 1
        duration = time.time() - start_time
        if tweet_count == 100 or duration >= 30:
            break
    tweet_format = []
    for tweet in tweets_list:
        tweet_message = "{message_id=" + str(tweet.id) + ", " + "message_creation_date=" + str(tweet.created_at) + ", " \
                        + "message=" + tweet.text + ", " + "Author=" + tweet.user.name + " : " + "user_id=" + str(tweet.user.id) \
                        + ", user_name=" + tweet.user.name + ", " + "screen_name=" + tweet.user.screen_name + ", "  \
                        + "created_at=" + str(tweet.user.created_at) + "}"
        tweet_format.append([tweet.user.name, tweet_message])
        print(tweet.user.name, tweet_message)

    df = pd.DataFrame(tweet_format, columns=["user", "tweet_messages"])
    res = df.sort_values("user").groupby("user").agg(list)
    with open("test_files", 'w') as outfile:
        res.to_string(outfile)
    return res


if __name__ == "__main__":
    consumer_key = "RLSrphihyR4G2UxvA0XBkLAdl"  # Add your API key here
    consumer_secret = "FTz2KcP1y3pcLw0XXMX5Jy3GTobqUweITIFy4QefullmpPnKm4"  # Add your API secret key here
    twitter_process(consumer_key, consumer_secret)
