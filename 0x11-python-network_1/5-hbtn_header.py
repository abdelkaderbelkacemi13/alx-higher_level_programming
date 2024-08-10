#!/usr/bin/python3
"""this Python script that takes in a URL
     and displays the value of the variable X-Request-Id
"""
import sys
import requests

if __name__ == "__main__":
    given_url = sys.argv[1]

    # req = request
    req = requests.get(given_url)
    print(req.headers.get("X-Request-Id"))
