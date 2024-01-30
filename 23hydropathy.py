#23hydropathy.py by Sophia Chen & Devin Fan

import sys

def kyte(aa):
	if aa == 'A':
		hydro_value = 1.80
	elif aa == 'C':
		hydro_value = 2.50
	elif aa == 'D' or aa == 'E' or aa == 'N' or aa == 'Q':
		hydro_value = -3.50
	elif aa == 'F':
		hydro_value = 2.80
	elif aa == 'G':
		hydro_value = -0.40
	elif aa == 'H':
		hydro_value = -3.20
	elif aa == 'I':
		hydro_value = 4.50
	elif aa == 'K':
		hydro_value = -3.90
	elif aa == 'L':
		hydro_value = 3.80
	elif aa == 'M':
		hydro_value = 1.90
	elif aa == 'P':
		hydro_value = -1.60
	elif aa == 'R':
		hydro_value = -4.50
	elif aa == 'S':
		hydro_value = -0.80
	elif aa == 'T':
		hydro_value = -0.70
	elif aa == 'V':
		hydro_value = 4.20
	elif aa == 'W':
		hydro_value = -0.90
	elif aa == 'Y':
		hydro_value = -1.30
	else:
		sys.exit('Error: not amino acid or typo')
	print(hydro_value)
	return hydro_value
		
kyte('A')
kyte('C')
kyte('Q')
kyte('M')
kyte('O')