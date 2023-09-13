#!/usr/bin/python3
"""This module defines a function `rotate_2d_matrix`"""


def rotate_2d_matrix(matrix):
    """
    Rotate a 2D matrix by 90 degrees clockwise.
    """
    length = len(matrix)
    new_list = []
    new_list = [[0 for _ in range(length)] for _ in range(length)]

    for i in range(0, length):
        new_list[i] = matrix[i].copy()

    for i in range(length):
        num = length - 1
        for j in range(length):
            matrix[i][j] = new_list[num][i]
            num -= 1
