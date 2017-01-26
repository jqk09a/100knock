# -*- coding: utf-8 -*-
"""31"""

import sys
from q30 import mecab_reader
for morph_list in mecab_reader(sys.stdin):
	for word in morph_list:
		if word['pos'] == '動詞':
			print '{surface}'.format(**word)
			
"""
$ python 31.py < neko.txt.mecab

生れ
つか
し
泣い
し
いる
始め
見
聞く
捕え
煮
食う
...
"""