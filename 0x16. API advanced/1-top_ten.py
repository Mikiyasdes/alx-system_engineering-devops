#!/usr/bin/python3
"""Displays the total number of subscribers for a subreddit
Dependency:
    -> Reddit API (https://www.reddit.com/r/{subreddit}/{listing}.json
"""
import requests


def top_ten(subreddit):
    """Returns number of subreddit subscribers."""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    res = requests.get(url, headers={'User-Agent': 'custom'},
                       allow_redirects=False)
    if res.status_code == 404:
        print(None)
    else:
        posts = res.json().get('data').get('children')
        for post in posts:
            title = post.get('data').get('title')
            print(title)
