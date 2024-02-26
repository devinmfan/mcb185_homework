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


nts = []

for defline, seq in mcb185.read_fasta(sys.argv[1]):
	defwords = defline.split()
	name = defwords[0]
	
	defline_stuff = f">{name} {defline[len(name):]}"

	
	for nt in seq:
		nts.append(nt)
seq = ''.join(nts)

result_nts = []

for i in range(0, len(seq), window):
	chunk = seq[i:i+window]
	
	count_a = chunk.count('A')
	count_t = chunk.count('T')
	count_g = chunk.count('G')
	count_c = chunk.count('C')
	
	#print(chunk)
	
	h = entropy(count_a, count_c, count_t, count_g)
	
	for j in chunk:
		if h < e:
			chunk = chunk.replace(j, "N")

		
	result_nts.append(chunk)

complete_genome = ''.join(result_nts)
print(defline_stuff)
print(complete_genome)
