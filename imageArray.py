import random

minRow = 10
maxRow = 20

minCol = 10
maxCol = 20

class ImageArray:

    def __init__(self):
        self.row = random.randint(minRow, maxRow)
        self.col = random.randint(minCol, maxCol)

        self.imageArray = [[1 for i in range(self.col)] for i in range(self.row)]


    def __setitem__(self, index, value):
        self.imageArray[index[0]][index[1]] = value


    def printImageArraySize(self):
        print('row: ' + str(self.row))   # show row size
        print('col: ' + str(self.col))   # show col size

        sizeText = str(self.row) + ' * ' + str(self.col)
        print(sizeText)

        
    def printImageArray(self):
        for i in range(self.row):
            for j in range(self.col):
                print(self.imageArray[i][j], end=' ')
            print()
        print()


    def save(self, path):
        pass

    def flattenImageArray(self):
        flatImageArray = []
        for sublist in self.imageArray:
            for item in sublist:
                flatImageArray.append(item)

        return flatImageArray
