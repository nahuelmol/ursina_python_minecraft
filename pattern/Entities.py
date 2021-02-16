from ursina import*

arm_texture = load_texture('textures/arm_texture.png')
heart_texture = load_texture('textures/heart.png')

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