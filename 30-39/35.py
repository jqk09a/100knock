# -*- coding: utf-8 -*-
"""35"""

import sys
from q30 import mecab_reader

for morph_list in mecab_reader(sys.stdin):
	flag1 = False
	flag2 = False
	tmp = []
#	print '\n'
	for word in morph_list:
		if not flag1 and word['pos'] == '名詞':
			tmp.append(word['surface'])
			flag1 = True
#			print '1'
		elif flag1 and word['pos'] == '名詞':
			tmp.append(word['surface'])
			flag2 = True
#			print '2'
		elif flag2 and word['pos'] == '名詞':
			tmp.append(word['surface'])
#			print '3'
		elif flag2 and not(word['pos'] == '名詞'):
			print ''.join(tmp)
			flag1 = False
			flag2 = False
			tmp = []
#			print '4'
		else:
			flag1 = False
			flag2 = False
			tmp = []
#			print '5'
		
"""
$ python 35.py < neko.txt.mecab

人間中
一番獰悪
時妙
一毛
その後猫
一度
...
"""