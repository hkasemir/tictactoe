import math
import random

BOARD_SIZE = 3
PLAYER_KEY = 'x'
COMPUTER_KEY = 'o'
EMPTY_KEY = ' '


def create_board(size):
    # Creates 1-dimensional game board for storing played values. 0 is empty,
    # -1 is the computer played value, 1 is the player value.
    return [0]*size**2


def board_to_string(board):
    # converts the numeric values of the game board to 'x', 'o', and blank
    # space. Adds column numbers and row letters for easy input of cell
    row_length = int(math.sqrt(len(board)))
    board_str = ''
    for k in range(row_length+1):
        board_str += ' ' + str(k) + ' '
    board_str += '\n'

    for i in range(row_length):
        row_string = ' ' + chr(65 + i) + ' '
        for j in range(row_length):
            key = EMPTY_KEY
            if board[i*row_length + j] == 1:
                key = PLAYER_KEY
            elif board[i*row_length + j] == -1:
                key = COMPUTER_KEY
            row_string += '[' + key + ']'
        board_str += row_string + '\n'
    return board_str


def get_column(board):
    row_length = int(math.sqrt(len(board)))

    while True:
        column_str = input('Choose a column (1, 2, etc): ')

        if column_str.isnumeric() and\
           int(column_str) - 1 in range(row_length):
            return int(column_str) - 1

        print('Sorry, please input a number between 1 and ' +
              str(row_length) + ': ')


def get_row(board):
    row_length = int(math.sqrt(len(board)))

    while True:
        row_str = input('Choose a row (A, B, etc): ').upper()

        if ord(row_str) - 65 in range(row_length):
            return ord(row_str) - 65

        print('Sorry, please input a letter between A and ' +
              str(chr(64 + row_length)) + ': ')


def valid_move(row, col, board):
    size = int(math.sqrt(len(board)))
    index = row*size + col
    return board[index] == 0


def make_move(row, col, board, player):
    size = int(math.sqrt(len(board)))
    index = row*size + col
    if player == 'Player':
        board[index] = 1
    elif player == 'Computer':
        board[index] = -1


def get_choice(player, board):
    size = int(math.sqrt(len(board)))

    if player == 'Player':
        column = get_column(board)
        row = get_row(board)

    elif player == 'Computer':
        column = random.randint(0, size-1)
        row = random.randint(0, size-1)
    return column, row


def game_turn(player, board):
    while True:
        column, row = get_choice(player, board)

        if valid_move(row, column, board):
            make_move(row, column, board, player)
            return board

        if player == 'Player':
            print('Sorry, that spot\'s been taken, try again: ')

WINNING_PATHS = [
    # rows
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],

    # columns
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],

    # diagonals
    [0, 4, 8],
    [2, 4, 6]
]


def check_win(board):
    # To be called after player and computer turns. Returns True if 3 in a row
    # is made from turn just played. Returns False if no win is detected, and
    # returns None if there is a tie.
    for path in WINNING_PATHS:
        check_sum = 0
        for i in range(len(path)):
            check_sum += board[path[i]]
        if abs(check_sum) == 3:
            return True
    # Check for full board if no wins, indicates a tie
    if 0 not in board:
        return None
    return False


print('Welcome to Heidi\'s Tic-Tac-Toe game!')
game_board = create_board(BOARD_SIZE)
print(board_to_string(game_board))

players = ['Player', 'Computer']
game_complete = False
while game_complete is False:
    for player in players:
        print('Turn: ' + player)
        game_board = game_turn(player, game_board)
        print(board_to_string(game_board))
        turn_result = check_win(game_board)
        if turn_result:
            print(player + ' wins!')
            game_complete = True
            break
        if turn_result is None:
            print('Catscratch! Nobody wins.')
            game_complete = True
            break
