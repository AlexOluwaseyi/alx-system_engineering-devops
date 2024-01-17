#!/usr/bin/python3
"""
A python script that retruns the number of (all-time)
subscribers of a subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """
    A function def to get the number of (all time subscribers
    of a subreddit. """
    if subreddit is None:
        return 0

    headers = {'User-Agent':
               "Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101\
               Firefox/81.0"}

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    resp = requests.get(url)
    if resp.status_code == 200:
        body = resp.json()
        subscribers = body["data"]["subscribers"]
        return subscribers
    else:
        return 0
