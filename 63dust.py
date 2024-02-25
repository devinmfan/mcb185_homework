import sys
import dogma
import mcb185
import math

file = sys.argv[1]
window = int(sys.argv[2])
e = float(sys.argv[3])

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


codon = []

for defline, seq in mcb185.read_fasta(sys.argv[1]):
	#defwords = defline.split()
	for nt in seq:
		if nt in 'CGAT': 
			codon.append(nt)
seq = ''.join(codon)

for i in range(0, len(seq), window):
	chunk = seq[i:i+window]
    
	count_a = chunk.count('A')
	count_c = chunk.count('C')
	count_t = chunk.count('T')
	count_g = chunk.count('G')

	h = entropy(count_a, count_c, count_t, count_g)

	if h < e:
		seq = seq[:i] + 'N' * len(chunk) + seq[i+window:]
		print(seq)
