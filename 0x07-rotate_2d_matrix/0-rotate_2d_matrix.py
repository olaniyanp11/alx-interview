#!/usr/bin/python3
def rotate_2d_matrix(matrix):
    """
    Rotate a 2D matrix by 90 degrees clockwise.
    """
    new_list =[1,2,3]
    new_list[0] = matrix[0].copy()
    new_list[1] = matrix[1].copy()
    new_list[2] = matrix[2].copy()
    
    for i in range(3):
        num = 2
        for j in range(3):
            matrix[i][j] = new_list[num][i]
            num -=1