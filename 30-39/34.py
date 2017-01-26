# -*- coding: utf-8 -*-
"""34"""

import sys
from q30 import mecab_reader

for morph_list in mecab_reader(sys.stdin):
	for i,word in enumerate(morph_list):
		if word['pos1'] == '連体化':
			print morph_list[i-1]['surface']+morph_list[i]['surface']+morph_list[i+1]['surface']
			
"""
$ python 34.py < neko.txt.mecab

彼の掌
掌の上
書生の顔
はずの顔
顔の真中
穴の中
書生の掌
掌の裏
何の事
肝心の母親
までの所
藁の上
笹原の中
...
"""
