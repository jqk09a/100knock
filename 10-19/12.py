# -*- coding: utf-8 -*-
''' 12 '''
with open('hightemp.txt','r') as h,open('col1.txt','w') as col1,open('col2.txt','w') as col2:
	for line in h:
		col1.write(line.split()[0] + '\n')
		col2.write(line.split()[1] + '\n')
	
# $ cut -f 1 < hightemp.txt
# $ cut -f 2 < hightemp.txt
