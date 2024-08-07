#!/usr/bin/python3
"""This script sends a POST request to a given URL with an email parameter
    and displays the body of the response
"""
# import the nececery modules
import sys
import urllib.parse
import urllib.request

if __name__ == "__main__":
    # the first argument is the URL
    url = sys.argv[1]
    email_val = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(email_val).encode("ascii")

    request = urllib.request.Request(url, data)
    with urllib.request.urlopen(request) as response:
        print(response.read().decode("utf-8"))
