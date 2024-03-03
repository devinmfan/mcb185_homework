import dogma
import sys
import mcb185

seq = sys.argv[1]
w = int(sys.argv[2])

nts = []
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	defwords = defline.split()
	name = defwords[0]
	for nt in seq:
		nts.append(nt)

seq = ''.join(nts)

g = seq[0:w].count('G')
c = seq[0:w].count('C')

for i in range(len(seq) - w):
	off = seq[i]
	on = seq[i+w]
	
	if off == 'C': c -= 1
	elif off == 'G': g -= 1
	
	if on == 'C': c += 1
	elif on == 'G': g += 1
	
	gc = (c+g) / w
	
	if (g+c) > 0: 
		skew = (g-c) / (g+c)
	else: 
		skew = 0
	
	print(i, gc, skew)

