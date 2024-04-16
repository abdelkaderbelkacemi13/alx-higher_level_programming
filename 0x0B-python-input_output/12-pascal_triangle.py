#!/usr/bin/python3
"""pascal_triangle(n) function"""


def pascal_triangle(n):
    """function that returns a list of lists of integers
    representing the Pascal's triangle of n"""
    if n <= 0:
        return []

    pastri = [[1]]
    while len(pastri) != n:
        pastr = pastri[-1]
        pstmp = [1]
        for i in range(len(pastri) - 1):
            pstmp.append(pastr[i] + pastr[i + 1])
        pstmp.append(1)
        pastri.append(pstmp)
    return (pastri)
