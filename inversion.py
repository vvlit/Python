#!/usr/bin/python3

""" Inversions counting.

The programm generates a list of random numbers and counts inversions.
'n' is a list length. Two elements form inversion if list[i] > list[j] and i < j.
"""

import random

# Take input from user to define a list length
n = int(input('Введите длину списка: '))

# Generate list of random numbers from 1 to n*5, n - list length
spisok = random.sample(range(1, n * 5), n)

# List output
print(spisok)

# Count inversions.
# For each list item (except the last one) check whether it is bigger than each of the following
inversion = 0
for i in range(0, n - 1): # loop for each list item
	for j in range(i + 1, n): # loop for each of the following items
		if spisok[i] > spisok[j]: # compare items
			inversion = inversion + 1 # take the inversion into account
		j += 1 # go to the next following item
	i += 1 # go to the next item

print('Количество инверсий в списке: {}.'.format(inversion))