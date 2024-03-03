import sys
import mcb185
import itertools

def count_kmers(seq, k):
	kcount = {}
	for i in range(len(seq) - k + 1):
		kmer = seq[i:i+k]
		if kmer not in kcount:
			kcount[kmer] = 0
		kcount[kmer] += 1
	return kcount

def print_kmers(kcount):
	for kmer, n in kcount.items():
		print(kmer, n)

file = sys.argv[1]
k_i = int(sys.argv[2])

for defline, seq in mcb185.read_fasta(file):
	k = k_i
	kcount = count_kmers(seq, k)

	for kmer, n in kcount.items():
		print(kmer, n)

	for nts in itertools.product('ACGT', repeat=k):
		kmer = ''.join(nts)
		if kmer not in kcount:
			print(kmer, 0)
	k += 1
