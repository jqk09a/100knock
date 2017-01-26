# -*- coding: utf-8 -*-
"""37"""

import sys
import matplotlib.pyplot as plt
import seaborn as sea             #ちょっとくらいはおしゃれになる
from q36 import word_counter

x=[]		# 単語
y=[]		# 出現回数
for k,v in word_counter():
	x.append(k.decode('utf-8'))
	y.append(v)
	if len(x)>9:
		break

# 棒グラフで表示		
plt.bar(range(10), y, width=0.6, align='center')
plt.xlim(-1,10)
plt.xticks(range(10), x)
plt.xlabel(u'単語')
plt.ylabel(u'出現回数')
plt.title(u'単語の出現頻度')
plt.show()


"""
$ python 37.py <neko.txt.mecab

http://www.cl.ecei.tohoku.ac.jp/~reina.a/nlp100/37.png
"""