#!/usr/bin/python3
def no_c(my_string):
    new_str = ''
    for cc in my_string:
        if cc == 'c' or cc == 'C':
            continue
        else:
            new_str += cc
    return (new_str)
