#!/usr/bin/python3
import random
number = random.randint(0,1000)
response_number = -1
while response_number != number:
	response_number = int(input('Введите целое число от 0 до 1000: '))
	if response_number == number:
		print('Поздравляю, Вы угадали!')
	elif response_number > number:
		print('Загаданное число меньше!')
	else:
		print('Загаданное число больше!')