import pytest
from twitter import twitter_process


def test_twitter_process():
    consumer_key = "RLSrphihyR4G2UxvA0XBkLAdl"  # Add your API key here
    consumer_secret = "FTz2KcP1y3pcLw0XXMX5Jy3GTobqUweITIFy4QefullmpPnKm4"  # Add your API secret key here
    df = twitter_process(consumer_key, consumer_secret)
    assert len(df) > 0
