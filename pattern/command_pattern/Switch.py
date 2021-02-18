from .Commands import *
from .Weapons import *
import time

class Switch:
	def __init__(self):
		self._commands = {}
		self._history = []

	@property
	def history(self):
	    return self._history

	def register(self,command_name,command):
		self._commands[command_name] = command

	def execute(self,command_name):
		if command_name in self._commands.keys():
			self._history.append((time.time(),command_name))
			self._commands[command_name].execute()
		else:
			print(f"Command [{command_name}] not recognised")

