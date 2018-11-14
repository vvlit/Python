#!/usr/bin/python3

response = input('Enter some text, please: ')
unnecessary_symbols = [',', '-', '!', '?', ':', '.', ';']
for i in unnecessary_symbols:
	response = response.replace(i, ' ')
lst = response.split()
lst.sort()
i = 0
while i < len(lst):
	lst_i_amount = lst.count(lst[i])
	print('{}:'.format(lst[i]), lst_i_amount)
	i += lst_i_amount