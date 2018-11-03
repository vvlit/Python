#!/usr/bin/python3
import random
n = int(input('Введите длину списка: '))
spisok = []
for i in range(0, n):
	spisok.append(random.randint(0, n*5))
print('Исходный список: {}'.format(spisok))
for i in range(0, n - 1):
	min = i
	tmp = spisok[i]
	for j in range(i + 1, n):
		if spisok[min] > spisok[j]:
			min = j
	spisok[i] = spisok[min]
	spisok[min] = tmp
print('Отсортированный список: {}'.format(spisok))