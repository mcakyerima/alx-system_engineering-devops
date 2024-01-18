#!/usr/bin/python3
"""
Query Reddit API for number of subscribers for a given subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """
        return number of subscribers for a given subreddit
        return 0 if invalid subreddit given
    """
    if subreddit is None or not isinstance(subreddit, str):
        return 0

    headers = {'User-agent': 'MYAPI/0.0.1'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    response = requests.get(url, headers=headers)
    data = response.json()

    try:
        return data.get('data').get('subscribers')

    except Exception:
        return 0
