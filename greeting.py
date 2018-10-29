#!/usr/bin/python3
response = input('What is your name?\n > ')
name_prefix = 'name is'
name_prefix_start_index = response.find(name_prefix)
name_prefix_length = len(name_prefix)
if name_prefix_start_index > -1:
	name_start_index = name_prefix_start_index + name_prefix_length + 1
	name = response[name_start_index:]
	print('Hello, {}!'.format(name))
else:
	print(
		"Couldn't find your name! Please use the following format:\n"
		"My name is <your name here>")
