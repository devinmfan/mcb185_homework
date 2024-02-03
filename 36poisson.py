#Co-Authors - Devin Fan, Sophia Chen

import math

def poisson(n, k):
	
	if k == 0: return 1
	fack = 1
	for i in range(1, k + 1):
		fack = fack * i
	
	x = n * (n**k * math.exp(-n)) / fack
	return x

print(poisson(6, 9))
print(poisson(420, 69))
print(poisson(8, 16))