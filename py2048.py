import random,sys
from copy import deepcopy
from numpy import *
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--n", help="board_size",default=4)
parser.add_argument("--w", help="winning_number",default=2044)
args = parser.parse_args()
boardsize=int(args.n)
winning_number=int(args.w)



def addrow(row):
    for j in range(boardsize - 1):
        for i in range(boardsize - 1, 0, -1):
            if row[i - 1] == 0:
                row[i - 1] = row[i]
                row[i] = 0
    for i in range(boardsize - 1):
        if row[i] == row[i + 1]:
            row[i] = row[i] * 2
            row[i + 1] = 0
    for i in range(boardsize - 1, 0, -1):
        if row[i - 1] == 0:
            row[i - 1] = row[i]
            row[i] = 0
    return row


def addleft(currentboard):
    for i in range(boardsize):
        currentboard[i] = addrow(currentboard[i])
    return currentboard


def addrow1(row):
    for j in range(boardsize-1):

        for i in range(boardsize-1,0,-1):
            if row[i]==0:
                row[i]=row[i-1]
                row[i-1]=0
    for i in range(boardsize-1,0,-1):
        if row[i] == row[i-1]:
            row[i]=row[i]*2
            row[i-1]=0
    for i in range(boardsize - 1, 0, -1):
        if row[i ] == 0:
            row[i] = row[i-1]
            row[i-1] = 0
    return row

def addright(currentboard):
    for i in range(boardsize):
        currentboard[i]=addrow1(currentboard[i])
    return currentboard


def transpose(currentboard):
    for j in range(boardsize):
        for i in range(j, boardsize):
            if not i == j:
                temp = currentboard[j][i]
                currentboard[j][i] = currentboard[i][j]
                currentboard[i][j] = temp
    return currentboard


def addup(currentboard):
    currentboard = transpose(currentboard)
    currentboard = addleft(currentboard)
    currentboard = transpose(currentboard)

    return currentboard


def adddown(currentboard):
    currentboard = transpose(currentboard)
    currentboard = addright(currentboard)
    currentboard = transpose(currentboard)

    return currentboard


def insertno():
    if random.randint(1) == 1:
        return 2
    else:
        return 2



def addvalue():
    i = random.randint(0, boardsize - 1)
    j = random.randint(0, boardsize - 1)

    while not board[i][j] == 0:
        i = random.randint(0, boardsize - 1)
        j = random.randint(0, boardsize - 1)

    board[i][j] = insertno()


def won():
    for row in board:
        if winning_number in row:
            return True
    return False


def end():
    Board1 = deepcopy(board)
    Board2 = deepcopy(board)
    # test every possible move

    Board1 = adddown(Board1)
    if Board1 == Board2:
        Board1 = addup(Board1)
        if Board1 == Board2:
            Board1 = addleft(Board1)
            if Board1 == Board2:
                Board1 = addright(Board1)
                if Board1 == Board2:
                    return True
    return False

def display_board():

    largest = board[0][0]
    for row in board:
        for element in row:
            if element > largest:
                largest = element

    n = len(str(largest))

    for row in board:
        currentrow = "|"
        for item in row:
            currentrow += (" " * (n - len(str(item)))) + str(item) + "|"
        print(currentrow)
    print()


board = []
for i in range(boardsize):
    row = []
    for j in range(boardsize):
        row.append(0)
    board.append(row)


numrequired = 1
while numrequired > 0:
    i = random.randint(0, boardsize - 1)
    j = random.randint(0, boardsize - 1)

    if board[i][j] == 0:
        board[i][j] = insertno()
        numrequired -= 1

display_board()

gameOver = False

while not gameOver:

    move = input("play your move : ")
    move = move.strip().lower()
    validInput = True
    tempBoard = deepcopy(board)
    if move == 'q':

            print('Thanks for playing!')
            sys.exit()
    else:
            if move == "d":
                board = addright(board)
            elif move == "w":
                board = addup(board)
            elif move == "a":
                board = addleft(board)
            elif move == "s":
                board = adddown(board)
            else:
                validInput = False

            if not validInput:
                print("your input is notvalid,please try again")
            else:
                if board == tempBoard:
                    print("try different direction!")
                else:
                    if won():
                        display_board()
                        print("you Won!")
                        print("your score is :",winning_number)
                        gameOver = True
                    else:
                        addvalue()
                        display_board()


                        if end():
                            print("you lose game ")
                            gameOver = True

