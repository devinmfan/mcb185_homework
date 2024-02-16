import random
import sys

if len(sys.argv) != 4:
	print("Usage: python3 57birthday.py <trials> <days> <people>")
	sys.exit(1)

trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])

