#!/usr/bin/python3
def safe_print_division(a, b):
    divresult = 0
    try:
        divresult = a / b
    except (TypeError, ZeroDivisionError):
        divresult = None
    finally:
        print("Inside result: {}".format(divresult))
    return (divresult)
