#!/usr/bin/python3
"""a Python script that fetches https://alx-intranet.hbtn.io/status"""
import urllib.request

if __name__ == "__main__":
    URL = urllib.request.Request("https://alx-intranet.hbtn.io/status")
    with urllib.request.urlopen(URL) as resopnse:
        body_respo = resopnse.read()
    print("Body response:")
    print("\t- type: {}".format(type(body_respo)))
    print("\t- content: {}".format(body_respo))
    print("\t- utf8 content: {}".format(body_respo.decode("utf-8")))
