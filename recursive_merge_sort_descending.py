#!/usr/bin/python3

import random

def merge_sort(l):
	""" Recursive merge sort."""

	if len(l) > 1:
		mid = len(l) // 2
		left = l[:mid]
		right = l[mid:]

		merge_sort(left)
		merge_sort(right)

		i = j = k = 0
		while i < len(left) and j < len(right):
			if left[i] > right[j]:
				l[k] = left[i]
				i += 1
			else:
				l[k] = right[j]
				j += 1
			k += 1

		if i < len(left):
			l[k: k + len(left[i:])] = left[i:]
		if j < len(right):
			l[k: k + len(right[j:])] = right[j:]

n = int(input('Enter the lenghth of the list: '))
lst = random.sample(range(1, n * 10), n)
print('Input list: {}'.format(lst))
merge_sort(lst)
print('Output list: {}'.format(lst))