# 09
# -*- coding: utf-8 -*-

from random import shuffle

s = raw_input('Please input > ')

w_list = s.split()
for word in w_list:
	c_list = list(word)
	if len(c_list)>4:
		s_list = c_list[1:-1]
		shuffle(s_list)
		c_list[1:-1] = s_list
	print ''.join(c_list),
