# -*- coding: utf-8 -*-
"""13"""

with open('col1.txt','r') as col1,open('col2.txt','r') as col2,open('col1col2.txt','w') as col1col2:
	for line1,line2 in zip(col1,col2):
		col1col2.write(line1.replace('\n','\t') + line2)

# $ paste col1.txt col2.txt