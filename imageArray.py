import random

minRow = 10
maxRow = 20

minCol = 10
maxCol = 20

class ImageArray:

    def __init__(self):
        self.row = random.randint(minRow, maxRow)
        self.col = random.randint(minCol, maxCol)

        self.imageArray = [[0 for i in range(self.col)] for i in range(self.row)]

    
    def printImageArray(self):
        print('row: ' + str(self.row))   # show row size
        print('col: ' + str(self.col))   # show col size

        sizeText = str(self.row) + ' * ' + str(self.col)
        print(sizeText)

        for i in range(self.row):
            for j in range(self.col):
                print('O', end=' ')
            print()          
