# -*- coding: utf-8 -*-
"""33"""

import sys
from q30 import mecab_reader

for morph_list in mecab_reader(sys.stdin):
	for word in morph_list:
		if word['pos1'] == 'サ変接続':
			print '{surface}'.format(**word)

"""
$ python 33.py < neko.txt.mecab

見当
記憶
話
装飾
突起
運転
記憶
分別
決心
我慢
餓死
訪問
...
"""

