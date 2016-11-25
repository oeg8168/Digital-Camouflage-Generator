import random
from imageArray import *
from dissolver import *

class CamoImageFactory:
    
    def __init__(self):
        self.colorStep = 60
        

    def getCamoImage(self):
        camoImage = ImageArray()
        dissolve(camoImage)
        
        color = self.colorStep * random.randint(0, 3)
        camoImage.setColor(color)

        return camoImage
