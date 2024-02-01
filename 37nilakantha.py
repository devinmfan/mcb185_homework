def nilakantha(i):
	result = 3
	sign = 1
	
	for i in range(1, i + 1):
		den = 2 * i * (2 * i + 1) * (2 * i + 2)
		term = 4 / den
		result = result + sign * term
		sign = sign * -1 

	return result

i = 100
est = nilakantha(i)
print(f"Estimated Pi after", i,  "iterations:" ,est)