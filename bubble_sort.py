#!/usr/bin/python3
n = int(input('Введите длину списка: '))
import random
spisok = []
for i in range(0, n):
	spisok.append(random.randint(0, n*5))
print('Исходный список: {}'.format(spisok))
for i in range(0, n):
	swapped = 0
	for j in range(0, n - i - 1):
		if spisok[j] >= spisok[j + 1]:
			tmp = spisok[j]
			spisok[j] = spisok[j + 1]
			spisok[j + 1] = tmp
			swapped = 1
	if swapped == 0:
		break
print('Отсортированный список: {}'.format(spisok))