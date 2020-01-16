# Shaun Leung
# Jan 15, 2020

from Vertex import Vertex
from Edge import Edge

class Model:
    def __init__(self, rad):
        self.rad=rad
        self.vertices=[]
        self.edges=[]
        self.z=1
        self.id=1
        self.selected=None
        
    def add_vertex(self,x,y):
        new_vertex= Vertex(x,y,self.z,self.id,self.rad)
        self.z=self.z+1
        self.id=self.id+1
        self.vertices.append(new_vertex)
    
    def update_Vertex(self,x,y):
        if not self.selected == None:
            self.selected.set_Vertex(x,y,self.z)
            self.z=self.z+1
    
    def vertex_Hit(self,x,y,width,height):
        for vertex in self.vertices:
            if vertex.clicked(x,y,width,height):
                return True
        return False

    def select_Vertex(self,x,y,width,height):
        z=-1
        for vertex in self.vertices:
            if vertex.clicked(x,y,width,height) and vertex.z > z:
                self.selected = vertex
                z=vertex.z

    def is_Vertex_Selected(self):
        if self.selected == None:
            return False
        else: 
            return True