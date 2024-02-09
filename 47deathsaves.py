#Co-Authors - Devin Fan, Sophia Chen

import random

fail = 0
rev = 0
stab = 0

for i in range(10000):
	failures = 0
	successes = 0
	revives = 0
	while failures < 3 and successes < 3 and revives < 1:
		roll = random.randint(1, 20)

		if roll == 1:
			failures += 2
		elif roll < 10:
			failures += 1
		elif roll == 20:
			revives += 1
		elif roll >= 10: 
			successes += 1
	
	if successes == 3:
		stab = stab + 1
	elif failures >= 3:
		fail = fail + 1
	elif revives == 1:
		rev = rev + 1

stab = stab / 10000
fail = fail / 10000
rev = rev / 10000

print("Probabilty of being revived:", rev)
print("Probabilty of being stabailized:", stab)
print("Probablity of dying:", fail)
