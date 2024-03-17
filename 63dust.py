import sys
import dogma
import mcb185
import math

file = sys.argv[1]
window = int(sys.argv[2])
e = float(sys.argv[3])

for defline, seq in mcb185.read_fasta(file):
	defwords = defline.split()
	name = defwords[0]
	defline_stuff = f">{name} {defline[len(name):]}"
	
	result_nts = []
	for i in range(0, len(seq), window):
		chunk = seq[i:i+window]
		count_a = chunk.count('A')
		count_t = chunk.count('T')
		count_g = chunk.count('G')
		count_c = chunk.count('C')
		
		h = dogma.entropy(count_a, count_c, count_t, count_g)
		
		for j in chunk:
			if h < e:
				chunk = chunk.replace(j, "N")
        
		result_nts.append(chunk)

	complete_genome = ''.join(result_nts)
	print(defline_stuff)
	print(complete_genome)
