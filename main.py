from random import randint
from Cell import Cell, Bomb
NUMBER_OF_BOMBS = 40
positionOfBombs = Bomb.initializeBombs(NUMBER_OF_BOMBS)
cells = []
for bomb in positionOfBombs:
    for cell in bomb.getNeighbors():
        if cell not in cells:
            cell.increaseBomb()
            cells.append(cell)
        else:
            cells[cells.index(cell)].increaseBomb()
        

for i in range(1,17):
    for j in range(1,17):
        dummyCell = Cell(i,j)
        if dummyCell in cells:
            print(cells[cells.index(dummyCell)].numberOfBombs,end="")
        elif Cell(i,j) in positionOfBombs:
            print('*',end='')
        else:
            print(' ',end='')
    print()


