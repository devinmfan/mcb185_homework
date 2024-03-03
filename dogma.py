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

	
	
def hydropathy(aa):
	if aa == 'A':
		return 1.8
	elif aa == 'R':
		return -4.5
	elif aa == 'N':
		return -3.5
	elif aa == 'D':
		return -3.5
	elif aa == 'C':
		return 2.5
	elif aa == 'Q':
		return -3.5
	elif aa == 'E':
		return -3.5
	elif aa == 'G':
		return -0.4
	elif aa == 'H':
		return -3.2
	elif aa == 'I':
		return 4.5
	elif aa == 'L':
		return 3.8
	elif aa == 'K':
		return -3.9
	elif aa == 'M':
		return 1.9
	elif aa == 'F':
		return 2.8
	elif aa == 'P':
		return -1.6
	elif aa == 'S':
		return -0.8
	elif aa == 'T':
		return -0.7
	elif aa == 'W':
		return -0.9
	elif aa == 'Y':
		return -1.3
	elif aa == 'V':
		return 4.2
	else:
		return 0

def gc_comp(seq):
	return (seq.count('C') + seq.count('G')) / len(seq)
	
def gc_skew(seq):
	c = seq.count('C')
	g = seq.count('G')
	if c + g == 0: return 0
	return (g - c) / (g + c)
	
def entropy(a, c, t, g):
	total = a + c + t + g

	if total == 0:
		return 0

	prob_a = a / total
	prob_c = c / total
	prob_t = t / total
	prob_g = g / total
	
	h = 0
	
	if prob_a != 0:
		h -= prob_a * math.log2(prob_a)
		
	if prob_c != 0:
		h -= prob_c * math.log2(prob_c)

	if prob_t != 0:
		h -= prob_t * math.log2(prob_t)

	if prob_g != 0:
		h -= prob_g * math.log2(prob_g)

	return h