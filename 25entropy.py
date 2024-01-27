#Co-Authors - Devin Fan, Sophia Chen

import math

def shannon(a, c, g, t):
	total = a + c + g + t
	
	p_a = a / total
	p_c = c / total
	p_g = g / total
	p_t = t / total
	
	entropy = - (p_a * math.log2(p_a)) - (p_c * math.log2(p_c)) - (p_g * math.log2(p_g)) - (p_t * math.log2(p_t))
    
	return entropy
	
print(shannon(1,2,3,5))
print(shannon(10,20,30,50))
print(shannon(69,420,1,6))
