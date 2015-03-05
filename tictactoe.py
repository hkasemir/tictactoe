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


def get_column(player, board):
    row_length = int(math.sqrt(len(board)))

    while True:
        column_str = input(player + ' choose a column (1, 2, etc): ')

        if column_str.isnumeric() and\
           int(column_str) - 1 in range(row_length):
            return int(column_str) - 1

        print('Sorry, please input a number between 1 and ' +
              str(row_length) + ': ')


def get_row(player, board):
    row_length = int(math.sqrt(len(board)))

    while True:
        row_str = input(player + ' choose a row (A, B, etc): ').upper()

        if ord(row_str) - 65 in range(row_length):
            return ord(row_str) - 65

        print('Sorry, please input a letter between A and ' +
              str(chr(64 + row_length)) + ': ')


def index_from_row_and_col(row, col, size):
        return row*size + col


def game_turn(player, board):
    if player == 'Player':
        size = int(math.sqrt(len(board)))

        while True:
            column = get_column(player, board)
            row = get_row(player, board)
            index = index_from_row_and_col(row, column, size)

            if board[index] == 0:
                board[index] = 1
                return board

            print('Sorry, that spot\'s been taken, try again: ')

    elif player == 'Computer':
        while True:
            index = random.randint(0, len(board)-1)

            if board[index] == 0:
                board[index] = -1
                return board


def check_win(board):
    # To be called after player and computer turns. Returns True if 3 in a row
    # is made from turn just played. Returns False if no win is detected, and
    # returns None if there is a tie.
    winning_paths = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]
    for path in winning_paths:
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
        game_board = game_turn(player, game_board)
        print(board_to_string(game_board))
        if check_win(game_board):
            print(player + ' wins!')
            game_complete = True
            break
        if check_win(game_board) is None:
            print('Catscratch! Nobody wins.')
            game_complete = True
            break
