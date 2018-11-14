#!/usr/bin/python3

def sorted_or_not(lst, i):
	"""Check if list is sorted"""

	if i < len(lst) - 1:
		if lst[i] < lst[i + 1]:
			i += 1		
			if i == len(lst) - 1:
				print('List is sorted.')
			sorted_or_not(lst, i)
		else:
			print('List is not sorted.')

lst = [1, 3, 5, 7, 9, 15, 30, 50, 70]
print('List: {}'.format(lst))
i = 0
sorted_or_not(lst, i)