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
    maxStartPoint = math.floor(inputImageArray.row/3)
    startPoint = random.randint(0, maxStartPoint)
    depth = [startPoint]
    
    for i in range(inputImageArray.col):
        newStep = getStep()
        newElement = depth[i] + newStep
        newElement = keepDepthWithinRange(newElement, inputImageArray.row)
        depth.append(newElement)

    return depth

def randomDepthHorizontal(inputImageArray):
    maxStartPoint = math.floor(inputImageArray.col/3)
    startPoint = random.randint(0, maxStartPoint)
    depth = [startPoint]
    
    for i in range(inputImageArray.row):
        newStep = getStep()
        newElement = depth[i] + newStep
        newElement = keepDepthWithinRange(newElement, inputImageArray.col)
        depth.append(newElement)

    return depth


def keepDepthWithinRange(element, bound):
    if element < 0:
        element = 0
    elif element > bound:
        element = bound

    return element


def getStep(ruggedness = 2):
    return random.randint(-1*ruggedness, 1*ruggedness)


def printDissolveInfo(direction, depth):
    print(direction)
    print('depth:')
    for i in depth:
        print(i, end=' ')
    print()
