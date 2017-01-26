# 19
# -*- coding: utf-8 -*-

import collections

with open('hightemp.txt','r') as h:
	lines = [line.split()[0] for line in h]

counter = collections.Counter(lines)

for i,cnt in counter.most_common():
	print str(cnt) + ' ' + i