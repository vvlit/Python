#!/usr/bin/python3

import random

lst = random.sample(range(1, 100), 15)
print('Input list: {}'.format(lst))

def split(lst, start, end):
	"""
	Splits list into two parts.

	Split list into two parts each element of first part
	are not bigger than every element
	
	"""
	i = start - 1
	splitter = lst[end]

	for j in range(start, end):
		if lst[j] >= splitter:
			i += 1
			lst[i], lst[j] = lst[j], lst[i]
	lst[i + 1], lst[end] = lst[end], lst[i + 1]
	return i + 1

def quick_sort(lst, start, end):
	"""
	Sorts list of items using quick sort algorithm.

	This is recursive implementation of quick sort algorithm.
	"""
	if start < end:
		s = split(lst, start, end)
		quick_sort(lst, start, s - 1)
		quick_sort(lst, s + 1, end)
	

quick_sort(lst, 0, len(lst) - 1)
print('Output list: {}'.format(lst))