#!/usr/bin/python3
"""
Count occurrences of keywords in hot articles of a given subreddit
"""
import requests

def count_words(subreddit, word_list, after=None, counts={}):
    """
    Recursive function that queries the Reddit API, parses the title of all hot articles,
    and prints a sorted count of given keywords.

    Args:
    - subreddit (str): The name of the subreddit.
    - word_list (list): List of keywords to count.
    - after (str): The pagination parameter for the API request (default is None).
    - counts (dict): Dictionary to store counts (default is an empty dictionary).

    Returns:
    - None: Results are printed directly.
    """
    headers = requests.utils.default_headers()
    headers.update({'User-Agent': 'My User Agent 1.0'})

    # Update URL each recursive call with the "after" parameter
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    if after:
        url += "?after={}".format(after)

    r = requests.get(url, headers=headers, allow_redirects=False)

    # Parse titles and update counts
    results = r.json().get('data', {}).get('children', [])
    for entry in results:
        title = entry.get('data', {}).get('title', '').lower()
        for word in word_list:
            keyword = word.lower()
            # Exclude variations like java. or java! or java_
            if keyword in title and not title.startswith(keyword) and not title.endswith(keyword):
                counts[keyword] = counts.get(keyword, 0) + 1

    # Get the next "after" parameter, or print counts if there's nothing else to recurse
    after = r.json().get('data', {}).get('after')
    if not after:
        sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
        for keyword, count in sorted_counts:
            print("{}: {}".format(keyword, count))
        return

    count_words(subreddit, word_list, after, counts)
