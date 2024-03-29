#Co-Authors - Devin Fan, Sophia Chen

def nchoosek(n, k):
	if n == 0: return 1
	facn = 1
	for i in range(1, n + 1):
		facn = facn * i
		
	if k == 0: return 1
	fack = 1
	for i in range(1, k + 1):
		fack = fack * i
		
	z = n - k
	if z == 0: return 1
	facnk = 1
	for i in range(1, z + 1):
		facnk = facnk * i
		
	x = facn / (fack * (facnk))
	return x

print(nchoosek(10, 6))
print(nchoosek(1, 1))
print(nchoosek(42, 11))