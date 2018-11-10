#!/usr/bin/python3

""" Euclidean algorithm.

Method for computing the greatest common divisor of two numbers,
the largest number that divides both of them without leaving a remainder.

The Euclidean algorithm is based on the principle that the greatest
common devisor of two numbers does not change if the larger number is
replaced by it's difference with the smaller number.
"""
# Take input from user to define numbers
A = int(input('Введите целое положительное число: '))
B = int(input('Введите второе целое положительное число: '))

# The loop continues until two numbers become equal
while A != B:
	
	# The larger of two numbers is replaced with numbers difference 
	if A > B:
		A = A - B
	else:
		B = B - A

# Output of the greatest common divisor of two numbers
print('Наибольший общий делитель: {}'.format(A))