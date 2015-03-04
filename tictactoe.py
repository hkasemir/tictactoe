import random

BOARD_SIZE = 3


def create_board(size):
    return [[' ']*size for i in range(size)]


def board_string(board):
    board_str = ''
    for k in range(len(board)+1):
        board_str += ' ' + str(k) + ' '
    board_str += '\n'
    for i in range(len(board)):
        row_string = ' ' + chr(65 + i) + ' '
        for j in range(len(board)):
            row_string += '[' + str(board[i][j]) + ']'
        board_str += row_string + '\n'
    return board_str


def get_column(player, board):
    column_str = input(player + ' choose a column (1, 2, etc): ')
    while True:
        if column_str.isnumeric() and\
           int(column_str) - 1 in range(len(board)):
            column = int(column_str) - 1
            return column
        else:
            column_str = input('Sorry, please input a number between 1 and ' +
                               str(len(board)) + ': ')


def get_row(player, board):
    row_str = input(player + ' choose a row (A, B, etc): ').upper()
    while True:
        if ord(row_str) - 65 in range(len(board)):
            row_int = ord(row_str) - 65
            return row_int
        else:
            row_str = input('Sorry, please input a letter between A and ' +
                            str(chr(65 + len(board)-1)))


def player_turn(player, key, board):
    while True:
        column = get_column(player, board)
        row = get_row(player, board)
        if board[row][column] == " ":
            board[row][column] = key
            return board
        else:
            print('Sorry, that spot\'s been taken, try again: ')
        

def computer_turn(key, board):
    while True:
        row = random.randint(0, (BOARD_SIZE-1))
        column = random.randint(0, (BOARD_SIZE-1))
        if board[row][column] == ' ':
            board[row][column] = key
            return board


def check_win(board):
    # To be called after player and computer turns. Returns True if 3 in a row 
    # is made from turn just played. Returns False if no win is detected, and 
    # returns None if there is a tie.
    # check for 3 in a row
    for i in range(len(board)):
        key = board[i][0]
        if key != " " and\
           board[i][1] == key and\
           board[i][2] == key:
            return True
    # check for 3 in a column
    for j in range(len(board)):
        key = board[0][j]
        if key != " " and\
           board[1][j] == key and\
           board[2][j] == key:
            return True
    # check for diagonals
    key = board[0][0]
    if key != " " and\
       board[1][1] == key and\
       board[2][2] == key:
        return True
    key = board[2][0]
    if key != " " and\
       board[1][1] == key and\
       board[0][2] == key:
        return True
    # Check for full board if no wins, indicates a tie
    full_row = 0
    for row in board:
        if ' ' not in row:
            full_row += 1
        if full_row == len(board):
            return None
    return False

player_key = 'x' 
computer_key = 'o'

print('Welcome to Heidi\'s Tic-Tac-Toe game!')
game_board = create_board(BOARD_SIZE)
print(board_string(game_board))

while True:
    game_board = player_turn('Player 1', player_key, game_board)
    print(board_string(game_board))
    if check_win(game_board):
        print('Player wins!')
        break
    if check_win(game_board) is None:
        print('Catscratch! Nobody wins.')
        break
    game_board = computer_turn(computer_key, game_board)
    print(board_string(game_board))
    if check_win(game_board):
        print('Computer wins!')
        break
    if check_win(game_board) is None:
        print('Catscratch! Nobody wins.')
        break
