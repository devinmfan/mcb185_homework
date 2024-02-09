#Co-Authors - Devin Fan, Sophia Chen11

import random

for seq in range(3):
	print(f">seq-{seq}")
	for j in range(50):
		print(random.choice('ACGT'), end='')
	print()