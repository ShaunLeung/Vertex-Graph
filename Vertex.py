# Shaun Leung
# Jan 15, 2020
import math

class Vertex(object):
    def __init__(self,x,y,z,id,rad):
        self.x=x
        self.y=y
        self.z=z
        self.id=id
        self.rad=rad

    def set_Vertex(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z

    def clicked(self,x,y,width,height):
        sqX=math.pow((self.x*width) - x,2)
        sqY=math.pow((self.y*height) - y,2)
        return (math.sqrt(sqX+sqY) <= self.rad)