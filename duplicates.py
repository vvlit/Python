#!/usr/bin/python3
n = int(input('Введите длину списка: '))
import random
spisok = []
for i in range(0, n):
	spisok.append(random.randint(0, n))
print(spisok)
spisok_1 = []
spisok_1.append(spisok[0])
for i in range(1, n):
	counter = 0
	for j in range(0, i):
		if spisok[i] == spisok[j]:
			counter += 1
	if counter == 0:
		spisok_1.append(spisok[i])
print(spisok_1)