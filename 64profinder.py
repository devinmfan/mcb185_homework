import sys
import dogma
import mcb185

file = sys.argv[1]
min_length = int(sys.argv[2])

codon = []
protein_sequence = []

for defline, seq in mcb185.read_fasta(sys.argv[1]):
	defwords = defline.split()
	name = defline[0]  
	for nt in seq:
		codon.append(nt)

seq = ''.join(codon)
rev = dogma.revcomp(seq)
x = dogma.translate(rev)

pro = []
deflines = []

for i in range(len(x)):
	if x[i] == "M":
		protein_segment = [x[i]]
		for j in range(i + 1, len(x)):
			if x[j] == "*":
				break
			protein_segment.append(x[j])
		pro.append(''.join(protein_segment))
		deflines.append(defline)

for defline, protein in zip(deflines, pro):
	if len(protein) >= min_length:
		print(defline)
		print(protein)
