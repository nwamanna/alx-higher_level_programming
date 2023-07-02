#!/usr/bin/python3
""" This script takes in a URL and displays
    the body of the response
    (decoded in utf-8)
"""
if __name__ == "__main__":
    import sys
    import urllib.request
    import urllib.error

    Url = sys.argv[1]
    try:
        with urllib.request.urlopen(Url) as r:
            print(r.read().decode('UTF-8'))
    except urllib.error.HTTPError as e:
        print('Error code:', e.code)
