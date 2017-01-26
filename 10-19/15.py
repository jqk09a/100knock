# -*- coding: utf-8 -*-
"""15"""

"""
リングバッファ使わないver. またの名をリスト爆発ver.

n = input('Please input N > ')
with open('hightemp.txt','r') as h:
	h_list = h.readlines()
for i in range(n):
	print h_list[len(h_list)-n+i].rstrip()
	
=> for x in h_list[:-n]:
	print x.rstrip
"""


import collections

n = input('Please input N > ')

with open('hightemp.txt','r') as h:
	h_list = collections.deque(h, n)
for i in h_list:
	print i.rstrip()


# $ tail -N hightemp.txt
