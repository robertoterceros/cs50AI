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
    for i in range(3):
        for j in range(3):
            if board[i][j] == X:
                count_x += 1
            elif board[i][j] == O:
                count_o += 1
    if count_o == 0 and count_x == 0:
        return X
    elif count_o == count_x:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    # Return all empty cases (i,j) i is the row, and j the column
    possible_actions = set()
    for i in range(3):
        for j in range(3):
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
    # Winner across horizontal axes
    for i in range(3):
        if board[i][0] == X and board[i][1] == X and board[i][2] == X:
            return X
        elif board[i][0] == O and board[i][1] == O and board[i][2] == O:
            return O
    # Winner across vertical axes
    for j in range(3):
        if board[0][j] == X and board[1][j] == X and board[2][j] == X:
            return X
        elif board[0][j] == O and board[1][j] == O and board[2][j] == O:
            return O
    # Winner across diagonals
    if  board[0][0] == board [1][1] == board[2][2]:
        return board[1][1]
    elif board[2][0] == board[1][1] == board[0][2]:
        return board[1][1]
    else:
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) == X or winner(board) == O:
        return True
    else:
        count_empty = 0
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    count_empty += 1
        if count_empty == 0:
            return True
        else:
            return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    # X player is the max player (+1)
    # O player is the min player (-1)
    #if player(board) == O:
        # minimize

    if terminal(board):
        return None

    if player(board) == X:
        best = -9999
        for i in actions(board):
            value = min_value(result(board, i))
            print(value)
            if value > best:
                best = value
                best_move = i
        return best_move
    else:
        best = 99999
        for i in actions(board):
            value = max_value(result(board, i))
            #acprint(value)
            if value < best:
                best = value
                best_move = i
        return best_move

        
def max_value(board):
    if terminal(board):
        return utility(board)
    v = -999999999
    for action in actions(board):
        v = max(v, min_value(result(board,action)))
    return v

def min_value(board):
    if terminal(board):
        return utility(board)
    v = 999999999
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v






