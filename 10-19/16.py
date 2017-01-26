# -*- coding: utf-8 -*-
"""16"""

with open('hightemp.txt','r') as h:
	lines = [line.rstrip() for line in h]

n = input('Please input N > ')
m = len(lines) / n
o  = len(lines) % n

while len(lines) != 0:
	if o != 0:
		tmp = lines[:m+1]
		del lines[:m+1]
		o -= 1
	else:
		tmp = lines[:m]
		del lines[:m]
	for i in tmp:
		print i
	print ''

# 4分割(24行÷4=6行ずつ)の例
# $ split -l 6 hightemp.txt
# $ ls xa*		---------->	xaa	xab	xac	xad
# $ cat xa*
