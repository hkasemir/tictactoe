import random

BOARD_SIZE = 3
EMPTY_KEY = ' '
PLAYER_KEY = 'x'
COMPUTER_KEY = 'o'

row_alpha = []
for i in range(BOARD_SIZE):
    row_alpha += chr(65 + i)


def create_board(size):
    return [[0]*size for i in range(size)]


def board_to_string(board):
    # converts the numeric values of the game board to 'x', 'o', and blank
    # space. Adds column numbers and row letters for easy input of cell
    board_str = ''

    # writes out the column numbers
    for k in range(len(board) + 1):
        board_str += ' ' + str(k) + ' '
    board_str += '\n'

    # puts the A, B, C etc values at the front of the rows
    for i in range(len(board)):
        row_string = ' ' + row_alpha[i] + ' '

        for j in range(len(board)):
            key = EMPTY_KEY

            if board[i][j] == 1:
                key = PLAYER_KEY
            elif board[i][j] == -1:
                key = COMPUTER_KEY

            row_string += '[' + key + ']'

        board_str += row_string + '\n'

    return board_str

def get_column(board):
    while True:
        column_str = input('Choose a column (1, 2, etc): ')
        if column_str.isnumeric() and\
           int(column_str) - 1 in range(len(board)):
            return int(column_str) - 1
        print('Sorry, please input a number between 1 and ' +
              str(len(board)) + ': ')


def get_row(board):
    while True:
        row_str = input('Choose a row (A, B, etc): ').upper()
        if row_str in row_alpha:
            return ord(row_str) - 65
        print('Sorry, please input a letter between A and ' +
              str(row_alpha[len(board)-1]) + ': ')


def valid_move(row, col, board):
    return board[row][col] == 0


def make_move(row, col, board, player):
    if player == 'Player':
        board[row][col] = 1
    elif player == 'Computer':
        board[row][col] = -1


def get_choice(player, board):
    if player == 'Player':
        column = get_column(board)
        row = get_row(board)

    elif player == 'Computer':
        column = random.randint(0, len(board) - 1)
        row = random.randint(0, len(board) - 1)

    return row, column


def game_turn(player, board):
    while True:
        row, column = get_choice(player, board)
        
        if valid_move(row, column, board):
            make_move(row, column, board, player)
            return board
        
        if player == 'Player':
            print('Sorry, that spot\'s been taken, try again: ')


IN_A_ROW_TO_WIN = 3

def check_win(board):
    # To be called after player and computer turns. Returns True if 3 in a row 
    # is made from turn just played. Returns False if no win is detected, and 
    # returns None if there is a tie.
    # check for 3 in a row
    for row in board: # row
        if abs(sum(row)) == IN_A_ROW_TO_WIN:
            return True
    # check for 3 in a column
    for col in range(len(board)):
        column_check_sum = 0
        for row in range(len(board)):
            column_check_sum += board[row][col]
        if abs(column_check_sum) == IN_A_ROW_TO_WIN:
            return True
    # check for diagonals down and right:
    diagonal_check_sum = 0
    for i in range(len(board)):
        diagonal_check_sum += board[i][i]
        if abs(diagonal_check_sum) == IN_A_ROW_TO_WIN:
            return True
    # check for diagonals down and left:
    diagonal_check_sum = 0
    for i in range(len(board)):
        diagonal_check_sum += board[len(board)-1 - i][i]
        if abs(diagonal_check_sum) == IN_A_ROW_TO_WIN:
            return True

    # Check for full board if no wins, indicates a tie
    full_row = 0
    for row in board:
        if 0 not in row:
            full_row += 1
        if full_row == len(board):
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
