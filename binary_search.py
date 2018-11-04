#!/usr/bin/python3
n = int(input('Введите длину списка: '))
x = int(input('Введите искомое (целое) число: '))
import random

spisok = []
for i in range(0, n):
	spisok.append(random.randint(0, n))
print('Исходный список: {}'.format(spisok))

for i in range(1, n):
	k = spisok[i]
	j = i - 1
	while j >= 0 and k < spisok[j]:
		spisok[j + 1] = spisok[j]
		j -= 1
	spisok[j + 1] = k
print('Отсортированный список: {}'.format(spisok))

min_index = 0
max_index = n - 1
x_index = - 1 # Искомого числа нет в списке

while min_index < max_index - 1:
	
	if x < spisok[min_index] or x > spisok[max_index]:
		print('Этого числа нет в списке.')
		break
	
	if x == spisok[min_index]:
		print('Число {} находится на позиции {} в отсортированном списке.'.format(x, min_index))
		x_index = min_index
		break
	
	if x == spisok[max_index]:
		print('Число {} находится на позиции {} в отсортированном списке.'.format(x, max_index))
		x_index = max_index
		break
	
	if (max_index - min_index) % 2 == 0:
		mid_index = min_index + (max_index - min_index) // 2
	else:
		mid_index = min_index + (max_index - min_index) // 2 + 1
	
	if x == spisok[mid_index]:
		print('Число {} находится на позиции {} в отсортированном списке.'.format(x, mid_index))
		x_index = mid_index
		break
	
	if x > spisok[mid_index]:
		min_index = mid_index
	else:
		max_index = mid_index

else:
	print('Этого числа нет в списке.')

if x_index > - 1:
	i = 1
	if x_index != max_index:
		while x_index + i <= max_index and spisok[x_index] == spisok[x_index + i]:
			print('Число {} находится на позиции {} в отсортированном списке.'.format(x, x_index + i))
			i += 1

	i = 1
	if x_index != min_index:
		while x_index >= min_index and spisok[x_index] == spisok[x_index - i]:
			print('Число {} находится на позиции {} в отсортированном списке.'.format(x, x_index - i))
			i += 1