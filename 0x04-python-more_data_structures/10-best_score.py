#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    keymx = None
    valmx = 0
    for key, val in a_dictionary.items():
        if val > valmx:
            valmx = val
            keymx = key
    return keymx
