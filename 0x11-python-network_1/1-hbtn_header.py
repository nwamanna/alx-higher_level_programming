#!/usr/bin/python3
""" This script takes in a URL, sends a request to the URL
    and displays the value of the X-Request-Id variable
    found in the header of the response.
"""
if __name__ == "__main__":
    import sys
    import urllib.request

    Url = sys.argv[1]

    request = urllib.request.Request(Url)
    with urllib.request.urlopen(request) as response:
        print(dict(response.headers)["X-Request-Id"])
