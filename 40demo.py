import random

#for i in range(50):
	#print(random.choice('ACGT'), end='')
#print()

#for i in range(50):
	#r = random.random()
	#if r < 0.7: print(random.choice('AT'), end='')
	#else:       print(random.choice('CG'), end='')
#print()

for i in range(3):
	print(random.randint(1, 6))
	
for i in range(5):
	print(random.gauss(0.0, 1.0))
	
print(10, 20, 30, 40, sep='\t')
print(100, 2000, 30000, 40000, sep='\t')

i = 1
pi = 3.14159
print('normal string {i} {pi}')
print(f'formatted string {i} {pi}')
print(f'tau {pi + pi}')

import sys
print('logging', file=sys.stderr)

random.seed(1)
print(random.random())
print(random.random())
random.seed(2)
print(random.random())
print(random.random())
random.seed(1)
print(random.random())
print(random.random())