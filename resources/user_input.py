#! python3
# user_input.py - 

from .game_actions import actionsDict

class UserInput():
  import re
  reg = re.compile(r"(\w+)\s*(\w*)\s*(\w*)")

  def __init__(self):
    self.matches = self.reg.match(input("> ").lower())
    try:
      self.word1 = self.matches.group(1)
      self.word2 = self.matches.group(2)
      self.word3 = self.matches.group(3)
      self.isValid = False
    except:
      self.word1 = False
      self.isValid = False

    if self.word1 in actionsDict:
      self.isValid = True

  def getInput(self):
    self.matches = self.reg.match(input("> ").lower())

  def asssignCmds(self, match):
    self.word1 = self.matches.group(1)
    self.word2 = self.matches.group(2)
    self.word3 = self.matches.group(3)