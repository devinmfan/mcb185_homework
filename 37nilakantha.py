def nilakantha(i):
	result = 3
	sign = 1
	
	for i in range(1, i + 1):
		den = 2 * i * (2 * i + 1) * (2 * i + 2)
		term = 4 / den
		result = result + sign * term
		sign = sign * -1 

	return result

i = 1
est = nilakantha(1)
print(f"Estimated Pi after 1 iterations:" ,est)

i = 10
est = nilakantha(10)
print(f"Estimated Pi after 10 iterations:" ,est)

i = 100
est = nilakantha(100)
print(f"Estimated Pi after 100 iterations:" ,est)