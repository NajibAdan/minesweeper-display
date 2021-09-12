from random import randint
MOVEMENTS = [
    [1,1],
    [1,0],
    [1,-1],
    [0,1],
    [0,-1],
    [-1,1],
    [-1,0],
    [-1,-1]
]
'''
    Creates the Cell Object,
    It takes in x,y and a boolean to indicate if the cell is a bomb or not
'''
class Cell:
    def __init__(self,x,y,isBomb=False):
        self.x = x
        self.y = y
        self.numberOfBombs = 0
        self.isBomb = isBomb
    '''
    Compares if two Cell objects are the same
    '''
    def __eq__(self, object):
        return (self.x==object.x) and (self.y == object.y) and (self.isBomb == object.isBomb)
    '''
    Returns the neighbors of a cell
    '''
    def getNeighbors(self, boardSize):
        possibleNeighbors = []
        for movement in MOVEMENTS:
            x = self.x+movement[0]
            y = self.y + movement[1]
            if ( x>=1 and x<=boardSize.width) and (y>=1 and y<=boardSize.height) and (Cell(x,y,True) not in boardSize.getPositions()):
                possibleNeighbors.append(Cell(x,y))
        return possibleNeighbors
    '''
    Increases the bomb counter of a cell
    '''
    def increaseBomb(self):
        self.numberOfBombs = self.numberOfBombs + 1

'''
Creates the board object and its properties
like width, height and the number of bombs 
on the board
'''
class Board():
    def __init__(self,width,height,bombs) -> None:
        self.width = int(width)
        self.height = int(height)
        self.bombs = int(bombs)
        self.positionOfBombs = []
    '''
    Picks which cells are bombs
    '''
    def pickPosition(self):
        temp = Cell(randint(1,self.width),randint(1,self.height),True)
        while temp in self.positionOfBombs:
            temp = Cell(randint(1,self.width),randint(1,self.height), True)
        return temp
    '''
    Initializes the board with bombs
    '''
    def initializeBombs(self):
        for _ in range(self.bombs):
            self.positionOfBombs.append(self.pickPosition())
        return self.positionOfBombs
    def getPositions(self):
        return self.positionOfBombs
    