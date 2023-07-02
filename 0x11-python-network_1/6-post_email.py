#!/usr/bin/python3
""" This script takes in a URL and an email, sends a POST
    request to the passed URL with the email as a parameter,
    and displays the body of the response (decoded in utf-8)
"""
if __name__ == "__main__":
    import sys
    import requests

    Url = sys.argv[1]
    val = sys.argv[2]
    value = {"email": val}
    request = requests.post(Url, value)
    print(request.text)
