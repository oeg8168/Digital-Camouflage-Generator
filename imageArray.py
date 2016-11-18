import random

def generateImageArray():

    minRow = 10
    maxRow = 20

    minCol = 10
    maxCol = 20
    
    row = random.randint(minRow, maxRow)
    col = random.randint(minCol, maxCol)

    imageArray = [[0 for i in range(col)] for i in range(row)]

    row = len(imageArray)
    col = len(imageArray[0])

    print('row: ' + str(row))   # show row size
    print('col: ' + str(col))   # show col size

    sizeText = str(row) + ' * ' + str(col)
    print(sizeText)

    for i in range(row):
        for j in range(col):
            print('O', end=' ')
        print()

#TODO: serprate generateImageArray
#def printImageArray():
        
