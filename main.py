from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

arm_texture = load_texture('textures/arm_texture.png')

block_color = 3

def update():

	global block_color  

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
		block_color = 3
		print(block_color)
	if held_keys['4']: 
		block_color = 4
		print(block_color)

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

class Hand(Entity):
	def __init__(self):
		super().__init__(
			parent = camera.ui,
			model='textures/arm',
			texture=arm_texture,
			scale = 0.2,
			rotation=Vec3(150,-10,0),
			position=Vec2(0.6,-0.6)
			)
	def active(self):
		self.position = Vec2(0.4,-0.5)
	def passive(self):
		self.position = Vec2(0.6,-0.6) 

app = Ursina()

for z in range(16):
	for x in range(16):
		voxel = Voxel(position=(x,0,z))

player = FirstPersonController()
hand = Hand()

app.run()