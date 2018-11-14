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
		if lst[j] <= splitter:
			i += 1
			lst[i], lst[j] = lst[j], lst[i]
	lst[i + 1], lst[end] = lst[end], lst[i + 1]
	return i + 1

def quick_sort(lst, start, end):
	"""
	Sorts list of items using quick sort algorithm.
	This is iterative implementation of quick sort algorithm.
	"""

	stack = []
	stack.append(start)
	stack.append(end)
	while stack:
		end = stack.pop()
		start = stack.pop()
		s = split(lst, start, end)

		if s - 1 > start:
			stack.append(start)
			stack.append(s - 1)

		if s + 1 < end:
			stack.append(s + 1)
			stack.append(end)

quick_sort(lst, 0, len(lst) - 1)
print('Output list: {}'.format(lst))