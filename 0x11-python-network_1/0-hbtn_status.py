#!/usr/bin/python3
"""a Python script that fetches https://alx-intranet.hbtn.io/status"""
import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as resopnse:
        body_respo = resopnse.read()
    print("Body response:")
    print("\t- type: {}".format(type(body_respo)))
    print("\t- content: {}".format(body_respo))
    print("\t- utf8 content: {}".format(body_respo.decode("utf-8")))