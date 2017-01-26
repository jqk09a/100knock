# -*- coding: utf-8 -*-
"""39"""

import sys, collections
import matplotlib.pyplot as plt
import seaborn as sea
from q38 import freq_counter

y=[]			# 出現頻度
repeat=[]		# 重複
for cnt, word in sorted(freq_counter(), reverse=True):
	y.append(cnt)
	repeat.append(word)

x=[]			# 順位
i=1
for r in repeat:
	x.append(i)
	i += r

# グラフを表示(点でプロット)
plt.loglog(x, y, 'o')
plt.xlabel(u'出現頻度順位(log)')
plt.ylabel(u'出現回数(log)')
plt.title(u'Zipfの法則')
plt.show()	

"""
$ python 39.py <neko.txt.mecab

http://www.cl.ecei.tohoku.ac.jp/~reina.a/nlp100/39.png
"""
