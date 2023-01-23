from interp import Interpreter
import sys

if __name__ == "__main__":
	file = sys.argv[1]
	with open(file, "r") as f:
		i = Interpreter()
		i.run(f.read())
