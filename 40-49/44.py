# -*- coding: utf-8 -*-
"""44"""

from graphviz import Digraph
import sys, collections
from q40 import Morph, Chunk, cabocha_reader02, src_dst

if __name__ == "__main__":
    for i,chunk_list in enumerate(cabocha_reader02(sys.stdin),start=1):
		if i == 13:
			c_d_list = src_dst(chunk_list)

			# 有向グラフを描く
			G = Digraph('graph', filename='44.gv')
			G.attr('node', shape='circle')

			for c in c_d_list:
				if c[1] != -1:
					d = c_d_list[c[1]]
					#要素を追加
					G.edge(c[0],d[0])

			#画像を出力
			G.view()

"""
$ python 44.py <koneko.txt.cabocha

http://www.cl.ecei.tohoku.ac.jp/~reina.a/nlp100/44.gv.pdf
"""
