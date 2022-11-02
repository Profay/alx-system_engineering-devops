#!/usr/bin/python3
"""prints the titles of the first 10 hot posts listed
    https://towardsdatascience.com/
    how-to-use-the-reddit-api-in-python-5e05ddfd1e5c"""

import requests


def top_ten(subreddit):
    """function returns the top 10 hot posts"""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {'User-Agent': 'My User Agent 1.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code >= 300:
        print('None')
    else:
        for post in response.json()['data']['children']:
            print(post['data']['title'])
