#Devin Fan & Sophia Chen


def pi_comp(n):
	pi_gl = 0
	const_gl = 1
	x_gl = 1
	pi_ni = 3
	const_ni = 4
	x_ni = 2
	y_ni = 3
	z_ni = 4
	for i in range(0, n):
		pi_gl = pi_gl + (const_gl / x_gl)
		x_gl = x_gl + 2
		const_gl = const_gl * -1
		pi_ni = pi_ni + (const_ni / (x_ni * y_ni * z_ni))
		x_ni = x_ni + 2
		y_ni = y_ni + 2
		z_ni = z_ni + 2
		const_ni = const_ni * -1
		print(pi_ni, 4*pi_gl)
		
pi_comp(100)