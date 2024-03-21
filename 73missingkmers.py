#Co-authors: Sophia Chen and Devin Fan

import dogma
import itertools
import mcb185
import sys

k = 1 
kcount = {}
n = 0 
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	rc = dogma.revcomp(seq)
	while n < 1: #condition breaks when missing kmers are found
		for i in range(len(seq) -k + 1):
			kmer = seq[i:i+k]
			if kmer not in kcount: kcount[kmer] = 0
			kcount[kmer] += 1
	
		for i in range(len(rc) - k + 1):
			kmer = rc[i:i+k]
			if kmer not in kcount: kcount[kmer] = 0
			kcount[kmer] += 1
	
		for nts in itertools.product('ACGT', repeat=k):
			kmer = ''.join(nts)
			if kmer not in kcount: 
				print(kmer)
				n += 1
		k += 1
		kcount = {}