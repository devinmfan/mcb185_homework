for i in range(1, 101):
    
	x = i
    
	if i % 3 == 0:
		x = "Fizz"
        
	if i % 5 == 0:
		x = "Buzz"
        
	if i % 5 == 0 and i % 3 == 0:
		x = "FizzBuzz"
        
	print(x)
