#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for it_key in sorted(a_dictionary.keys()):
        print('{}: {}'. format(it_key, a_dictionary[it_key]))
