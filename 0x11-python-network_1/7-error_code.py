#!/usr/bin/python3
"""this Python script that takes in a URL
     and displays the body of the response
"""
import sys
import requests

if __name__ == "__main__":
    given_url = sys.argv[1]

    # req = request
    req = requests.get(given_url)
    # Check if the response status code indicates an error
    if req.status_code >= 400:
        print("Error code: {}".format(req.status_code))
    else:
        print(req.text)
