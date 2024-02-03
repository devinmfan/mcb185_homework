#Co-Authors - Devin Fan, Sophia Chen
alph = 'ACGT'

print(" ", end=' ')
for i in alph:
	print(" " + i, end=' ')
print()

for nt1 in alph:
	print(nt1, end=' ')
	for nt2 in alph:
		if nt1 == nt2:
			print('+1', end=' ')
		else:
			print('-1', end=' ')
	print()
