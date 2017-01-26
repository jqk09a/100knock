# 11
# -*- coding: utf-8 -*-

with open('hightemp.txt','r') as h:
	for line in h:
		print ' '.join(line.split())

# $ tr '\t' ' ' < hightemp.txt > 11.txt
