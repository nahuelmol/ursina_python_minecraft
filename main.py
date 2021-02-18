from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

from pattern.Buttons import*   
from pattern.Entities import Menu, Inventory, Hammer, Oka

for z in range(15):
	for x in range(15):
		voxel = Voxel(position=(x,0,z))

player = FirstPersonController()

menu = Menu()
inventory = Inventory()
hammer=Hammer()
oka = Oka()

app.run()