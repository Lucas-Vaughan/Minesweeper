
from asyncio import protocols
import random
from sys import flags
from xmlrpc.client import Boolean


class Board:
    
    #variables
    #ok actually python apparently doesn't do variables up here I dislike this language lol
    #also I'm gonna use lists for the boards actually

    #All board functions should be used in set up of board, one function should be used to change board characters
    #All other board interactions should have their logic in interaction.py

    #Functions should accept input as x,y format, but board operations use [y][x] because double list goes down then across

    #Class Variables (shared among all instances):
    guideCoords = True #Make False

    def __init__(self, width, height, mines) -> None:
        #variables here
        self.width = width
        self.height = height
        self.board = [list(list())]
        self.mines = mines
        self.flags = 0
        self.isLose = False
        self.protectedx = (-1,-1)
        self.protectedy = (-1,-1)
        
        for i in range(height):
            self.board.append(list())
            for j in range(width):
                self.board[i].append([".", "*"])

        print("Board initialized!\n")
    

    def validCoords(self, x:int, y:int) -> Boolean:
        isValid = True
        #check if between x size
        if (x < 0 or x >= self.width):
            isValid = False
        if (y < 0 or y >= self.height):
            isValid = False
        return isValid

    #----------Board interaction functions below----------
    
    def addFlag(self, x:int, y:int):

        #dont run if invalid coords
        if(not self.validCoords(x,y)):
            print("\nInvalid coordinates! Try again")
            return

        # print(self.board[x][y])
        currentChar = self.board[y][x][1]
        if currentChar == "*":
            self.board[y][x][1] = "F"
            self.flags += 1
        elif currentChar == "F":
            self.board[y][x][1] = "*"
            self.flags -= 1
        else:
            print(f"{x+1},{y+1} has already been revealed!")
            return
        
        print(f"Flagged {x+1},{y+1}")
    
    def reveal(self, x:int, y:int):

        #dont run if invalid coords
        if(not self.validCoords(x,y)):
            print("\nInvalid coordinates! Try again")
            return

        if(self.board[y][x][1] == "*"):
            self.board[y][x][1] = "_"
        elif(self.board[y][x][1] == "F"):
            print(f"{x+1},{y+1} is flagged")
            return
        else:
            print(f"Already revealed {x+1},{y+1}")
            return

        #if tile is ".", reveal surrounding spaces too
        if(self.board[y][x][0] == "."):
            
            #check if up is in bounds
            if(y-1 >= 0):
                #center
                if(self.board[y-1][x][1] != "_"):
                    self.reveal(x,y-1)

                #left
                if(x-1 >= 0 and self.board[y-1][x-1][1] != "_"):
                    self.reveal(x-1,y-1)
                
                #right
                if(x+1 < self.width and self.board[y-1][x+1][1] != "_"):
                    self.reveal(x+1,y-1)
            
            #check sides

            #left
            if(x-1 >= 0 and self.board[y][x-1][1] != "_"):
                self.reveal(x-1,y)
            
            #right
            if(x+1 < self.width and self.board[y][x+1][1] != "_"):
                self.reveal(x+1,y)
            
            #check if down is in bounds
            if(y+1 < self.height):
                #center 
                if(self.board[y+1][x][1] != "_"):
                    self.reveal(x,y+1)

                #left
                if(x-1 >= 0 and self.board[y+1][x-1][1] != "_"):
                    self.reveal(x-1,y+1)
                
                #right
                if(x+1 < self.width and self.board[y+1][x+1][1] != "_"):
                    self.reveal(x+1,y+1)



        if(self.board[y][x][0] == "x"):
            self.isLose = True
            print("GAME OVER")
            return
            #trigger game over once created
        # return isLoss
        print(f"Revealed {x+1},{y+1}")
    
    #----------Board setup functions below----------

    def printBoard(self, isNum:bool):

        xDigitLength = 1
        yDigitLength = 1

        offset = 0
        if(self.guideCoords):
            offset = 2
            xDigitLength = len(str(self.width))
            yDigitLength = len(str(self.height))

        output = ""
        try:
            output += f"Flags:{self.flags}/{self.mines}".center(offset+(1+xDigitLength)*self.width)
            output += "\n"
            for i in range(len(self.board) -1 + offset):
                #if guideCoord add number and separator at row start
                if(self.guideCoords and i <= 1):
                    output += "".rjust(yDigitLength+1)
                elif(self.guideCoords and i < self.height + offset):
                    output += f"{i-1}|".rjust(yDigitLength+1)
                
                for j in range(self.width):
                    #if guideCoord add numbered row
                    if(self.guideCoords and i == 0):
                        output += f"{j+1}".rjust(xDigitLength+1)
                    #if guideCoord add separator row
                    elif(self.guideCoords and i == 1):
                        output += "---"[:xDigitLength+1].ljust(xDigitLength+1)
                    #print normal stuff
                    elif(isNum or self.board[i-offset][j][1] == "_"):
                        output += f" {self.board[i-offset][j][0]}".center(xDigitLength+1)
                    elif(i < self.height+offset):
                        output += f" {self.board[i-offset][j][1]}".center(xDigitLength+1)
                output += "\n"
            
        except:
            output += "Board couldn't print :<"
        print(output)
    
    def addMine(self, x:int, y:int):
        # print(self.board[x][y])
        self.board[y][x][0] = "x"

    def addRandomMine(self):
        #not the best way to prevent repeat mines but works ok in reasonable circumstances
        while(True):
            x = random.randrange(0, self.width)
            y = random.randrange(0, self.height)
            #check that mine is outside of starting area
            if((self.board[y][x][0] != "x" ) and (x < self.protectedx[0] or x > self.protectedx[1] or y < self.protectedy[0] or y > self.protectedy[1])):
                # print(f"added mine at {x+1},{y+1}")
                self.board[y][x][0] = "x"
                break
            # print("repeated")

    def addRandomMines(self, amount:int):
        for _ in range(amount):
            Board.addRandomMine(self)
    
    def obscure(self):
        #go thru board, replace all with "*"
        for y in range(self.height):
            for x in range(self.width):
               self.board[y][x][1] = "*"
    def clearNumbers(self):
        #go thru board, replace non x's with "."
        for y in range(self.height):
            for x in range(self.width):
                if(self.board[y][x][0] != "x"):
                    self.board[y][x][0] = "."
    
    def numberAll(self):
        #Only use on new board, does not account for existing numbers (nvm working on that)
        Board.clearNumbers(self)
        
        #check for x's
        for y in range(self.height):
            for x in range(self.width):
                if(self.board[y][x][0] == "x"):
                    # print("Checkpoint", x, y)

                    #add 1 to surrounding count
                    for j in range(y-1,y+2):
                        #check within board range
                        if j >= 0 and j < self.height:
                            for i in range(x-1,x+2):
                                if i >= 0 and i < self.width:
                                    try:
                                        self.board[j][i][0] = int(self.board[j][i][0]) + 1
                                        # print("it worked!")
                                    except:
                                        if(self.board[j][i][0] == "."):
                                            self.board[j][i][0] = "1"

    def startGame(self, x:int, y:int):
        print(f"Starting game with: {x},{y}")
        replacedMines = 0
        self.protectedx = (x,x)
        self.protectedy = (y,y)

        #check if up is in bounds
        if(y-1 >= 0):
            print("Up in bounds")
            self.protectedy = (y-1,self.protectedy[1])
            #center
            if(self.board[y-1][x][0] == "x"):
                self.board[y-1][x][0] = "."
                replacedMines += 1

            #left
            if(x-1 >= 0 and self.board[y-1][x-1][0] == "x"):
                self.board[y-1][x-1][0] = "."
                replacedMines += 1
            
            #right
            if(x+1 < self.width and self.board[y-1][x+1][0] == "x"):
                self.board[y-1][x+1][0] = "."
                replacedMines += 1

        #check sides

        #left
        if(x-1 >= 0):
            print("Left in bounds")
            self.protectedx = (x-1,self.protectedx[1])
            if(self.board[y][x-1][0] == "x"):
                self.board[y][x-1][0] = "."
                replacedMines += 1

        #center
        if(self.board[y][x][0] == "x"):
                self.board[y][x][0] = "."
                replacedMines += 1

        #right
        if(x+1 < self.width):
            print("Right in bounds")
            self.protectedx = (self.protectedx[0],x+1)
            if(self.board[y][x+1][0] == "x"):
                self.board[y][x+1][0] = "."
                replacedMines += 1

        #check if down is in bounds
        if(y+1 < self.height):
            print("Down in bounds")
            self.protectedy = (self.protectedy[0],y+1)
            #center 
            if(self.board[y+1][x][0] == "x"):
                self.board[y+1][x][0] = "."
                replacedMines += 1

            #left
            if(x-1 >= 0 and self.board[y+1][x-1][0] == "x"):
                self.board[y+1][x-1][0] = "."
                replacedMines += 1

            #right
            if(x+1 < self.width and self.board[y+1][x+1][0] == "x"):
                self.board[y+1][x+1][0] = "."
                replacedMines += 1
        
        print(f"Protectedx: {self.protectedx} Protectedy:{self.protectedy}")
        print(f"ReplacedMines: {replacedMines}")
        for _ in range(replacedMines):
            print("Added mine")
            self.addRandomMine()
        self.numberAll()


    def isWin(self) -> bool:
        win = True
        for y in range(self.height):
            for x in range(self.width):
                if(self.board[y][x][1] != "_" and self.board[y][x][0] != "x"):
                    win = False
        return win
    
    def prepBoard(self):
        self.isLose = False
        self.addRandomMines(self.mines)
        self.numberAll()

        self.printBoard(False)