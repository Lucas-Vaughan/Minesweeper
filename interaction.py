import imp
from Board import Board

class interaction:

    def __init__(self, board) -> None:
        self.board = board

    def flag(self, x:int, y:int):
        self.board.addFlag(x,y)
        # print(f"You would've flagged x:{x} y:{y}")
