from lexer import Lexer as L

class Interpreter:
	def __init__(self):
		self.c = None
		pass

	def run(self, c):
		self.c = c
		self.l = L(self.c)
		self.l.Lex()