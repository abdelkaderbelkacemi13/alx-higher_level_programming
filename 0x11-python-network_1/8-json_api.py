#!/usr/bin/python3
""" """
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
