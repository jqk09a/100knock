# 17
# -*- coding: utf-8 -*-

with open('hightemp.txt') as h:
	s = set()
	for line in h:
		s.add(line.split()[0])
for i in s:
	print i
