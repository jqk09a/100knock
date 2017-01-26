# -*- coding: utf-8 -*-
"""32"""

import sys
from q30 import mecab_reader

for morph_list in mecab_reader(sys.stdin):
	for word in morph_list:
		if word['pos'] == '動詞':
			print '{base}'.format(**word)
			
"""
$ python 32.py < neko.txt.mecab

生れる
つく
する
泣く
する
いる
始める
見る
聞く
捕える
煮る
食う
...
"""