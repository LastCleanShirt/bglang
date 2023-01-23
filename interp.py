class Interpreter:
	def __init__(self):
		self.c = None
		pass

	def run(self, c):
		self.c = c
		print(self.c)