#! python3
# user_input.py - 

from .game_actions import actionsDict

class UserInput():
	import re
	reg = re.compile(r"(\w+)\s*((\w*)\s*(\w*)\s*\w*)")

	def __init__(self):
		self.matches = self.reg.match(input("> ").lower())
		try:
			self.word1 = self.matches.group(1)
			self.word2 = self.matches.group(2)
			self.word3 = self.matches.group(3)
			self.word4 = self.matches.group(4)
			self.isValid = False
		except:
			self.word1 = False
			self.isValid = False

		if self.word1 in actionsDict:
			self.isValid = True

	def hasSecondInput(self):
		if len(self.word2) == 0:
			return False
		return True
	
	def setSecondInput(self, string, override=False):
		if len(self.word2) == 0:
			self.word2 = string
			return True
		else:
			if override:
				self.word2 = string
				return True
			else:
				return False
	
	def secondInput(self):
		if len(self.word2) == 0:
			return "No second input"
		return self.word2