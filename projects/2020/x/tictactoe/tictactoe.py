"""
Tic Tac Toe Player
"""
import copy
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
    if board == initial_state():
        return X

    total_x = 0
    total_o = 0

    for i in board:
        total_x += i.count(X)
        total_o += i.count(O)

    if (total_x + total_o) % 2 == 1:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    moves = []

    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == X or board[i][j] == O:
                pass
            else:
                moves.append((i, j))

    moves = set(moves)
    return moves


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """


    new_board = copy.deepcopy(board)
    turn = player(board)

    if board[action[0]][action[1]] == X or board[action[0]][action[1]] == O:
        raise ValueError('Invalid Action')
    else:
        new_board[action[0]][action[1]] = turn

    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    x_in_board = []
    o_in_board = []
    winning_positions = [
        [[0, 0], [0, 1], [0, 2]],
        [[1, 0], [1, 1], [1, 2]],
        [[2, 0], [2, 1], [2, 2]],
        [[0, 0], [1, 0], [2, 0]],
        [[0, 1], [1, 1], [2, 1]],
        [[0, 2], [1, 2], [2, 2]],
        [[0, 0], [1, 1], [2, 2]],
        [[0, 2], [1, 1], [2, 0]]
    ]

    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == X:
                x_in_board.append([i, j])
            elif board[i][j] == O:
                o_in_board.append([i, j])

    for i in winning_positions:
        if i[0] in x_in_board and i[1] in x_in_board and i[2] in x_in_board:
            return X
        elif i[0] in o_in_board and i[1] in o_in_board and i[2] in o_in_board:
            return O

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) == X or winner(board) == O:
        return True

    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == EMPTY:
                return False

    return True


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

    if terminal(board):
        return None

    action_x = []
    value_x = []
    action_y = []
    value_y = []

    def max_value(board):
        v = -float('inf')
        if terminal(board):
            return utility(board)

        for action in actions(board):
            v = max(v, min_value(result(board, action)))


        return v

    def min_value(board):
        v = float('inf')
        if terminal(board):
            return utility(board)
        for action in actions(board):
            v = min(v, max_value(result(board, action)))

        return v

    for action in actions(board):
        if player(board) == X:
            action_x.append(action)
            value_x.append(min_value(result(board, action)))

        elif player(board) == O:
            action_y.append(action)
            value_y.append(max_value(result(board, action)))

    if player(board) == X:
        return action_x[value_x.index(max(value_x))]
    elif player(board) == O:
        return action_y[value_y.index(min(value_y))]

