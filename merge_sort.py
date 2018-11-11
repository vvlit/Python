#!/usr/bin/python3

# Merge sort

import random

n = int(input('Введите длину списка: '))

# generate a list
spisok = random.sample(range(1, n * 5), n)
# list output
print('Исходный список: {}'.format(spisok))

# define minimal sublist size
podspisok_size = 1

while podspisok_size < n:
	# index of the first split item (the first item of the first sublist)
	start = 0
	
	while start < n:
		
		# index of the middle split item (the last item of the first sublist)
		middle = start + podspisok_size - 1
		# index of the last split item (the last item of the second sublist)
		end = min(start + 2 * podspisok_size - 1, n - 1)

		# sizes of additional lists
		merge_list_1_size = middle - start + 1
		merge_list_2_size = end - middle

		# additional lists for sorting and merging
		merge_list_1 = spisok[start: start + merge_list_1_size]
		merge_list_2 = spisok[middle + 1: middle + merge_list_2_size + 1]

		# indexes of merge_list_1, merge_list_2, spisok
		i, j, k = 0, 0, start
		# sorting and merging unit
		while i < merge_list_1_size and j < merge_list_2_size:
			if merge_list_1[i] < merge_list_2[j]:
				spisok[k] = merge_list_1[i]
				i += 1
			else:
				spisok[k] = merge_list_2[j]
				j += 1
			k += 1

		if i < merge_list_1_size:
			spisok[k: k + len(merge_list_1[i:])] = merge_list_1[i:]

		if j < merge_list_2_size:
			spisok[k: k + len(merge_list_2[j:])] = merge_list_2[j:]

		start = start + podspisok_size * 2

	podspisok_size = 2 * podspisok_size

print('Отсортированный список: {}'.format(spisok))