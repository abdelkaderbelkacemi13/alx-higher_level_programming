#!/usr/bin/python3
"""this Python script that takes in a URL and an email
    and displays the body of the response.
"""
import sys
import requests

if __name__ == "__main__":
    given_url = sys.argv[1]
    email_value = {'email': sys.argv[2]}

    # req = request
    req = requests.get(given_url, data=email_value)
    # Print the text content of the server's response
    print(req.text)
