from Cell import Cell, Board
import argparse
ap = argparse.ArgumentParser()
ap.add_argument("width")
ap.add_argument("height")
ap.add_argument("bombs")
args = vars(ap.parse_args())
board = Board(args['width'],args['height'],args['bombs'])
positionOfBombs = board.initializeBombs()
cells = []
for bomb in positionOfBombs:
    for cell in bomb.getNeighbors(board):
        if cell not in cells:
            cell.increaseBomb()
            cells.append(cell)
        else:
            cells[cells.index(cell)].increaseBomb()

for i in range(1,board.width+1):
    for j in range(1,board.height+1):
        dummyCell = Cell(i,j)
        if dummyCell in cells:
            print(cells[cells.index(dummyCell)].numberOfBombs,end="")
        elif Cell(i,j,True) in positionOfBombs:
            print('*',end='')
        else:
            print(' ',end='')
    print()