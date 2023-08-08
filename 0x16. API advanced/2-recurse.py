#!/usr/bin/python3
"""Returns a list containing the titles of all the hot topics in a subreddit.
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Returns a list of hot topics."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    params = {'limit': 100, 'after': after}
    headers = {'User-Agent': 'custom'}
    res = requests.get(url, headers=headers, params=params,
                       allow_redirects=False)
    if res.status_code == 404:
        return None
    after = res.json().get('data').get('after')
    posts = res.json().get('data').get('children')
    post_titles = [post['data']['title'] for post in posts]
    hot_list.extend(post_titles)
    if after is None:
        return hot_list
    else:
        return recurse(subreddit, hot_list, after)
