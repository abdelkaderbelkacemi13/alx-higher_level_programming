#!/usr/bin/python3
"""This python script that fetches https://alx-intranet.hbtn.io/status"""
# import the nececery modules
import requests


if __name__ == "__main__":
    # Send an HTTP GET request to URL
    http_response = requests.get("https://intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(http_response.text)))
    print("\t- content: {}".format(http_response.text))
