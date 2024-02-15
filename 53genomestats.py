import gzip
import sys
import math

if len(sys.argv) != 3:
	print("Usage: python3 script.py <gff_path> <feature_type>")
	sys.exit(1)

gffpath = sys.argv[1]
feature = sys.argv[2]

def calc_std_dev(data):
	squared_diff = 0
	for x in data:
		squared_diff += (x - mean) ** 2
	variance = squared_diff / len(data)
	std_dev = math.sqrt(variance)
	return std_dev

print(f"| Genome         | Type |  N   | Min |  Max  | Mean | Stdv | Med  |")
print(f"|:---------------|:-----|:-----|:----|:------|:-----|:-----|:-----|")

lengths = []
with gzip.open(gffpath, 'rt') as fp:
	for line in fp:
		if line[0] != '#':
			words = line.split()
			if words[2] == feature:
				beg = int(words[3])
				end = int(words[4])
				lengths.append(end - beg + 1)

n = len(lengths)
mini = min(lengths)
maxi = max(lengths)
mean = sum(lengths) / n
std_dev = calc_std_dev(lengths)
lengths.sort()

if len(lengths) % 2 == 0:
	mid1 = lengths[(int(n) // 2) - 1]
	mid2 = lengths[int(n) // 2]
	med = (mid1 + mid2) / 2

else:
	med = lengths[int(n)//2]

print(f"| {gffpath} | {feature} | {n} | {mini} | {maxi} | {mean:.2f} | {std_dev:.2f} | {med:.2f} |")
