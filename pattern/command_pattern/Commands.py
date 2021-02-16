from abc import ABCMeta, abstractstaticmethod

class Command(metaclass=ABCMeta):

	@abstractstaticmethod
	def execute():
		"""Hola"""


class Shot(Command):
	def __init__(self,weapon):
		self._weapon = weapon
		self._count = 0
	def execute(self):

		if(self._count == self._weapon._charger_cap):
			self._weapon.recharge()
			self._count == 0

		print("Shooting with {}".format(self._weapon._name))
		
		self._weapon.flaming()
		self._weapon.explosive_sound()
		self._weapon.forces_rebote()
		self._weapon.velocity_at_walking()

		self._count = self._count + 1


class Throw(Command):
	def __init__(self,weapon):
		self._weapon = weapon

	def execute(self):
		print("Thowing the {}".format(self._weapon._name))

		self._weapon.sound_falling()	
