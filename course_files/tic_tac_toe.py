import random


def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    print("+-------" * 3, "+", sep="")
    for row in range(3):
        print("|       " * 3, "|", sep="")
        for col in range(3):
            print("|   " + str(board[row][col]) + "   ", end="")
        print("|")
        print("|       " * 3, "|", sep="")
        print("+-------" * 3, "+", sep="")


def enter_move(board):
    # The function accepts the board's current status, asks the user about their move,
    # checks the input, and updates the board according to the user's decision.
    try:
        num = int(input("Enter your move: "))
        if num not in range(1, 10):
            print("Your number must be in 1..9. Try more!")
            enter_move(board)
        row = (num - 1) // 3
        col = (num - 1) % 3
        el = (row, col)
        print(el)
        lst_free = make_list_of_free_fields(board)
        if len(lst_free) > 0:
            if el in lst_free:
                board[row][col] = 'O'
            else:
                print("The square is not free. Try more!")
                enter_move(board)
    except TypeError:
        print("input value must be integer. Try more!")
        enter_move(board)
    except:
        print("Some other error. Try more!")
        enter_move(board)


def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares;
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] not in ('X', 'O')]


def victory_for(board, sgn):
    # The function analyzes the board's status in order to check if
    # the player using 'O's or 'X's has won the game
    if sgn == "X":  # are we looking for X?
        who = 'me'  # yes - it's computer's side
    elif sgn == "O":  # ... or for O?
        who = 'you'  # yes - it's our side
    else:
        who = None  # we should not fall here!
    cross1 = cross2 = True  # for diagonals
    for rc in range(3):
        if board[rc][0] == sgn and board[rc][1] == sgn and board[rc][2] == sgn:  # check row rc
            return who
        if board[0][rc] == sgn and board[1][rc] == sgn and board[2][rc] == sgn:  # check column rc
            return who
        if board[rc][rc] != sgn:  # check 1st diagonal
            cross1 = False
        if board[2 - rc][2 - rc] != sgn:  # check 2nd diagonal
            cross2 = False
    if cross1 or cross2:
        return who
    return None


def draw_move(board):
    # The function draws the computer's move and updates the board.
    free = make_list_of_free_fields(board)  # make a list of free fields
    cnt = len(free)
    if cnt > 0:  # if the list is not empty, choose a place for 'X' and set it
        this = random.randrange(cnt)
        row, col = free[this]
        board[row][col] = 'X'


board = [[3 * j + i + 1 for i in range(3)] for j in range(3)]  # make an empty board
board[1][1] = 'X'  # set first 'X' in the middle
free = make_list_of_free_fields(board)
human_turn = True  # which turn is it now?
while len(free):
    display_board(board)
    if human_turn:
        enter_move(board)
        victor = victory_for(board, 'O')
    else:
        draw_move(board)
        victor = victory_for(board, 'X')
    if victor != None:
        break
    human_turn = not human_turn
    free = make_list_of_free_fields(board)

display_board(board)
if victor == 'you':
    print("You won!")
elif victor == 'me':
    print("I won")
else:
    print("Tie!")
