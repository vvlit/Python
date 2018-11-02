#!/usr/bin/python3
n = int(input('Введите длину первого списка: '))
m = int(input('Введите длину второго списка: '))
import random
spisok_1 = []
spisok_2 = []
for i in range(0, n):
	spisok_1.append(random.randint(0, n))
print(spisok_1)
for i in range(0, m):
	spisok_2.append(random.randint(0, m))
print(spisok_2)
spisok_joint_0 = []
for i in range (0, n):
	for j in range(0, m):
		if spisok_1[i] == spisok_2[j]:
			spisok_joint_0.append(spisok_1[i])
print(spisok_joint_0)
spisok_joint = []
spisok_joint.append(spisok_joint_0[0])
for i in range(1, len(spisok_joint_0)):
	counter = 0
	for j in range(0, i):
		if spisok_joint_0[i] == spisok_joint_0[j]:
			counter += 1
	if counter == 0:
		spisok_joint.append(spisok_joint_0[i])
print(spisok_joint)