import dogma
import sys
import mcb185

seq = sys.argv[1]
window = int(sys.argv[2])

codon = []
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	for nt in seq:
		if nt in 'CGAT': 
			codon.append(nt)
seq = ''.join(codon)

for i in range(0, len(seq), window):
	s = seq[i:i+window]
	print(f'{i}\t{dogma.gc_comp(s):.3f}\t{dogma.gc_skew(s):.3f}')

