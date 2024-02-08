import random

#normal

def saving_sim(dc):
	suc = 0
	for i in range(1, 10000):
		result = random.randint(1, 20)	
		
		if result >= dc:
			suc = suc + 1
	prob = suc / 10000
	return prob

#advantage

result = 0
def ad(dc):
	suc = 0
	for i in range(1, 10000):
		roll1 = random.randint(1, 20)
		roll2 = random.randint(1, 20)
		if roll1 > roll2: 
			result = roll1 
		else: 
			result = roll2
		#print(result)	

		if result >= dc:
			suc = suc + 1
	prob = suc / 10000
	return prob



#disadvatage

result = 0
def disad(dc):
	suc = 0
	for i in range(1, 10000):
		roll1 = random.randint(1, 20)
		roll2 = random.randint(1, 20)
		if roll1 < roll2:
			result = roll1 
		else:
			result = roll2

		if result >= dc:
			suc = suc + 1
	prob = suc / 10000
	return prob

	
saving_sim(5)
disad(5)
ad(5)

saving_sim(10)
disad(10)
ad(10)
	
saving_sim(15)	
disad(15)
ad(15)

dc = 5, 10, 15

print(f"| DC | Normal | Advantage | Disadvantage |")
print(f"|----|--------|-----------|--------------|")
for i in dc:
	print(f"| {i} | {saving_sim(i):.4f} | {ad(i):.4f} | {disad(i):.4f} |")