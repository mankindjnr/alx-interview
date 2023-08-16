#!/usr/bin/python3
"""
rotating a 2d matrix
90 degrees clockwise
"""


def deep_copy(lst):
    """creating a deep copy of a list"""
    if isinstance(lst, list):
        new_list = []
        for item in lst:
            new_list.append(deep_copy(item))
        return new_list
    else:
        return lst


def rotate_2d_matrix(matrix):
    """rotating the matrix 90 degrees"""
    row_length = len(matrix[0])
    rotated_matrix = deep_copy(matrix)
    for i in range(row_length - 1, -1, -1):
        last = []
        for item in rotated_matrix:
            last.append(item[i])

        last.reverse()
        matrix[i] = last
