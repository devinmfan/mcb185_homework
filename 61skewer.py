import dogma
import sys
import mcb185

file = sys.argv[1]
w = int(sys.argv[2])

codon = []
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	#defwords = defline.split()
	for nt in seq:
		if nt in 'CGAT': 
			codon.append(nt)
seq = ''.join(codon)

for i in range(len(seq) -w +1):
	s = seq[i:i+w]
	#print(i, dogma.gc_comp(s), dogma.gc_skew(s))
	print(f'{i}\t{dogma.gc_comp(s):.3f}\t{dogma.gc_skew(s):.3f}')
