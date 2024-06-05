#!/usr/bin/python3
"""queries the Reddit API"""
import requests


def top_ten(subreddit):
    """ function that queries the Reddit API and prints the titles
	of the first 10 hot posts listed for a given subreddit.
    """
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    header = {"User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"}
    param = {"limit": 10}
    response = requests.get(url, headers=header, params=param,
                            allow_redirects=False)
    if response.status_code == 404:
        print("None")
        return
    results = response.json().get("data")
    [print(c.get("data").get("title")) for c in results.get("children")]
