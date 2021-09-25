# factorial.py

# Алгоритм нахождения факториала числа

def factorial(factor):
	for i in range(1, factor):
		factor = factor*i

	print(factor)
    
factorial(5)
