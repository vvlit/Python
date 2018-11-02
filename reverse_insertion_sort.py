#!/usr/bin/python3
n = int(input('Введите длину списка: '))
spisok = []
import random
for i in range(0, n):
	spisok.append(random.randint(0, n*5))
print(spisok)
for i in range (1, len(spisok)):
	k = spisok[i]
	j = i - 1
	while j >= 0 and k > spisok[j]:
		spisok[j + 1] = spisok[j]
		j -= 1
	spisok[j + 1] = k
print(spisok)