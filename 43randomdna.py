#Co-Authors - Devin Fan, Sophia Chen11

import random

for seq in range(3):
	print(f">seq-{seq}")
	for j in range(random.randint(50,60)):
		print(random.choice('ACGT'), end='')
	print()