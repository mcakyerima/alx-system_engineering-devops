#!/usr/bin/python3
"""
Query Reddit API for titles of top ten posts of a given subreddit
"""
import requests


def top_ten(subreddit):
    """
    Return top ten titles for a given subreddit.
    Return None if an invalid subreddit is given.
    """

    headers = requests.utils.default_headers()
    headers.update({'User-Agent': 'My User Agent 1.0'})

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    response = requests.get(url, headers=headers).json()
    top_ten_posts = response.get('data', {}).get('children', [])

    if not top_ten_posts:
        return None

    for post in top_ten_posts:
        title = post.get('data', {}).get('title')
        print(title)
