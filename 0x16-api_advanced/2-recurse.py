#!/usr/bin/python3
"""
Recursively query Reddit API for titles of hot articles in a given subreddit
"""
import requests

def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively queries the Reddit API and returns a list containing the titles
    of all hot articles for a given subreddit.

    Args:
    - subreddit (str): The name of the subreddit.
    - hot_list (list): The list to store titles (default is an empty list).
    - after (str): The pagination parameter for the API request (default is None).

    Returns:
    - list: The list containing titles of hot articles. Returns None if the subreddit is invalid.
    """
    headers = requests.utils.default_headers()
    headers.update({'User-Agent': 'My User Agent 1.0'})

    # Update URL each recursive call with the "after" parameter
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    if after:
        url += "?after={}".format(after)

    r = requests.get(url, headers=headers, allow_redirects=False)

    # Append top titles to hot_list
    results = r.json().get('data', {}).get('children', [])
    if not results:
        return hot_list
    for e in results:
        hot_list.append(e.get('data').get('title'))


    after = r.json().get('data', {}).get('after')
    if not after:
        return hot_list
    return recurse(subreddit, hot_list, after)
