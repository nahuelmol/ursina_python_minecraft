from abc import ABCMeta, abstractstaticmethod

class Command(metaclass=ABCMeta):
	@abstractstaticmethod
	def execute():



class Shot(Command):
	def __init__(self,weapon):
		self._weapon = weapon
	def execute(self):
		self._weapon.flaming()
		self._weapon.explosive_sound()
		self._forces_rebote()

		if walking == 'on':
			self._weapon.movement_at_walking()
		if packet = 'empty':
			self._weapon.recharge()



