# -*- coding: utf-8 -*-
"""43"""

import sys, collections
from q40 import Morph, Chunk, cabocha_reader02

def n_v(data):
	for chunk in data:
		d_chunk = data[int(chunk.dst)]
		if chunk.dst != '-1':
			src = "".join(morph.surface for morph in chunk.morphs \
					if morph.pos != "記号")
			dst = "".join(morph.surface for morph in  d_chunk.morphs \
					if morph.pos != "記号")

			n = False
			for morph in chunk.morphs:
				if morph.pos == '名詞':
					n = True
					break

			v = False
			for morph in d_chunk.morphs:
				if morph.pos == '動詞':
					v = True
					break

			if n and v:
				print "{}\t{}".format(src,dst)


if __name__=="__main__":
	for chunk_list in cabocha_reader02(sys.stdin):
		 n_v(chunk_list)


"""
$ python 43.py < neko.txt.cabocha

どこで	生れたか
見当が	つかぬ
所で	泣いて
ニャーニャー	泣いて
いた事だけは	記憶している
吾輩は	見た
ここで	始めて
ものを	見た
あとで	聞くと
"""

"""
l.11-14をl.26以下に書いた方がコスト削減できる
"""
