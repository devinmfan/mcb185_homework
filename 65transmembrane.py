import gzip
import mcb185
import sys
import dogma

def sigpep_check(seq):
	sp = seq[:30]
	for i in range(len(sp) - 7):
		signal = sp[i:i+8]
		if 'P' in signal: continue
		hydro_score = dogma.hydropathy(signal)
		if hydro_score >= 2.5: 
			return True
	return False
	
def transreg_check(seq):
	tr = seq[30:]
	for i in range(len(tr) - 10):
		trans = tr[i:i+11]
		if 'P' in trans: continue
		hydro_score = dogma.hydropathy(trans)
		if hydro_score >= 2.0:
			return True
	return False

for defline, seq in mcb185.read_fasta(sys.argv[1]):
	sigpep_result = sigpep_check(seq)
	transreg_result = transreg_check(seq)
	if sigpep_result and transreg_result:
		print(defline)
