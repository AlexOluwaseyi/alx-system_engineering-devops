#!/usr/bin/python3
"""
A python script that retruns the number of (all-time)
subscribers of a subreddit.
"""

import requests
import sys


def get_sub(subreddit=None):
    """
    A function def to get the number of (all time subscribers
    of a subreddit. """
    if len(sys.argv) != 2:
        sys.exit(1)
    else:
        subreddit = sys.argv[1]

    if subreddit is None:
        return 0

    headers = {'User-Agent': 'CustomUserAgent/1.0'}

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    resp = requests.get(url)
    if resp.status_code == "200":
        body = resp.json()
        subscribers = body["data"]["subscribers"]
        print(subscribers)
        return subscribers
    else:
        return 0


if __name__ == "__main__":
    """
    Main guard
    """
    get_sub()
