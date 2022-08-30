from code import interact
from interaction import interaction
from minesweeperText import minesweeperText
from Board import Board
from Game import Game
import copy

class main:
    
    realBoard = Board(7,5)
    
    realBoard.addRandomMines(6)
    realBoard.numberAll()

    realBoard.printBoard(False)
    
    game = Game(realBoard)
    while(realBoard.isWin() == False):
        game.interact()
    print("YOU WON! NICEEE")

main()