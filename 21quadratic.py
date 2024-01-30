#Co-Authors - Devin Fan, Sophia Chen
import math

def quad (a, b, c):
	
	x1 = (-b + math.sqrt(b**2 - 4 * a * c)) / 2 * a
	x2 = (-b - math.sqrt(b**2 - 4 * a * c)) / 2 * a
	
	return x1, x2

print(quad(1, 2, 1))
print(quad(2, -4, -1))
print(quad(1, -5, -14))