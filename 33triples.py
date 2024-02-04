#Co-Authors - Devin Fan, Sophia Chen

import math

limit = 100

for s1 in range(1, limit):
	for s2 in range(s1 + 1, limit):
		hypotenuse = math.sqrt(s1**2 + s2**2)
		if hypotenuse == hypotenuse // 1:
			print(s1, s2, hypotenuse)