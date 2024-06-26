#!/usr/bin/python3
"""a recursive function that queries the Reddit API and returns a list containing the titles of all hot articles for a given subreddit."""

import requests

def recurse(subreddit, hot_list=[], after="", count=0):
    """ a recursive function that queries the Reddit API
    Return
        A list containing the titles of all hot articles for a given subreddit
        None is no result was found
    """
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    header = {"User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"}
    params = {"after": after, "count": count, "limit": 100}
    response = requests.get(url, headers=header, params=params, allow_redirects=False)

    if response.status_code == 404:
        return None

    results = response.json().get("data")
    after = results.get("after")
    count += results.get("dist")
    for r in results.get("children"):
        hot_list.append(r.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    return hot_list
