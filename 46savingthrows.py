#Co-Authors - Devin Fan, Sophia Chen

import random

trials = 10000

#normal

def saving_sim(dc):
	suc = 0
	for i in range(1, trials):
		result = random.randint(1, 20)	
		
		if result >= dc:
			suc = suc + 1
	prob = suc / trials
	return prob

#advantage

result = 0
def ad(dc):
	suc = 0
	for i in range(1, trials):
		roll1 = random.randint(1, 20)
		roll2 = random.randint(1, 20)
		if roll1 > roll2: 
			result = roll1 
		else: 
			result = roll2
		#print(result)	

		if result >= dc:
			suc = suc + 1
	prob = suc / trials
	return prob



#disadvatage

result = 0
def disad(dc):
	suc = 0
	for i in range(1, trials):
		roll1 = random.randint(1, 20)
		roll2 = random.randint(1, 20)
		if roll1 < roll2:
			result = roll1 
		else:
			result = roll2

		if result >= dc:
			suc = suc + 1
	prob = suc / trials
	return prob


dc1 = 5
dc2 = 10
dc3 = 15

print("| DC | Normal | Advantage | Disadvantage |")
print("|----|--------|-----------|--------------|")
print(f"| {dc1} | {saving_sim(dc1):.4f} | {ad(dc1):.4f} | {disad(dc1):.4f} |")
print(f"| {dc2} | {saving_sim(dc2):.4f} | {ad(dc2):.4f} | {disad(dc2):.4f} |")
print(f"| {dc3} | {saving_sim(dc3):.4f} | {ad(dc3):.4f} | {disad(dc3):.4f} |")
