# Functions in tictactoe.py by Alex Aranes


# Libraries and modules used
import os
import time
from colorama import Fore,Style,init

init(autoreset=True)


# Function for clearing the console
def clear_console():
        command = 'clear'
        if os.name in ('nt', 'dos'):
            command = 'cls'
        os.system(command)


# Prints the TICTACTOE HUD
def menu():
    print(Fore.CYAN+"=================\n|               |\n|  TIC TAC TOE  |\n|               |\n=================")


# Main UI that shows the board of the game
def ui(matrix):
    clear_console()
    menu()
    print("     1   2   3 ")
    print("   ____________")
    print("  |")
    for i in range(len(matrix)):
        print(i+1, "|", end=" ")
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                print(Style.DIM+"[ ]", end=" ")
            elif matrix[i][j] == 1:
                print(Fore.RED+" X ", end=" ")
            else:
                print(Fore.BLUE+" O ", end=" ")
        print()
        if i < 2:
            print("  |")
    print("   ____________\n")


# UI after the program detects a winner
def winUI(matrix):
    clear_console()
    menu()
    print(Fore.YELLOW+"     1   2   3 ")
    print(Fore.YELLOW+"   ____________")
    print(Fore.YELLOW+"  |")
    winning_line = get_winning_line(matrix) # Get the winning line coordinates

    for i in range(len(matrix)):
        print(Fore.YELLOW+f"{i+1} |", end=" ")
        for j in range(len(matrix[i])):
            is_winning_cell = winning_line and (i, j) in winning_line
            if matrix[i][j] == 0:
                print(Fore.YELLOW+"[ ]", end=" ")
            elif matrix[i][j] == 1: # Player X
                if is_winning_cell:
                    print(Style.BRIGHT+Fore.GREEN+" X ", end=" ")
                else:
                    print(Fore.YELLOW+" X ", end=" ")
            else: # Player O (matrix[i][j] == 2)
                if is_winning_cell:
                    print(Style.BRIGHT+Fore.GREEN+" O ", end=" ")
                else:
                    print(Fore.YELLOW+" O ", end=" ")
        print()
        if i < 2:
            print(Fore.YELLOW+"  |")
    print(Fore.YELLOW+"   ____________\n")
    

# Main Function that handles User Input
def playerInput(matrix,role,turn):
    rowsCols = ["1","2","3"]
    while True:
        print("Player ",turn+1,"'s Turn")
        col = input("Input Column Number: ")
        row = input("Input Row Number: ")
        if row not in rowsCols or col not in rowsCols:
            print(Fore.RED+"Invalid Input")
            time.sleep(1)
            ui(matrix)
        else:
            if role == True and turn == 0:
                chosen = 2
            elif role == True and turn == 1:
                chosen = 1
            elif role == False and turn == 0:
                chosen = 1
            else:
                chosen = 2
            if matrix[int(row)-1][int(col)-1] == 0 or not matrix[int(row)-1][int(col)-1] == chosen:
                if role == True and turn == 0:
                    CELL = 1
                elif role == True and turn == 1:
                    CELL = 2
                elif role == False and turn == 0:
                    CELL = 2
                else:
                    CELL = 1
                ROW = int(row)-1
                COL = int(col)-1
                return CELL,ROW,COL
            else:
                print(Fore.RED+"That was already occupied!")
                time.sleep(1)
                ui(matrix)


# Function that constantly checks if there's a winner or no more blank spaces indicating.
def checkMatrix(matrix,turn):
    winner = 0
    hasBlank = False
    for i in range(0,len(matrix)):
        if matrix[i][0] == matrix[i][1] == matrix[i][2] != 0:
            if turn == 0:
                winner = 1
                return winner
            else:
                winner = 2
                return winner
        if matrix[0][i] == matrix[1][i] == matrix[2][i] != 0:
            if turn == 0:
                winner = 1
                return winner
            else:
                winner = 2
                return winner
        if i == 0:
            if matrix[i+2][0] == matrix[i+1][1] == matrix[i][2] != 0:
                if turn == 0:
                    winner = 1
                    return winner
                else:
                    winner = 2
                    return winner
            if matrix[i][i] == matrix[i+1][i+1] == matrix[i+2][i+2] != 0:
                if turn == 0:
                    winner = 1
                    return winner
                else:
                    winner = 2
                    return winner
    if winner == 0:
        for i in range(0,len(matrix)):
            for j in range(0,len(matrix[i])):
                if matrix[i][j] == 0:
                    hasBlank = True

    if hasBlank == False:
        winner = 3
        return winner


# UI that will pop out when a Draw happened
def drawUI(matrix):
    clear_console()
    menu()
    print(Style.DIM+"     1   2   3 ")
    print(Style.DIM+"   ____________")
    print(Style.DIM+"  |")
    for i in range(len(matrix)):
        print(Style.DIM+f"{i+1} |", end=" ")
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                print(Style.DIM+"[ ]", end=" ")
            elif matrix[i][j] == 1:
                print(Style.DIM+" X ", end=" ")
            else:
                print(Style.DIM+" O ", end=" ")
        print()
        if i < 2:
            print(Style.DIM+"  |")
    print(Style.DIM+"   ____________\n")


# This function identifies the coordinates of the winning line.
# It returns a list of three (row, col) tuples if a win is found, otherwise None.
def get_winning_line(matrix):
    # Check rows
    for r in range(3):
        if matrix[r][0] == matrix[r][1] == matrix[r][2] != 0:
            return [(r, 0), (r, 1), (r, 2)]
    # Check columns
    for c in range(3):
        if matrix[0][c] == matrix[1][c] == matrix[2][c] != 0:
            return [(0, c), (1, c), (2, c)]
    # Check diagonals
    if matrix[0][0] == matrix[1][1] == matrix[2][2] != 0:
        return [(0, 0), (1, 1), (2, 2)]
    if matrix[0][2] == matrix[1][1] == matrix[2][0] != 0:
        return [(0, 2), (1, 1), (2, 0)]
    return None


# Function for choosing which symbol to start with
def chooseSym():
    while True:
        print("Select 1st Player:")
        choice = input("Type 'X' or 'O': ")
        print()
        if choice.lower() == "x":
            clear_console()
            menu()
            print("Player 1 is 'X'\nPlayer 2 is 'O'")
            return True
        elif choice.lower() == "o":
            clear_console()
            menu()
            print("Player 1 is 'O'\nPlayer 2 is 'X'")
            return False
        else:
            print(Fore.RED+"Invalid Input")
            time.sleep(1)
            clear_console()
            menu()
