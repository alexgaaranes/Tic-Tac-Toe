# TICTACTOE by Alexander Gabriel Aranes, BSCS Freshman, UPLB
# This is made as a practice for upcoming midterms of 1st semester Freshman year. This program has all the learnings through the CMSC 12 course as of October 8, 2023 integrated and made into a full game. However, this uses a data structrure which is a lesson advance than the lessons taught as of the date mentioned.
# Features: Menu, row and column input, clean UI using repetitive execution and clearing console. Colored text using colorama.


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



        
