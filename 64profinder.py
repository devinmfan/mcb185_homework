import sys
import dogma
import mcb185

file = sys.argv[1]
min_length = int(sys.argv[2])

proteins = []
prot_index = 0

for defline, seq in mcb185.read_fasta(file):
	codon = []
	for nt in seq:
		codon.append(nt)
		
	seq = ''.join(codon)
	rev = dogma.revcomp(seq)
	translated_seq = dogma.translate(rev)
	
	protein_segments = []
	current_segment = []
	for aa in translated_seq:
		if aa == "M":
			if current_segment:
				protein_segments.append(''.join(current_segment))
				current_segment = []
			current_segment.append(aa)
		elif aa == "*":
			if current_segment:
				protein_segments.append(''.join(current_segment))
				current_segment = []
		else:
			current_segment.append(aa)
			
	for protein_segment in protein_segments:
		if len(protein_segment) >= min_length:
			prot_index += 1
			prot_defline = f">NC_000913.3-prot-{prot_index}"
			proteins.append((prot_defline, protein_segment))
			
for defline, protein in proteins:
	print(defline)
	print(protein)