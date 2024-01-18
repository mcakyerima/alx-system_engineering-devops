#!/usr/bin/python3
"""
Query Reddit API for number of subscribers for a given subreddit
"""

import requests

def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers for a given subreddit.

    Args:
    - subreddit (str): The name of the subreddit.

    Returns:
    - int: The number of subscribers. Returns 0 if the subreddit is invalid.
    """

    # URL for Reddit API to get subreddit information
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    # Set a custom User-Agent to avoid Too Many Requests error
    headers = {"User-Agent": "my-app/1.0"}

    # Make the API request
    response = requests.get(url, headers=headers)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()

        # Extract the number of subscribers
        subscribers = data["data"]["subscribers"]
        return subscribers
    else:
        # Return 0 for an invalid subreddit
        return 0
