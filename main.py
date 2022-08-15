from code import interact
from interaction import interaction
from minesweeperText import minesweeperText
from Board import Board
from Game import Game
import copy

class main:
    # minesweeperText.makeGrid(2,3)
    # minesweeperText.printGrid()
    realBoard = Board(7,5)
    # realBoard.printBoard()

    realBoard.addRandomMines(6)
    realBoard.numberAll()

    # realBoard.printBoard()

    # playerBoard = realBoard
    # playerBoard = copy.deepcopy(realBoard)
    # playerBoard.obscure()
    # realBoard.reveal(3,2)
    realBoard.printBoard(True)
    realBoard.printBoard(False)
    # playerBoard.printBoard()

    game = Game(realBoard)
    while(realBoard.isWin() == False):
        game.interact()


    # print(minesweeperText.grid)

    # interaction.flag(0,2)

main()