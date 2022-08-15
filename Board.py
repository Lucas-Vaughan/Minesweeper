
import random
from xmlrpc.client import Boolean


class Board:
    
    #variables
    #ok actually python apparently doesn't do variables up here I dislike this language lol
    #also I'm gonna use lists for the boards actually

    #All board functions should be used in set up of board, one function should be used to change board characters
    #All other board interactions should have their logic in interaction.py

    #Functions should accept input as x,y format, but board operations use [y][x] because double list goes down then across

    def __init__(self, width, height) -> None:
        #variables here
        self.width = width
        self.height = height
        self.board = [list(list())]

        for i in range(height):
            self.board.append(list())
            for j in range(width):
                self.board[i].append([".", "*"])

        # self.board = [["."]*width]*height
        print("Board initialized!")
    

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
        # print(self.board[x][y])
        currentChar = self.board[y][x][1]
        if currentChar == "*":
            self.board[y][x][1] = "F"
        elif currentChar == "F":
            self.board[y][x][1] = "*"
        else:
            print(f"{x},{y} has already been revealed!")
    
    def reveal(self, x:int, y:int):
        # isLose = False
        self.board[y][x][1] = "_"
        if(self.board[y][x][0] == "x"):
            # isLoss = True
            print("GAME OVER")
            #trigger game over once created
        # return isLoss
    
    
    # def reveal(self, x:int, y:int):
    #     # print(self.board[x][y])

    #     count = 0
        
    #     #check if bomb
    #     if self.board[x][y] == "x":
    #         print("GAME OVER")
    #         #reveal board/end game
    #         pass
        
    #     #if empty then count
    #     for i in range(y-1,y+2):
    #         if i >= 0 and i < self.height:
    #             for j in range(x-1,x+2):
    #                 if j >= 0 and j < self.width and self.board[j][i] == "x":
    #                     count += 1
    #     self.board[x][y] = count

    #----------Board setup functions below----------

    def printBoard(self, isNum:bool):
        # print(self.board)

        try:
            print(f"Printed Board:")
            for i in range(len(self.board)):
                for j in range(len(self.board[i])):
                    # print(i,j, end="|")
                    if(isNum or self.board[i][j][1] == "_"):
                        print(self.board[i][j][0], end=" ")
                    else:
                        print(self.board[i][j][1], end=" ")
                print()
            
        except:
            print("Board couldn't print :<")
    
    def addMine(self, x:int, y:int):
        # print(self.board[x][y])
        self.board[y][x][0] = "x"

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
    
    def addRandomMine(self):
        x = random.randrange(0, self.width)
        y = random.randrange(0, self.height)
        self.board[y][x][0] = "x"

    def addRandomMines(self, amount:int):
        for _ in range(amount):
            Board.addRandomMine(self)
    
    def obscure(self):
        #go thru board, replace all with "*"
        for y in range(self.height):
            for x in range(self.width):
               self.board[y][x][1] = "*"

    #MOVE TO interaction.py
    def isWin(self) -> bool:
        win = True
        for y in range(self.height):
            for x in range(self.width):
                if(self.board[y][x][1] == "*" and self.board[y][x][0] != "x"):
                    win = False
        return win