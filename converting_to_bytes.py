#!/usr/bin/python3

#converting to bytes

name = input('Enter your name, please: ')
name_bytes = name.encode('utf-8')
print(f'Your name converted to bytes: {name_bytes}')