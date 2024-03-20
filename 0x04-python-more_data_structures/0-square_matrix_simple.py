#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    return [list(map(lambda elmt: elmt * elmt, inte)) for inte in matrix]
