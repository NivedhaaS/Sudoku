import random
board = [[2, 1, 7, 1, 2, 6, 3, 6, 2], [1, 8, 8, 2, 5, 6, 9, 2, 6], [7, 5, 1, 1, 9, 9, 2, 2, 4], [8, 4, 6, 6, 4, 5, 1, 7, 5], [1, 9, 8, 2, 5, 4, 4, 7, 9], [3, 2, 2, 7, 7, 7, 1, 9, 6], [8, 2, 8, 3, 8, 4, 9, 2, 3], [8, 1, 3, 9, 3, 1, 8, 9, 6], [3, 3, 2, 6, 3, 8, 3, 2, 4]]



def valid_in_row(row, num):
    for i in board[row]:
        if num == i:
            return False
        else:
            return True
print(valid_in_row(0, 7))
