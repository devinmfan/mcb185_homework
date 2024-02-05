import random

for seq in range(3):
	print("seq-", seq+1)
	for j in range(50):
		print(random.choice('ACGT'), end='')
	print("\n")