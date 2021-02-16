from Commands import *
from Weapons import *
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

if __name__ == "__main__":
	mp4 = Mp4()
	magnum = Magnum()

	mp4_shot = Shot(mp4)
	magnum_shot = Shot(magnum)
	mp4_let_out = Throw(mp4)
	magnum_let_out = Throw(mp4)

	switch = Switch()

	switch.register('shot_mp4',mp4_shot)

	switch.execute('shot_mp4')
	switch.execute('shot_mp4')
	switch.execute('shot_mp4')
	switch.execute('shot_mp4')
	switch.execute('shot_mp4')
	switch.execute('shot_mp4')
	switch.execute('shot_mp4')

