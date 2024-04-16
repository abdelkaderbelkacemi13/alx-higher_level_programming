#!/usr/bin/python3
""" write_file function"""


def write_file(filename="", text=""):
    """write a content of a text file"""
    with open(filename, "w", encoding="utf-8") as f:
        return (f.write(text))
