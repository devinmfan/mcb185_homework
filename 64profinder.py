import sys
import dogma
import mcb185
import math

file = sys.argv[1]
length = int(sys.argv[2])

codon = []
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	#defwords = defline.split()
	for nt in seq:
		if nt == 'C' or nt == 'G' or nt == 'A' or nt == 'T': 
			codon.append(nt)
seq = ''.join(codon)
x = dogma.translate(seq)

for i in x:
	if i == "M":
		print("M")

for i in x:
	if i == "*":
		print("*")