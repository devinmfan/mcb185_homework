#Co-Authors - Devin Fan, Sophia Chen

pi = 3
const = 4
x = 2
y = 3
z = 4
 
for i in range(0, 1000000):
	pi = pi + (const / (x * y * z))
	x = x + 2
	y = y + 2
	z = z + 2
	const = const * -1
print('The estimate of pi using the Nilakantha series is:', pi)