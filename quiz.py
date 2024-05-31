def reverse_list(l: list):
    """
    TODO: Reverse a list without using any build in functions

    The function should return a sorted list.
    Input l is a list which can contain any type of data.
    """
    if isinstance(l, list):
        l_new = []
        for i in l[::-1]:
            l_new.append(i)
        return l_new
    else:
        return
    pass


import numpy as np


def solve_sudoku(matrix):
    """
    TODO: Write a programme to solve 9x9 Sudoku board.

    Sudoku is one of the most popular puzzle games of all time. The goal of Sudoku is to fill a 9×9 grid with numbers so that each row, column and 3×3 section contain all of the digits between 1 and 9. As a logic puzzle, Sudoku is also an excellent brain game.

    The input matrix is a 9x9 matrix. You need to write a program to solve it.
    """
    matrix = np.array(matrix)
    pos = [-1, -1]
    possible = []
    solves = []
    if matrix.max() > 9 or matrix.min() < 0 or matrix.shape != (9, 9):
        raise ValueError('matrix error')
    for y in range(9):
        if pos[0] != -1 and pos[1] != -1:
            break
        for x in range(9):
            if matrix[y][x] == 0:
                pos = [x, y]
                break
    if pos[0] == -1 and pos[1] == -1:
        return [matrix]
    for k in range(1, 9 + 1):
        x = pos[0]
        y = pos[1]

        row = matrix[y, :]
        if k in row:
            continue

        col = matrix[:, x]
        if k in col:
            continue
        box = matrix[y - y % 3:y - y % 3 + 3, x - x % 3:x - x % 3 + 3]
        if k in box:
            continue
        possible.append(k)
    if len(possible) == 0:
        return
    for i in range(len(possible)):
        y = pos[1]
        x = pos[0]
        matrix[y][x] = possible[i]
        ret = solve_sudoku(matrix)
        if ret is None:
            pass
        elif isinstance(ret, list) and len(ret) == 0:
            pass
        else:
            return ret
    return solves
