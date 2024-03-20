#!/usr/bin/python3
def uniq_add(my_list=[]):
    num = 0
    for elmt in set(my_list):
        num += elmt
    return num
