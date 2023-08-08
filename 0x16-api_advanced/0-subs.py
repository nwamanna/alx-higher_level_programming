#!/usr/bin/python3
""" This script queries the Reddit API and returns the number of
    subscribers (not active users, total subscribers) for a
    given subreddit.If an invalid subreddit is given, the
    function should return 0.
"""
import requests

def number_of_subscribers(subreddit):
    # Set a custom User-Agent to avoid Too Many Requests error
    headers = {'User-Agent': 'Custom User-Agent'}

    # Construct the URL for the subreddit's API endpoint
    url = f'https://www.reddit.com/r/{subreddit}/about.json'

    # Send a GET request to the API endpoint
    response = requests.get(url, headers=headers)

    # Check if the response is successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()

        # Extract the number of subscribers
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        # If the response is not successful, return 0
        return 0
