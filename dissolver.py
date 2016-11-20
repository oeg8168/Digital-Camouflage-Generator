import random
import math


def dissolve(inputImageArray):
    dissolveFromTop(inputImageArray)
    inputImageArray.printImageArray()

    dissolveFromBottom(inputImageArray)
    inputImageArray.printImageArray()

    dissolveFromLeft(inputImageArray)
    inputImageArray.printImageArray()

    dissolveFromRight(inputImageArray)
    inputImageArray.printImageArray()


def dissolveFromTop(inputImageArray):
    depth = randomDepthVertical(inputImageArray)

    # For test purpose
    printDissolveInfo('Top', depth)
    
    for i in range(inputImageArray.col):
        for j in range(depth[i]):
            inputImageArray[j, i] = ' '

def dissolveFromBottom(inputImageArray):
    depth = randomDepthVertical(inputImageArray)

    # For test purpose
    printDissolveInfo('Bottom', depth)

    for i in range(inputImageArray.col):
        for j in range(depth[i]):
            inputImageArray[inputImageArray.row-1-j, i] = ' '

def dissolveFromLeft(inputImageArray):
    depth = randomDepthHorizontal(inputImageArray)
    
    # For test purpose
    printDissolveInfo('Left', depth)

    for i in range(inputImageArray.row):
        for j in range(depth[i]):
            inputImageArray[i, j] = ' '

def dissolveFromRight(inputImageArray):
    depth = randomDepthHorizontal(inputImageArray)
    
    # For test purpose
    printDissolveInfo('Right', depth)

    for i in range(inputImageArray.row):
        for j in range(depth[i]):
            inputImageArray[i, inputImageArray.col-1-j] = ' '


def randomDepthVertical(inputImageArray):
    maxDepth = math.floor(inputImageArray.row/3)
    depth = [random.randint(0, maxDepth) for i in range(inputImageArray.col)]
    return depth

def randomDepthHorizontal(inputImageArray):
    maxDepth = math.floor(inputImageArray.col/3)
    depth = [random.randint(0, maxDepth) for i in range(inputImageArray.row)]
    return depth

def printDissolveInfo(direction, depth):
    print(direction)
    print('depth:')
    for i in depth:
        print(i, end=' ')
    print()
