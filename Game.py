from ast import While
from pickle import NEWOBJ
from Board import Board

class Game:

    def __init__(self) -> None:
        self.winCount = 0
        self.initialized = False
        self.board = self.newBoard()
        # class gameState(enum.Enum):
        #     interaction = 1
        #     win = 2
        #     loss = 3

    def newBoard(self, width:int=7, height:int=5, mines:int=6) -> Board:
        self.initialized = False
        print()
        print("Beginner (10 mines):")
        print("    1|8x8 board")
        print("    2|9x9 board")
        print("    3|10x10 board")
        print("Intermediate (40 mines):")
        print("    4|13x15 board")
        print("    5|16x16 board")
        print("Expert (99 mines):")
        print("    6|30x16 board")
        print("Custom:")
        print("    7|Your choice!")
        print()

        width = 8
        height = 8
        mines = 10

        while(True):
            try:
                boardChoice = input("Select a board:\n")
                if(boardChoice.startswith("exi")):
                    self.exit()
                boardChoice = int(boardChoice)
                print()
            except TypeError:
                boardChoice = -1

            if(boardChoice == 1):
                width = 8
                height = 8
                mines = 10
                break
            elif(boardChoice == 2):
                width = 9
                height = 9
                mines = 10
                break
            elif(boardChoice == 3):
                width = 10
                height = 10
                mines = 10
                break
            elif(boardChoice == 4):
                width = 13
                height = 15
                mines = 40
                break
            elif(boardChoice == 5):
                width = 16
                height = 16
                mines = 40
                break
            elif(boardChoice == 6):
                width = 30
                height = 16
                mines = 99
                break
            elif(boardChoice == 7):
                while(True):
                    try:
                        width = int(input("Width: "))
                        break
                    except:
                        print("\nEnter a number\n")
                while(True):
                    try:
                        height = int(input("Height: "))
                        break
                    except:
                        print("\nEnter a number\n")
                while(True):
                    try:
                        mines = int(input("Mines: "))
                        break
                    except:
                        print("\nEnter a number\n")
                print()
                break
            else:
                print("Select a given number\n")


        # if()
        
        board = Board(width,height,mines)
        
        board.prepBoard()

        return board      
    
    def exit(self):
        print(f"You won {self.winCount} games!\nThanks for playing!")
        exit()

    def interact(self):

        # #start by showing the player what the board looks like
        # print()
        # self.board.printBoard(False)

        #ask the player what they want to do
        command = input("What do you want to do? type help for available commands\n").lower()
        print()
        
        #check for commands w/out args
        if(command.startswith("help")):
            print("help - help ofc :p")
            print("info - gives you information about the given board and game")
            print("flag x,y - makes a flag on the space")
            print("reveal x,y - reveal a space")
            print("    Coordinate commands can be chained by adding a new set of coordinates like so:")
            print("    reveal 1,2 5,4 2,3 ...")
            print("newgame - stops the current game and starts a new")
            print("guide - toggles the coordinate guide on the edge")
            print("exit - stop playing the game")
            print()
        elif(command.startswith("exi")): #Command check shortened to 3 letters to remain unique but allow typos
            self.exit()
        elif(command.startswith("inf")):
            print("Board characteristics:")
            print(f"    Width: {self.board.width}")
            print(f"    Height: {self.board.height}")
            print(f"    Mines: {self.board.mines}")
            print()
            print("Game characteristics:")
            print(f"    Wins: {self.winCount}")
            print(f"    Flags: {self.board.flags}")
            print()

        elif(command.startswith("gui")):
            self.board.guideCoords = not self.board.guideCoords
            # show the player the board after appropriate commands
            self.board.printBoard(False)
        elif(command.replace(" ","").startswith("newgame")):
            command = input("Are you sure? (y/n)\n").lower()
            print()
            if(command == "y"):
                self.board = self.newBoard()
                self.initialized = False
            else:
                self.board.printBoard(False)
            
        #secret command to print fully revealed board
        elif(command.startswith("printall")):
            self.board.printBoard(True)
        # elif(command.startswith("revealall")):
        #     for i in range(self.board.height):
        #         for j in range(self.board.width):
        #             self.board.reveal(j,i)
        
        #rest of commands require an argument, retry input if formatted wrong
        else:
            try:
                # #coords are the second part of command, ex the 2,3 in "flag 2,3"
                # coords = command.split(" ")[1].split(",")
                # #format coords as integers
                # coords[0] = int(coords[0])-1
                # coords[1] = int(coords[1])-1
                
                # if len(coords) != 2:
                #     return

                coordList = command.rstrip().split(" ")
                del coordList[0]
                # for thing in coordList:
                #     print(f"Coord {thing}")
                for i in range(len(coordList)):
                    coords = coordList[i].split(",")
                    coordList[i] = (int(coords[0])-1, int(coords[1])-1)
                    # print(f"coordList[{i}] = {coordList[i]}")
                    # for thing in coordList[i]:
                    #     print(f"For thing in coordList[{i}] = {thing}")
                
                
            except:
                print("Your response is formatted wrong, try again!")
                self.interact()
                #return so once you get a working response the failed responses don't recurse
                return
        
        #check for which command and use args to fulfill command       
        if(command.startswith("fla")):
            # print("flag command done")
            for coords in coordList:
                # print(f"flag coord[0] = {coords[0]} coord[1] = {coords[1]}")
                self.board.addFlag(coords[0], coords[1])
            print()
            self.board.printBoard(False)
        
        elif(command.startswith("rev")):
            for coords in coordList:
                if(not self.initialized):
                    self.board.startGame(coords[0],coords[1])
                    self.initialized = True
                self.board.reveal(coords[0], coords[1])
                print()
            self.board.printBoard(False)
        
        #end by showing what the player did (9/17 changing this bc sometimes it is counterintuitive for some commands)
        # print()
        # self.board.printBoard(False)

        if(self.board.isLose):
            playAgain = input("Do you want to play a new board? (y/n)\n").lower()
            print()
            while(not playAgain.startswith("y") and not playAgain.startswith("n")):
                print(f'"{playAgain}" was an invalid response')
                playAgain = input("Do you want to play a new board? (y/n)\n").lower()
                print()
                
            if(playAgain.startswith("y")):
                self.board = self.newBoard()
            elif(playAgain.startswith("n")):
                self.exit()
            else:
                print("Unexpected response")
                exit()

        #call interact again until player exits
        if(not self.board.isWin()):
            self.interact()
            #I believe this will prevent issues when starting a new game
            return
        
        #start again and add a win once win
        print("You won!")
        self.winCount += 1
        self.board = self.newBoard()
        self.interact()
        
        
