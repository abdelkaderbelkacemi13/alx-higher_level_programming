#!/usr/bin/python3
"""
this python script takes in a letter
and sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter.
"""
import sys
import requests

if __name__ == "__main__":
    letter = "" if len(sys.argv) == 1 else sys.argv[1]
    payload = {"q": letter}

    # req =request
    req = requests.post("http://0.0.0.0:5000/search_user", data=payload)
    try:
        respon = req.json()
        if respon == {}:
            print("No result")
        else:
            print("[{}] {}".format(respon.get("id"), respon.get("name")))
    except ValueError:
        print("Not a valid JSON")
