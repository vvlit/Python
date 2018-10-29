#!/usr/bin/python3
n = int(input(
			'До какого числа сгенерировать последовательность Фибоначчи?\n'
			'Введите целое число: '))
Fibonacci = [1, 1]
while Fibonacci[-2] + Fibonacci[-1] < n:
	Fibonacci.append(Fibonacci[-2] + Fibonacci[-1])
print(Fibonacci)