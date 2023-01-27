from token import * 

"""
Problem:
entah kenapa ya, variable t nya malah dibelakang , seharusnya didepan asu.
"""

class Lexer:
	def __init__(self, c):
		self.c = c
		self.cc = None # Current character buffer
		self.cp = -1 # Character position
		self.pbuff = "" # Previous character buffer
		self.advbuff = "" # Advanced character buffer
		self.instr = 0 # In string, 1 for true 0 for false
		self.tk = [] # Tokens, this is very important.
		self.isRunning = False
		self.c = " ".join([self.c, " "]) # i added this, because the more i add space, the less it does the bug

	def _adv(self):
		self.cp += 1
		if self.cp >= len(self.c):
			self.isRunning = False
			return None
		else:
			self.cc = self.c[self.cp]

	def _add(self, t, p=""):
		self.tk.append(Token(t, p))

	def Lex(self):
		self._adv()
		self.isRunning = True
		while self.isRunning:
			print(self.tk)
			print(self.cc)
			print(self.instr)
			if self.cc in DCHARS:
				if self.instr:
					self.advbuff += self.cc
					self._adv()
				else:
					self.pbuff += self.cc
					self._adv()

			elif self.cc in DSOP:
				if self.instr == 0:
					self.instr = 1
					self._adv()
				elif self.instr == 1:
					self._add(STR, self.advbuff)
					self.advbuff = ""
					self.instr = 0
					self._adv()

			elif self.cc not in DCHARS:
				if self.instr == 1:
					self.advbuff += self.cc
					self._adv()
				else:
					if self.pbuff == "" and self.cp != 0: self._adv()
					else:
						self._add(CHAR, self.pbuff)
						self.pbuff = ""

					if self.cc in DNUM:
						self._adv()

					elif self.cc in DOP:
						self._add(OP, self.cc)
						self._adv()
					
					elif self.cc in DNEW:
						self._adv()
					elif self.cc in DWSP:
						self._adv()
					elif self.cc in DNEW:
						self._adv()
			