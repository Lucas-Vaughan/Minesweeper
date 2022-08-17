import enum
import imp
from ntpath import join
from Board import Board

class Game:
    
    def __init__(self, board:Board) -> None:
        self.winCount = 0
        self.board = board
        # class gameState(enum.Enum):
        #     interaction = 1
        #     win = 2
        #     loss = 3      


    def newGame(self):
        pass

    def interact(self):

        # #start by showing the player what the board looks like
        # print()
        # self.board.printBoard(False)

        #ask the player what they want to do
        command = input("What do you want to do? type help for available commands\n").lower()
        
        #check for commands w/out args
        if(command.startswith("help")):
            print("\nhelp - help ofc :p \nflag x,y - makes a flag on the space \nreveal x,y - reveal a space \nguide - toggles the coordinate guide on the edge \nexit - stop playing the game\n")
        elif(command.startswith("exit")):
            print("EXITED!")
            return
        elif(command.startswith("guide")):
            self.board.guideCoords = not self.board.guideCoords
        
        #rest of commands require an argument, retry input if formatted wrong
        else:
            try:
                #coords are the second part of command, ex the 2,3 in "flag 2,3"
                coords = command.split(" ")[1].split(",")
                #format coords as integers
                coords[0] = int(coords[0])-1
                coords[1] = int(coords[1])-1
                for coord in coords:
                    print(coord)
                if len(coords) != 2:
                    return
            except:
                print("Your response is formatted wrong, try again!")
                self.interact()
                #return so once you get a working response the failed responses don't recurse
                return
        
        #check for which command and use args to fulfill command       
        if(command.startswith("flag")):
            print(f"Flagged {coords[0]},{coords[1]}")
            self.board.addFlag(coords[0], coords[1])
        
        elif(command.startswith("reveal")):
            print(f"Revealed {coords[0]},{coords[1]}")
            self.board.reveal(coords[0], coords[1])
        
        #end by showing what the player did
        print()
        self.board.printBoard(False)
            
        
        
