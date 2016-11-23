import random
from PIL import Image

minRow = 20
maxRow = 50

minCol = 20
maxCol = 50

class ImageArray:

    def __init__(self):
        self.row = random.randint(minRow, maxRow)
        self.col = random.randint(minCol, maxCol)
        self.color = 0 #black in L mode

        self.imageArray = [[1 for i in range(self.col)] for i in range(self.row)]


    def __setitem__(self, index, value):
        self.imageArray[index[0]][index[1]] = value

    def setColor(self, color):
        self.color = color

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


    def saveToPNG(self, path='out.png'):
        img = Image.new("LA", (self.col, self.row))
        imgDataList = [(self.color, 255*i) for i in self.flattenImageArray()]
        img.putdata(imgDataList)
        img.save(path)     


    def flattenImageArray(self):
        flatImageArray = []
        for sublist in self.imageArray:
            for item in sublist:
                flatImageArray.append(item)

        return flatImageArray
