import random

inner = 0
i = 1

while True:
	x, y = random.random(), random.random()

	origin = x**2 + y**2

	if origin < 1:
		inner += 1

	pi_est = (inner / i) * 4

	print(f"Iteration: {i + 1}, Pi Estimate: {pi_est}")
	i += 1