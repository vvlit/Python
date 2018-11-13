#!/usr/bin/python3

# The program generate sorted list of numbers.
# Even elements are divisible by 3.
# Odd elements are divisible by 5.
# 'N' is an input parameter - a number to which list is generated.

def add_element_to_list(lst, i, j, N):
	if i < N:
		if (j + 1) % 2 == 0:
			while i % 3 != 0:
				i += 1
		else:
			while i % 5 != 0:
				i += 1
		if i < N:
			lst.append(i)
		i += 1
		j += 1
		add_element_to_list(lst, i, j, N)


N = int(input('Enter a number to which list will be generated: '))
lst = []
j = 0
i = 1
add_element_to_list(lst, i, j, N)

print('Output list: {}'.format(lst))