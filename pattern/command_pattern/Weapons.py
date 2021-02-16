
class Weapon:
	def flaming(self):
		print('flaming')
	def explosive_sound(self):
		print('doing an explosive sound')
	def forces_rebote(self):
		print('rebote')
	
	def aiming(self):
		print('aiming')

	def recharge(self):
		print('recharging')

	def sound_falling(self):
		print('sound falling in the floor')


class Mp4(Weapon):

	def __init__(self):

		self._name = 'Mp4'
		self._charger_cap = 3
		self._weight = 1000

	def velocity_at_walking(self):
		print('movement media velocity')

class Magnum(Weapon):
	def __init__(self):
		self._name = 'Magnum'
	def velocity_at_walking(self):
		print('movement slow velocity')

class Pistol(Weapon):
	def __init__(self):
		self._name = 'Pistol'
	def velocity_at_walking(self):
		print('movement fast')