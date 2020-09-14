def clock_wise_90rotation(board):
    '''
    board : n by n list.
    '''
    x_max = len(board[0])
    y_max = len(board)

    temp = []
    for x in range(x_max):
        row = []
        for y in range(y_max):
            row.append(board[y][x])
        temp.append(row[::-1])
    return temp

def solution(board, moves):
    board = clock_wise_90rotation(board)
    for row in board:
        while row:
            if row[-1] == 0:
                row.pop()
                continue
            break

    basket = []
    count = 0
    for move in moves:
        index = move - 1
        if board[index]:
            if basket:
                if basket[-1] == board[index][-1]:
                    basket.pop()
                    board[index].pop()
                    count += 2
                else:
                    basket.append(board[index].pop())
            else:
                basket.append(board[index].pop())

    return count

def solution_direct(board, moves):

    count = 0
    stack = [-1]
    for move in moves:
        index = move - 1
        for i in range(len(board)):
            value = board[i][index]
            if board[i][index] == 0:
                continue
            if stack[-1] == board[i][index]:
                stack.pop()
                count += 2
            else:
                stack.append(board[i][index])
            board[i][index] = 0
            break
    return count

import random
def make_board(column, row):

    board = [[random.randint(1, 100) for i in range(row)] for j in range(column)]

    for r in range(row):
        zero_length = random.randint(0, column)
        for i in range(zero_length):
            board[i][r] = 0
    return board

def make_moves(num, row):
    moves = [random.randint(1, row) for i in range(num)]
    return moves

import time
if __name__ == '__main__':
    _board = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]]
    _moves = [1, 5, 3, 5, 1, 2, 1, 4]
    _result = 4

    temp = solution_direct(_board, _moves)
    print(f"result : {temp}")
    print(temp == _result)

    t_board = make_board(30, 30)
    t_moves = make_moves(1000, 30)

    start = time.time()
    solution_direct(t_board, t_moves)
    end = time.time()
    print(end - start)

    start = time.time()
    solution(t_board, t_moves)
    end = time.time()
    print(end - start)




