from Board import Board

class Game:

    def __init__(self) -> None:
        self.winCount = 0
        self.board = self.newBoard()
        # class gameState(enum.Enum):
        #     interaction = 1
        #     win = 2
        #     loss = 3

    def newBoard(self, width:int=7, height:int=5) -> Board:
        board = Board(width,height)
        
        board.addRandomMines(6)
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
            print("info (wip)- gives you information about the given board and game")
            print("flag x,y - makes a flag on the space")
            print("reveal x,y - reveal a space")
            print("    Coordinate commands can be chained by adding a new set of coordinates like so:")
            print("    reveal 1,2 5,4 2,3 ...")
            print("newgame - stops the current game and starts a new")
            print("guide - toggles the coordinate guide on the edge")
            print("exit - stop playing the game\n")
        elif(command.startswith("exit")):
            self.exit()
        elif(command.startswith("info")):
            print("Board characteristics:")
            print(f"\n\tWidth: {self.board.width}")
            print(f"\n\tHeight: {self.board.height}")
            print(f"\n\tMines: {self.board.height}")
        elif(command.startswith("guide")):
            self.board.guideCoords = not self.board.guideCoords
            # show the player the board after appropriate commands
            self.board.printBoard(False)
        elif(command.replace(" ","").startswith("newgame")):
            command = input("Are you sure? (y/n)\n").lower()
            print()
            if(command == "y"):
                self.board = self.newBoard()
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

                coordList = command.split(" ")
                del coordList[0]
                # for thing in coordList:
                #     print(f"Coord {thing}")
                for i in range(len(coordList)):
                    coords = coordList[i].split(",")
                    coordList[i] = (int(coords[0])-1, int(coords[1])-1)
                    print(f"coordList[{i}] = {coordList[i]}")
                    # for thing in coordList[i]:
                    #     print(f"For thing in coordList[{i}] = {thing}")
                
                
            except:
                print("Your response is formatted wrong, try again!")
                self.interact()
                #return so once you get a working response the failed responses don't recurse
                return
        
        #check for which command and use args to fulfill command       
        if(command.startswith("flag")):
            # print("flag command done")
            for coords in coordList:
                # print(f"flag coord[0] = {coords[0]} coord[1] = {coords[1]}")
                self.board.addFlag(coords[0], coords[1])
            self.board.printBoard(False)
        
        elif(command.startswith("reveal")):
            for coords in coordList:
                self.board.reveal(coords[0], coords[1])
            self.board.printBoard(False)
        
        #end by showing what the player did (9/17 changing this bc sometimes it is counterintuitive for some commands)
        # print()
        # self.board.printBoard(False)

        #call interact again until player exits
        if(not self.board.isWin()):
            self.interact()
            #I believe this will prevent issues when starting a new game
            return
        
        #start again and add a win once win
        self.winCount += 1
        self.board = self.newBoard()
        self.interact()
        
        
