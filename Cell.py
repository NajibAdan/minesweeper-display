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
positionOfBombs = []
class Cell:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.numberOfBombs = 0
    def getNeighbors(self):
        possibleNeighbors = []
        for movement in MOVEMENTS:
            x = self.x+movement[0]
            y = self.y + movement[1]
            if ( x>=1 and x<=16) and (y>=1 and y<=16) and (Bomb(x,y) not in positionOfBombs):
                possibleNeighbors.append(Cell(x,y))
        return possibleNeighbors
    def increaseBomb(self):
        self.numberOfBombs = self.numberOfBombs + 1
    def __eq__(self, object):
        return (self.x==object.x) and (self.y == object.y)

class Bomb(Cell):
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.bomb = True
    def isBomb(self):
        if self.bomb:
            return True
        else:
            return True
    def pickPosition():
        temp = Bomb(randint(1,16),randint(1,16))
        while temp in positionOfBombs:
            temp = Bomb(randint(1,16),randint(1,16))
        return temp
    def initializeBombs(NUMBER_OF_BOMBS):
        for _ in range(NUMBER_OF_BOMBS):
            positionOfBombs.append(Bomb.pickPosition())
        return positionOfBombs