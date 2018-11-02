#!/usr/bin/python3
i = 1500
spisok = []
while i <= 3000:
	if i % 7 == 0 and i % 3 != 0:
		spisok.append(i)
	i += 1
print('Числа в диапазоне от 1500 до 3000 включительно, которые делятся на 7, но не делятся на 3:\n', spisok)