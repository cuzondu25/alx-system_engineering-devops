#!/usr/bin/python3
""" a function that queries the Reddit API
returns the number of subscribers"""
import requests

def number_of_subscribers(subreddit):
    """Return number of subscribers (not active users, total subscribers)"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        return 0
    results = response.json().get("data")
    return result.get("subscribers")
