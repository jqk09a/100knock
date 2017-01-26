# -*- coding: utf-8 -*-
"""14"""

n = input('Please input N > ')

with open('hightemp.txt','r') as h:
	for i in range(n):
		print h.readline().rstrip()

# $ head -N hightemp.txt
