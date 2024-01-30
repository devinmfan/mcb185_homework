#Co-Authors - Devin Fan, Sophia Chen
def oligotemp (A,C,G,T):
	nt = A + C + G + T
	if nt <= 13:
		Tm = (A + T) * 2 + (G + C) * 4
	else:
		Tm = 64.9 + 41 * (G + C - 16.4) / (A + T + G + C)
		
	return Tm

print(oligotemp(2, 6, 9, 15))

print(oligotemp(100, 100, 100, 100))

print(oligotemp(2, 4, 4, 3))

print(oligotemp(2, 4, 4, 4))