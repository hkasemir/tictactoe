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



"""
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
"""
directions = [
    [0, 1],      # Check to the right
    [1, 0],      # Check down the column
    [1, 1],      # Check diagonal to the right
    [1, -1]      # Check diagonal to the left
]

def check_win(board):
    pos = [0, 0]
    direction = [1, 0]
    check_win_for_cell(board, pos, direction)

def check_win_for_cell(board, pos, direction):

    char = board[pos[0]][pos[1]]
    if char == 0:
        return False
    next_pos = pos
    check_sum = 1
    while True:
        next_pos = [next_pos[0] + direction[0], next_pos[1] + direction[1]]

        if next_pos[0] >= len(board):
            break

        if next_pos[1] >= len(board):
            break

        next_char = board[next_pos[0]][next_pos[1]]

        if next_char != char:
            break
        check_sum +=1

        if check_sum == 3:
            return True

    return False

board = [
    [1,0,1,0],
    [0,1,0,0],
    [1,0,1,0],
    [1,0,1,1],
]

print(check_win(board))