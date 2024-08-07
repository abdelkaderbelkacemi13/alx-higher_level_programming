#!/usr/bin/python3
""" This script takes in a URL sends a request to the URL
    and displays the body of the response
"""
# import the nececery modules
import sys
import urllib.error
import urllib.request


if __name__ == "__main__":
    # takes the URL as first argument.
    URL = sys.argv[1]

    # Create the request
    request = urllib.request.Request(URL)
    # Open the URL and get the response
    try:
        with urllib.request.urlopen(request) as response:
            print(response.read().decode("ascii"))
    # Print the error code if any error accurs
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
