from camoImageFactory import *

import random

if __name__ == '__main__':

    camoImageFactory = CamoImageFactory()

    canvasSize = (200, 200)
    canvas = Image.new('LA', canvasSize, 'white')

    camoImgNumber = 1000
    for i in range(camoImgNumber):
        camoImg = camoImageFactory.getCamoImage()
        
        img = camoImg.toImageObj()
        x = random.randint(-100, 200)
        y = random.randint(-100, 200)

        canvas.paste(img, (x, y), img.split()[1])

        # camoImg.saveToPNG()
    
    canvas.save('output.png')


    '''
    for i in range(100):
        camoImg = camoImageFactory.getCamoImage()
        camoImg.saveToPNG('./out/' + str(i) + '.png')
    '''
