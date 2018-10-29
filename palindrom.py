#!/usr/bin/python3
word = input('Введите слово: ')
word_reverse = word[::-1]
if word == word_reverse:
	print('Это слово является палиндромом.')
else:
	print('Это слово не является палиндромом.')