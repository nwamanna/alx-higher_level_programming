#!/usr/bin/python3
""" This script takes in a URL, sends a request to the URL
    and displays the value of the X-Request-Id variable
    found in the header of the response.
"""
if __name__ == "__main__":
    import sys
    import requests

    Url = sys.argv[1]

    r = requests.get(Url)
    print(r.headers["X-Request-Id"])
