# Author: Heidi Kasemir
BOARD_SIZE = 3

alpha_numeric = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F'}
key_list = list(alpha_numeric.keys())
value_list = list(alpha_numeric.values())


def create_board(size):
    board = []
    for i in range(size):
        row = [" "] * size
        board.append(row)
    return board


def print_board(board):
    first_row = ""
    for k in range(len(board)+1):
        first_row += ' ' + str(k) + ' '
    print(first_row)
    for i in range(len(board)):
        row_string = ' ' + alpha_numeric[i] + ' '
        for j in range(len(board)):
            row_string += '[' + board[i][j] + ']'
        print(row_string)


def get_player_key(player):
    key = input("What is " + player + "'s symbol (X/O)? ")
    if len(key) > 1:
        key = key[0]
        print("We're just going to keep the first character of that: " + key)
    return key


def get_column(player, board):
    column_str = input(player + " choose a column (1, 2, etc): ")
    try:
        column = int(column_str) - 1
    except:
        print("Sorry, please input a number between 1 and " + str(len(board)))
        column = get_column(player, board)
    return column


def get_row(player, board):
    try:
        row_str = input(player + " choose a row (A, B, etc): ").upper()
        row_number = key_list[value_list.index(row_str)]
    except:
        print("Sorry, please input a letter between A and " +
              str(value_list[len(board)-1]))
        row_number = get_row(player, board)
    return row_number


def player_turn(player, player_key, board):
    column = get_column(player, board)
    while column not in range(len(board)):
        print("Value not in range, please input a number between 1 and " +
              str(len(board)))
        column = get_column(player, board)
    row = get_row(player, board)
    while row not in range(len(board)):
        print("Not in range, please input a letter between A and " +
              str(value_list[len(board)-1]))
        row = get_row(player, board)
    while board[row][column] != " ":
        print("Sorry, that spot's been taken, try again: ")
        column = get_column(player, board)
        row = get_row(player, board)
    else:
        board[row][column] = player_key
        print_board(board)


def check_win(board):
    # check for 3 in a row
    win = False
    for i in range(len(board)):
        key = board[i][0]
        if key != " " and\
           board[i][1] == key and\
           board[i][2] == key:
            print(str(key) + " got three in a row!")
            win = True
            break
        else:
            next
    if win is False:
        # check for 3 in a column if no 3 in a row
        for j in range(len(board)):
            key = board[0][j]
            if key != " " and\
               board[1][j] == key and\
               board[2][j] == key:
                print(str(key) + " got three in a column!")
                win = True
                break
            else:
                next
    if win is False:
        # check for diagonals
        key = board[0][0]
        if key != " " and\
           board[1][1] == key and\
           board[2][2] == key:
            print(str(key) + " got three in a diagonal!")
            win = True
        key = board[2][0]
        if key != " " and\
           board[1][1] == key and\
           board[0][2] == key:
            print(str(key) + " got three in a diagonal!")
            win = True
    return win

player1_key = get_player_key("Player 1")
player2_key = get_player_key("Player 2")

while player1_key == player2_key:
    print("Sorry, Player 1 and Player 2 can't be the same, try again:")
    player2_key = get_player_key("Player 2")

print("Welcome to Heidi's Tic-Tac-Toe game!")
win = False
game_board = create_board(BOARD_SIZE)
print_board(game_board)
win = check_win(game_board)

while win is False:
    full_row = 0
    player_turn("Player 1", player1_key, game_board)
    win = check_win(game_board)
    if win is True:
        print("Player 1 wins!")
        break
    for row in game_board:
        if " " not in row:
            full_row += 1
    if full_row == BOARD_SIZE:
        print("Catscratch! Nobody wins.")
        break
    player_turn("Player 2", player2_key, game_board)
    win = check_win(game_board)
    if win is True:
        print("Player 2 wins!")
