from ursina import*

from .command_pattern.Commands import*
from .command_pattern.Weapons import*
from .command_pattern.Switch import*

arm_texture = load_texture('textures/arm_texture.png')
heart_texture = load_texture('textures/heart.png')

class Oka(Entity):
	def __init__(self):
		super().__init__(
				model='textures/oka',
				texture='white_cube',
				color=color.red,
				scale=1,
				position=Vec3(10,1,10),
				rotation=Vec3(-90,0,0)
			)

class Hammer(Entity):
	def __init__(self):
		super().__init__(
				model='textures/HammerFinal',
				texture='white_cube',
				color=color.green,
				scale=2,
				position=Vec3(0,10,10)
			)

class Sword(Entity):
	def __init__(self):
			super().__init__(
				model='textures/HammerFinal',
				texture='white_cube',
				color=color.dark_gray,
				scale=0.15,
				position=Vec2(0.5,-0.5)
				)
	def active(self):
		pass
	def passive(self):
		pass

class Weapon(Entity):
        def __init__(self):
        	super().__init__(
			parent = camera.ui,
			
			)

        def active(self):
        	mp4=Mp4()
        	mp4_shot=Shot(mp4)
        	switch=Switch()
        	switch.register('shot_mp4',mp4_shot)
        	switch.execute('shot_mp4')


        def passive(self):
        	pass
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

class Menu(Entity):
	def __init__(self):
		super().__init__(
			parent=camera.ui,
			model='quad',
			texture=heart_texture,
			position=Vec2(-0.7,0.4),
			scale=0.1
			)

class Inventory(Entity):
    def __init__(self):
        super().__init__(
            parent = camera.ui,                                         
            model = 'quad',
            scale = (.35, .4),                                           
            position = Vec2(.6,.2),                                        
            texture = 'white_cube',                                     
            texture_scale = (5,5),                                      
            color = color.dark_gray                                             
            )
