from camoImageFactory import *

import sys
import getopt
import random

def main(argv):

    width, height, camoImgNumber, outputFile = parseArguments(argv)

    print(width, height, camoImgNumber, outputFile)
    
    camoImageFactory = CamoImageFactory()

    canvasSize = (width, height)
    canvas = Image.new('LA', canvasSize, 'white')

    for i in range(camoImgNumber):
        camoImg = camoImageFactory.getCamoImage()
        
        img = camoImg.toImageObj()
        x = random.randint(-camoImg.col, width)
        y = random.randint(-camoImg.row, height)

        canvas.paste(img, (x, y), img.split()[1])
    
    canvas.save(outputFile)


def parseArguments(argv):
    
    try:
        opts, args = getopt.getopt(argv, 'w:h:n:o:')
    except getopt.GetoptError as e:
        print('error:', e)
        printUsage()
        exit(1)

    # defaults
    width, height = 200, 200
    camoImgNumber = 1000
    outputFile = 'output.png'

    try:
        for opt, arg in opts:
            print(opt, arg)
            if opt in '-w':
                width = int(arg)
            elif opt in '-h':
                height = int(arg)
            elif opt in '-n':
                camoImgNumber = int(arg)
            elif opt in '-o':
                outputFile = arg
    except Exception as e:
        print(e)
        exit(1)
    
    return width, height, camoImgNumber, outputFile


def printUsage():
    print('Usage: python DigitalCamouflageGenerator.py')
    print('       [-w <width>] [-h <height>]')
    print('       [-n <numberOfCamo>] [-r <ruggedness>]')
    print('       [-o <outputFile>]')
    

if __name__ == '__main__':
    main(sys.argv[1:])
