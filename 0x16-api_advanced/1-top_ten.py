#!/usr/bin/python3
""" This script queries the Reddit API and prints the titles of
    the first 10 hot posts listed for a given subreddit.
"""
import requests

def top_ten(subreddit):
    # Set a custom User-Agent to avoid Too Many Requests error
    headers = {'User-Agent': 'Custom User-Agent'}

    # Construct the URL for the subreddit's hot posts API endpoint
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'

    # Send a GET request to the API endpoint
    response = requests.get(url, headers=headers)

    # Check if the response is successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()

        # Extract the list of posts
        posts = data['data']['children']

        # Print the titles of the first 10 posts
        for post in posts:
            title = post['data']['title']
            print(title)
