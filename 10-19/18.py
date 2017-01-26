# 18
# -*- coding: utf-8 -*-

import operator

with open('hightemp.txt','r') as h:
	lines = [line.split() for line in h]

temp = sorted(lines, key=operator.itemgetter(2), reverse=True)

for line in temp:
	print '\t'.join(line)