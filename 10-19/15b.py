# -*- coding: utf-8 -*-
"""15(ringbuffer)"""

import collections

n = input('Please input N > ')

with open('hightemp.txt','r') as h:
	h_list = collections.deque(h, n)

for i in h_list:
	print i.rstrip()
