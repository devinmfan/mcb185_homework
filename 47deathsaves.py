#Co-Authors - Devin Fan, Sophia Chen

import random

fail = 0
suc = 0
stab = 0

for i in range(10000):
	failures = 0
	successes = 0
	health = 0
	while failures < 3 and successes < 3:
		roll = random.randint(1, 20)

		if roll == 1:
			failures += 2
		elif roll < 10:
			failures += 1
		elif roll >= 10 and roll < 20:
			successes += 1
		else:
			health += 1
	
	if successes == 3:
		suc = suc + 1
	elif failures == 3:
		fail = fail + 1
	else:
		stab = stab + 1

suc = suc / 10000
fail = fail / 10000
stab = stab / 10000

print("Probabilty of being revived:", suc)
print("Probabilty of being stabailized:", stab)
print("Probablity of dying:", fail)