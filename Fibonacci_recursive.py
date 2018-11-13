#!/usr/bin/python3

def fibonacci(lst):
	"""Fibonacci numbers generating"""

	if lst[-1] + lst[-2] < N:
		lst.append(lst[-1] + lst[-2])
		fibonacci(lst)




N = int(input(
			'To which number Fibonacci numbers must be generated?\n'
			'Enter an integer: '))
lst = [1, 1]
fibonacci(lst)
print('Fibonacci numbers: {}'.format(lst))