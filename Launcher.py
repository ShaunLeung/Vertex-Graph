# Shaun Leung
# Jan 15, 2020

from Model import Model
from View import View
from Controller import Controller

height = 1000
width = 1000
rad = 25

model = Model(rad)
root = View(model,width,height)
controller = Controller(model,root)

root.start_View()