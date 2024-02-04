#Co-Authors - Devin Fan, Sophia Chen

import math

def poisson(n, k):
	
	if k == 0: return 1
	fac = 1
	for i in range(1, k + 1):
		fac = fac * i
	
	x = n * (n**k * math.exp(-n)) / fac
	return x

print(poisson(6, 9))
print(poisson(25, 12))
print(poisson(8, 16))