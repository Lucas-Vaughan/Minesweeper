
class minesweeperText:

    #start by creating the grid and objects
    grid = [list(list())]
    height = 1
    width = 1

    def __init__(self, height:int, width:int) -> None:
        self.grid = [["."]*width]*height
        print("minesweeperText Initialized!")
    

    def makeGrid(height:int, width:int):
    
        # for i in range(height):
        #     for j in range(width):
        #         grid.add(".")
        grid = [["."]*width]*height

        print("Grid created!")
        print(grid)
    
    def printGrid():
        try:
            for i in range(len(grid)):
                for j in range(len(grid[i])):
                    print(i,j, end="|")
                print()
        except:
            print("Grid couldn't print :<")