# Shaun Leung
# Jan 15, 2020

import tkinter as tk

class View:
    def __init__(self,model, width, height):
        self.model = model
        self.width = width
        self.height = height
        self.window = tk.Tk()
        self.canvas = tk.Canvas(self.window,height=height, width=width)
        self.canvas.pack()

    def start_View(self):
        self.window.title("Graph")
        self.window.mainloop()
        return

    def update_View(self):
        self.canvas.delete('all')
        self.update_Vertices()
        return

    def update_Vertices(self):
        for vertex in self.model.vertices:
            x1=(vertex.x * self.width) - vertex.rad
            y1=(vertex.y * self.height) - vertex.rad
            x2=(vertex.x * self.width) + vertex.rad
            y2=(vertex.y * self.height) + vertex.rad

            new_Label = tk.Label(self.window,text=vertex.id)
            self.canvas.create_window(x1,y1,window=new_Label)

            self.canvas.create_oval(x1,y1,x2,y2)
            
        self.canvas.pack()
        return


