"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    # If empty then x
    # if quant(x) = quant(y) then x
    # else y
    count_o = 0
    count_x = 0
    for i in board:
        for j in board:
            if board[i][j] == 'X':
                count_x += 1
            elif board[i][j] == 'O':
                count_o += 1
        if count_o == 0 and count_x == 0:
            return 'X'
        elif count_o == count_x:
            return 'X'
        else:
            return 'O'


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    # Return all empty cases (i,j) i is the row, and j the column
    possible_actions = set()
    for i in board:
        for j in board:
            if board[i][j] == None:
                possible_actions.add((i,j))
    return possible_actions



def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # Make a deep copy for new_board
    import copy
    new_board = copy.deepcopy(board)
    i,j = action
    # new_board[action] = o,x
    new_board[i][j] = player(board)
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
