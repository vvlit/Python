#!/usr/bin/python3

def elements_change(lst, i):
	"""List element replaces wiht opposite index list element """

	if i < len(lst) / 2:	
		lst[i], lst[-i - 1] = lst[-i - 1], lst[i]
		i += 1
		elements_change(lst, i)


import random

n = int(input('Введите n: '))
lst = random.sample(range(1, n * 5), n)
print(lst)

i = 0
elements_change(lst, i)

print(lst)