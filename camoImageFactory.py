from imageArray import *
from dissolver import *

class CamoImageFactory(object):
    
    def __init__(self):
        pass
        

    def getCamoImage(self):
        camoImage = ImageArray()
        dissolve(camoImage)
        
        color = random.randint(0, 3)
        camoImage.setColor(60*color)

        return camoImage
