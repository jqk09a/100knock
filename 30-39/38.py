# -*- coding: utf-8 -*-
"""38"""

import sys, collections
import matplotlib.pyplot as plt
import seaborn as sea
from q36 import word_counter

def freq_counter():
	freq = []		# 出現頻度:単語数の辞書
	for word,cnt in word_counter():
		freq.append(cnt)
	freq_dict = collections.Counter(freq)
	
	return freq_dict.most_common()		# [(出現頻度, 単語数), ...]

x = []			# 出現頻度
y = []			# 単語数
for k,v in freq_counter():
	x.append(k)
	y.append(v)

# 棒グラフで表示
plt.bar(x, y, align='center')
plt.xlim(0,100)
#plt.ylim(0,20)
plt.xlabel(u'出現頻度')
plt.ylabel(u'単語種類数')
plt.title(u'単語の出現頻度のヒストグラム')
plt.show()

"""
$ python 38.py <neko.txt.mecab

http://www.cl.ecei.tohoku.ac.jp/~reina.a/nlp100/38.png
"""
