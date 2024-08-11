#!/usr/bin/python3
"""
This Python script that takes your GitHub credentials
and uses the GitHub API to display your id
"""
import sys
import requests
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    # Create an HTTPBasicAuth object
    autho = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    # Send a GET request to the GitHub API
    req = requests.get("https://api.github.com/user", auth=autho)
    print(req.json().get("id"))
