#!/usr/bin/python3
"""Displays the total number of subscribers for a subreddit
Dependency:
    -> Reddit API (https://www.reddit.com/r/{subreddit}/{listing}.json
"""
import requests


def number_of_subscribers(subreddit):
    """Returns number of subreddit subscribers."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    res = requests.get(url, headers={'User-Agent': 'custom'},
                       allow_redirects=False)
    if res.status_code == 404:
        return 0
    data = res.json()
    num_subscribers = data['data']['subscribers']
    return num_subscribers
