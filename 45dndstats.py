import random

total_3d6 = 0  

for i in range(10000):
	for j in range(3):
		x = random.randint(1, 6)
		total_3d6 += x

print("3d6:", round(total_3d6 / 10000, 1))

total_3d6r1 = 0

for i in range(10000):
	for j in range(3):
		x = random.randint(2, 6)
		total_3d6r1 += x

print("3d6r1:", round(total_3d6r1 / 10000, 1))  

total_3d6x2 = 0

for i in range(10000):
	for j in range(3):
		x1 = random.randint(1, 6)
		x2 = random.randint(1, 6)
		if x2 > x1:
			total_3d6x2 += x2
		else:
			total_3d6x2 += x1
            
print("3d6x2:", round(total_3d6x2 / 10000, 1))

total_4D6d1 = 0

for i in range(10000):
	for j in range(4):
		y1 = random.randint(1, 6)
		y2 = random.randint(1, 6)
		y3 = random.randint(1, 6)
		y4 = random.randint(1, 6)
        
		min_y = y1
		if y2 < min_y:
			min_y = y2
		if y3 < min_y:
			min_y = y3
		if y4 < min_y:
			min_y = y4
            
	total_4D6d1 += y1 + y2 + y3 + y4 - min_y

print("4D6d1:", round(total_4D6d1 / 10000, 1))