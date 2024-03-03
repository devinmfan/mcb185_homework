import sys
import mcb185
import dogma

seq = sys.argv[1]

def sig_pep(seq):
	w = 8
	s = 1
	for i in range(0, len(seq) -w +1, s):
		if i + w <= 30:
			sp = seq[i:i+w]
			print("Amino acid sequence:", sp)
			for aa in sp:
				hydro_score = dogma.hydropathy(aa)
			print("Hydropathy score:", hydro_score)
			if hydro_score >= 2.5 and 'P' not in sp:
				continue

def trans_reg(seq):
	w = 11
	s = 1
	for i in range(30, len(seq) -w +1, s) :
		tr = seq[i:i+w]
		print("Amino acid sequence:", tr)
		for aa in tr:
			hydro_score = dogma.hydropathy(aa)
		print("Hydropathy score:", hydro_score)
		if hydro_score >= 2.0 and 'P' not in tr:
			continue
codon = []

for defline, seq in mcb185.read_fasta(sys.argv[1]):
	defwords = defline.split(']')
	name = defline[0] 
	for nt in seq:
		codon.append(nt)
seq = ''.join(codon)
x = dogma.translate(seq)

print(trans_reg(x))
print(sig_pep(x))