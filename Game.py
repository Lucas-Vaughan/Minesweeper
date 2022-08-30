from Board import Board

class Game:

    def __init__(self) -> None:
        self.winCount = 0
        self.board = self.newBoard()
        # class gameState(enum.Enum):
        #     interaction = 1
        #     win = 2
        #     loss = 3

    def newBoard(width:int=7, height:int=5) -> Board:
        board = Board(7,5)
        
        board.addRandomMines(1)
        board.numberAll()

        board.printBoard(False)
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
            print("flag x,y - makes a flag on the space")
            print("reveal x,y - reveal a space")
            print("guide - toggles the coordinate guide on the edge")
            print("exit - stop playing the game")
        elif(command.startswith("exit")):
            self.exit()
        elif(command.startswith("guide")):
            self.board.guideCoords = not self.board.guideCoords
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
                #coords are the second part of command, ex the 2,3 in "flag 2,3"
                coords = command.split(" ")[1].split(",")
                #format coords as integers
                coords[0] = int(coords[0])-1
                coords[1] = int(coords[1])-1
                
                if len(coords) != 2:
                    return
            except:
                print("Your response is formatted wrong, try again!")
                self.interact()
                #return so once you get a working response the failed responses don't recurse
                return
        
        #check for which command and use args to fulfill command       
        if(command.startswith("flag")):
            self.board.addFlag(coords[0], coords[1])
        
        elif(command.startswith("reveal")):
            self.board.reveal(coords[0], coords[1])
        
        #end by showing what the player did
        print()
        self.board.printBoard(False)

        #call interact again until player exits
        if(not self.board.isWin()):
            self.interact()
        
        #start again and add a win once win
        self.winCount += 1
        self.board = self.newBoard()
        self.interact()
        
        
