# -*- coding: utf-8 -*-
"""36"""

import sys, collections
from q30 import mecab_reader

def word_counter():		# 単語:出現頻度の辞書
 	words = []
	for morph_list in mecab_reader(sys.stdin):
		for word in morph_list:
			words.append(word['base'])	
	word_dict = collections.Counter(words)	
	
	return word_dict.most_common()		# [(単語, 出現頻度), ...]
	
if __name__ == "__main__":
	for word,cnt in word_counter():
		print '{}\t{}'.format(word,cnt)

"""
$ python 36.py < neko.txt.mecab

の	9194
。	7486
て	6848
、	6772
は	6420
に	6243
を	6071
だ	5975
と	5508
が	5337
た	4267
する	3657
「	3231
」	3225
ない	3052
も	2479
ある	2320
...
"""
	