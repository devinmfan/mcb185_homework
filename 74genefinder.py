#Co-authors: Sophia Chen and Devin Fan

import sys
import mcb185

seq = sys.argv[1]
gene_min = int(sys.argv[2])
anti = mcb185.anti_seq(seq)

codon = []

for defline, seq in mcb185.read_fasta(sys.argv[1]):
	defwords = defline.split()
	name = defline[0]
	for nt in seq:
		codon.append(nt)

seq = ''.join(codon)
anti_seq = mcb185.anti_seq(seq)

stops_used = {}

for frame in range(3):
	fseq = seq[frame:]

	for i in range(0, len(seq) - 3 + 1, 3):
		start_codon = fseq[i:i + 3]

		if start_codon == 'ATG':
			for j in range(i, len(fseq) - 2, 3):
				stop_codon = fseq[j:j + 3]

				if stop_codon == 'TAA' or stop_codon == 'TAG' or stop_codon == 'TGA':
					stop = j
					if stop not in stops_used:
						gene_length = stop - i + 3  
						if gene_length >= gene_min:  
							print('gene:', i+1, j)
							print('Found in the normal sequence')
							stops_used[stop] = True
							break

for frame in range(3):
	anti_fseq = anti_seq[frame:]

	for i in range(0, len(anti_seq) - 3 + 1, 3):
		start_codon = anti_fseq[i:i + 3]

		if start_codon == 'ATG':
			for j in range(i, len(anti_fseq) - 2, 3):
				stop_codon = anti_fseq[j:j + 3]

				if stop_codon == 'TAA' or stop_codon == 'TAG' or stop_codon == 'TGA':
					stop = j
					if stop not in stops_used:
						gene_length = stop - i + 3  
						if gene_length >= gene_min:  
							print('gene:', i+1, j)
							print('Found in the anti-sequence')
							stops_used[stop] = True
							break
