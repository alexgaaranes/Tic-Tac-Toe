# Tic-Tac-Toe
<sub>Tic-Tac-Toe made in Python with Colorama</sub>

### TICTACTOE by Alexander Gabriel Aranes, BSCS Freshman, UPLB

 This was made as a practice for upcoming midterms of 1st semester Freshman year. This program has all my learnings through the CMSC 12 course as of October 8, 2023 integrated and made into a full game. However, this uses a data structrure which is a lesson advance than the lessons taught as of the date mentioned.

I'm willing to receive any comments and criticism to improve.

<sub>Est. time taken: 6 - 8 hrs</sub>

<sub>colorama: https://pypi.org/project/colorama/</sub>

**Features**: 
 - Menu
 - row and column input
 - clean UI using repetitive execution and clearing console
 - Colored text using colorama
 - 2 player
 - Looping until exit

**Plans**:
 - COM vs Player
 - Improved Ai
 - Optimized Code

### The Code
**Main python file**
```python
# Other libraries/Modules used
import func
import time
from colorama import Fore,Style,init
init(autoreset=True)


# Main
while True:

    # Matrix to be manipulated during the game
    matrix = [[0,0,0],
        [0,0,0],
        [0,0,0]]

    # This changes between 0 and 1 indicating turns of Player 1 and 2 respectively
    turn = 0

    # Main menu
    func.clear_console()
    func.menu()
    print(Fore.CYAN+"Press Enter to Play")
    entry = input("(Input any character to exit)\n")
    if entry != "":
        func.clear_console()
        break

    # Initialization  
    gameOver = False
    
    # Picking starting symbol
    func.clear_console()
    func.menu()
    roles = func.chooseSym()
    for i in range(3,0,-1):
        print(Style.DIM+"\nStarting in", i,"...")
        time.sleep(1)
    
    # Main game flow
    while gameOver == False:

        # Main Game, Showing the UI
        func.ui(matrix)
        cell,row,col = func.playerInput(matrix,roles,turn)
        matrix[row][col] = cell
        result = func.checkMatrix(matrix,turn)

        # Checking of Matrix; else continues the game
        if result == 1:
            func.winUI(matrix)
            print(Fore.MAGENTA+"Player 1 WINS")
            input("Press Enter to Continue")
            gameOver = True
        elif result == 2:
            func.winUI(matrix)
            print(Fore.MAGENTA+"Player 2 WINS")
            input("Press Enter to Continue")
            gameOver = True
        elif result == 3:
            func.drawUI(matrix)
            print(Fore.YELLOW+"DRAW")
            input("Press Enter to Continue")
            gameOver = True

        # Changes the turn between the two players
        if turn == 0:
            turn = 1
        else:
            turn = 0

```

**Functions python file**
```python
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
    row1,row2,row3,col1,col2,col3 = wincheckMatrix(matrix)
    for i in range(len(matrix)):
        print(Fore.YELLOW+f"{i+1} |", end=" ")
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                print(Fore.YELLOW+"[ ]", end=" ")
            elif matrix[i][j] == 1:
                if matrix[i][j] == matrix[row1][col1] == matrix[row2][col2] == matrix[row3][col3]:
                    print(Style.BRIGHT+Fore.GREEN+" X ", end=" ")
                else:
                    print(Fore.YELLOW+" X ", end=" ")
            else:
                if matrix[i][j] == matrix[row1][col1] == matrix[row2][col2] == matrix[row3][col3]:
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


# This function is more on coloring the winning connecting symbols
def wincheckMatrix(matrix):
    for i in range(0,len(matrix)):
        if matrix[i][0] == matrix[i][1] == matrix[i][2] != 0:
            row1 = matrix.index(matrix[i])
            row2 = matrix.index(matrix[i])
            row3 = matrix.index(matrix[i])
            col1 = matrix.index(matrix[0])
            col2 = matrix.index(matrix[1])
            col3 = matrix.index(matrix[2])
        if matrix[0][i] == matrix[1][i] == matrix[2][i] != 0:
            row1 = matrix.index(matrix[0])
            row2 = matrix.index(matrix[1])
            row3 = matrix.index(matrix[2])
            col1 = matrix.index(matrix[i])
            col2 = matrix.index(matrix[i])
            col3 = matrix.index(matrix[i])
        if i == 0:
            if matrix[i+2][0] == matrix[i+1][1] == matrix[i][2] != 0:
                row1 = matrix.index(matrix[i+2])
                row2 = matrix.index(matrix[i+1])
                row3 = matrix.index(matrix[i])
                col1 = matrix.index(matrix[0])
                col2 = matrix.index(matrix[1])
                col3 = matrix.index(matrix[2])
            if matrix[i][i] == matrix[i+1][i+1] == matrix[i+2][i+2] != 0:
                row1 = matrix.index(matrix[i])
                row2 = matrix.index(matrix[i+1])
                row3 = matrix.index(matrix[i+2])
                col1 = matrix.index(matrix[i])
                col2 = matrix.index(matrix[i+1])
                col3 = matrix.index(matrix[i+2])
    return row1,row2,row3,col1,col2,col3


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

```
