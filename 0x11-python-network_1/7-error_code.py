#!/usr/bin/python3
""" This script takes in a URL and displays
    the body of the response
    (decoded in utf-8)
"""
if __name__ == "__main__":
    import sys
    import requests

    Url = sys.argv[1]

    r = requests.get(Url)
    if r.status_code >= 400:
        print("Error code: {}".format(r.status_code))
    else:
        print(r.text)
