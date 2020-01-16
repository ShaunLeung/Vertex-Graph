# Shaun Leung
# Jan 15, 2020

from Model import Model
from View import View

class Controller:
    
    def move(self,event):
        if self.model.is_Vertex_Selected():
            x=event.x
            y=event.y

            self.model.update_Vertex(x/self.view.width,y/self.view.height)
            
            #update the canvas
            self.view.update_View()
        
    def release(self,event):
        if self.model.is_Vertex_Selected():  
            self.model.selected=None
        return

    def click(self, event):

        if(event.widget.winfo_class() == 'Label'):
            x=event.widget.winfo_x()
            y=event.widget.winfo_y()
        else:
            x=event.x
            y=event.y

        if (self.model.vertex_Hit(x,y,self.view.width,self.view.height)):
            # Vertex has been selected in the model
            self.model.select_Vertex(x,y,self.view.width,self.view.height)
            
               
        else:
            #Create a vertex if background clicked
            self.model.add_vertex(x/self.view.width,y/self.view.height)
            

            #update the canvas
            self.view.update_View()
        
        return

    def __init__(self,model, view):
        self.model = model
        self.view = view
        self.view.window.bind('<Button-1>', self.click)
        self.view.window.bind('<B1-Motion>', self.move)
        self.view.canvas.bind('<B1-Motion>', self.move)
        self.view.window.bind('<ButtonRelease-1>', self.release)



    

