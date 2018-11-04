#!/usr/bin/python3
n = int(input('Введите длину списка: '))
import random
fibonacci = [1, 1]
for i in range(0, n * 5 - 2):
	fibonacci.append(fibonacci[i] + fibonacci[i + 1])
print('Список Фибоначчи: {}'.format(fibonacci))
spisok = random.sample(fibonacci, n)
print('Исходный список: {}'.format(spisok))
for i in range(1, n):
	k = spisok[i]
	j = i - 1
	while j >= 0 and k < spisok[j]:
		spisok[j + 1] = spisok[j]
		j -= 1
	spisok[j + 1] = k
print('Отсортированный список: {}'.format(spisok))