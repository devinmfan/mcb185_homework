def transcribe(dna):
	return dna.replace('T', 'U')
	
def revcomp(dna):
	rc = []
	for nt in dna[::-1]:
		if   nt == 'A': rc.append('T')
		elif nt == 'C': rc.append('G')
		elif nt == 'G': rc.append('C')
		elif nt == 'T': rc.append('A')
		else:           rc.append('N')
	return ''.join(rc)
	
def translate(dna):
	aas = []
	for i in range(0, len(dna), 3):
		codon = dna[i:i+3]

		if codon == 'TTT' or codon == 'TTC':
			aa = 'F'
		elif codon == 'TTA' or codon == 'TTG' or codon == 'CTT' or codon == 'CTC' or codon == 'CTA' or codon == 'CTG':
			aa = 'L'
		elif codon == 'ATT' or codon == 'ATC' or codon == 'ATA':
			aa = 'I'
		elif codon == 'ATG':
			aa = 'M'
		elif codon == 'GTT' or codon == 'GTC' or codon == 'GTA' or codon == 'GTG':
			aa = 'V'
		elif codon == 'TCT' or codon == 'TCC' or codon == 'TCA' or codon == 'TCG':
			aa = 'S'
		elif codon == 'CCT' or codon == 'CCC' or codon == 'CCA' or codon == 'CCG':
			aa = 'P'
		elif codon == 'ACT' or codon == 'ACC' or codon == 'ACA' or codon == 'ACG':
			aa = 'T'
		elif codon == 'GCT' or codon == 'GCC' or codon == 'GCA' or codon == 'GCG':
			aa = 'A'
		elif codon == 'TAT' or codon == 'TAC':
			aa = 'Y'
		elif codon == 'TAA' or codon == 'TAG' or codon == 'TGA':
			aa = '*'
		elif codon == 'CAT' or codon == 'CAC':
			aa = 'H'
		elif codon == 'CAA' or codon == 'CAG':
			aa = 'Q'
		elif codon == 'AAT' or codon == 'AAC':
			aa = 'N'
		elif codon == 'AAA' or codon == 'AAG':
			aa = 'K'
		elif codon == 'GAT' or codon == 'GAC':
			aa = 'D'
		elif codon == 'GAA' or codon == 'GAG':
			aa = 'E'
		elif codon == 'TGT' or codon == 'TGC':
			aa = 'C'
		elif codon == 'TGG':
			aa = 'W'
		elif codon == 'CGT' or codon == 'CGC' or codon == 'CGA' or codon == 'CGG':
			aa = 'R'
		elif codon == 'AGT' or codon == 'AGC':
			aa = 'S'
		elif codon == 'AGA' or codon == 'AGG':
			aa = 'R'
		elif codon == 'GGT' or codon == 'GGC' or codon == 'GGA' or codon == 'GGG':
			aa = 'G'
		else:
			aa = 'X'

		aas.append(aa)

	return ''.join(aas)

	
def gc_comp(seq):
	return (seq.count('C') + seq.count('G')) / len(seq)
	
def gc_skew(seq):
	c = seq.count('C')
	g = seq.count('G')
	if c + g == 0: return 0
	return (g - c) / (g + c)
	
import math

def entropy(a, c, t, g):
	total = a + c + t + g
	prob_a = a / total
	prob_c = c / total
	prob_t = t / total
	prob_g = g / total
	
	if a == 0:
		info_c = math.log2(prob_c)
		info_t = math.log2(prob_t)
		info_g = math.log2(prob_g)
		h = -(prob_c * info_c + prob_t * info_t + prob_g * info_g)
	elif c == 0:
		info_a = math.log2(prob_a)
		info_t = math.log2(prob_t)
		info_g = math.log2(prob_g)
		h = -(prob_a * info_a + prob_t * info_t + prob_g * info_g)
	elif t == 0:
		info_a = math.log2(prob_a)
		info_c = math.log2(prob_c)
		info_g = math.log2(prob_g)
		h = -(prob_a * info_a + prob_c * info_c + prob_g * info_g)
	elif g == 0: 
		info_a = math.log2(prob_a)
		info_c = math.log2(prob_c)
		info_t = math.log2(prob_t)
		h = -(prob_a * info_a + prob_c * info_c + prob_t * info_t)
	else:
		info_a = math.log2(prob_a)
		info_c = math.log2(prob_c)
		info_t = math.log2(prob_t)
		info_g = math.log2(prob_g)
		h = -(prob_a * info_a + prob_c * info_c + prob_t * info_t + prob_g * info_g)
	print('Shannon entropy is:', round(h, 4))
	return h