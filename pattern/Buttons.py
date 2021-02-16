from ursina import*
from .Entities import Hand, Weapon

hand = Hand()
block_color = 2

def update():

	global block_color  
        global hand

	if held_keys['left mouse'] or held_keys['right mouse']:
		hand.active()
	else:
		hand.passive()

	if held_keys['1']: 
		block_color = 1
		print(block_color)
	if held_keys['2']: 
		block_color = 2
		print(block_color)
	if held_keys['3']: 
		hand = Weapon()
	if held_keys['4']: 
		hand = Sword()

class Voxel(Button):
	def __init__(self,position=(0,0,0),mycolor=color.white):


		super().__init__(
			parent = scene,
			position=position,
			model='cube',
			origin_y=0.5,
			texture='white_cube',
			color=mycolor,
			#highlight_color=color.lime,
			scale=1
			)
	def input(self,key):
		if self.hovered:
			
			if key == 'left mouse down':
			    if block_color == 1: 
			    	voxel = Voxel(position=self.position + mouse.normal,mycolor=color.red)
			    if block_color == 2: 
			    	voxel = Voxel(position=self.position + mouse.normal,mycolor=color.green)
			    if block_color == 3: 
			    	voxel = Voxel(position=self.position + mouse.normal,mycolor=color.orange)
			    if block_color == 4: 
			    	voxel = Voxel(position=self.position + mouse.normal,mycolor=color.lime)
			if key == 'right mouse down':
				destroy(self)
