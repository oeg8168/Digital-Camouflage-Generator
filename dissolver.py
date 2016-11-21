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
            inputImageArray[j, i] = 0

def dissolveFromBottom(inputImageArray):
    depth = randomDepthVertical(inputImageArray)

    # For test purpose
    printDissolveInfo('Bottom', depth)

    for i in range(inputImageArray.col):
        for j in range(depth[i]):
            inputImageArray[inputImageArray.row-1-j, i] = 0

def dissolveFromLeft(inputImageArray):
    depth = randomDepthHorizontal(inputImageArray)
    
    # For test purpose
    printDissolveInfo('Left', depth)

    for i in range(inputImageArray.row):
        for j in range(depth[i]):
            inputImageArray[i, j] = 0

def dissolveFromRight(inputImageArray):
    depth = randomDepthHorizontal(inputImageArray)
    
    # For test purpose
    printDissolveInfo('Right', depth)

    for i in range(inputImageArray.row):
        for j in range(depth[i]):
            inputImageArray[i, inputImageArray.col-1-j] = 0


def randomDepthVertical(inputImageArray):
    maxDepth = math.floor(inputImageArray.row/3)
    #depth = [random.randint(0, maxDepth) for i in range(inputImageArray.col)]
    depth = [random.randint(0, maxDepth)]
    
    for i in range(inputImageArray.col):
        newStep = random.randint(-2, 2)
        newElement = depth[i] + newStep
        if newElement < 0:
            depth.append(0)
        else:
            depth.append(newElement)

    return depth

def randomDepthHorizontal(inputImageArray):
    maxDepth = math.floor(inputImageArray.col/3)
    #depth = [random.randint(0, maxDepth) for i in range(inputImageArray.row)]
    depth = [random.randint(0, maxDepth)]
    
    for i in range(inputImageArray.row):
        newStep = random.randint(-2, 2)
        newElement = depth[i] + newStep
        if newElement < 0:
            depth.append(0)
        else:
            depth.append(newElement)

    return depth

def printDissolveInfo(direction, depth):
    print(direction)
    print('depth:')
    for i in depth:
        print(i, end=' ')
    print()
