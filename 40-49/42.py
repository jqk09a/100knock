# -*- coding: utf-8 -*-
"""42"""

import sys, collections
from q40 import Morph, Chunk, cabocha_reader02

# [chunk,dst]を要素とするtext1行文のリストc_d_listを返す
def src_dst(data):
    c_d_list = []
    for chunk in data:
        chnk = "".join(morph.surface for morph in chunk.morphs \
				if morph.pos != "記号")
        tmp = [chnk,int(chunk.dst)]
        c_d_list.append(tmp)
    return c_d_list

if __name__ == "__main__":
    for chunk_list in cabocha_reader02(sys.stdin):
        c_d_list = src_dst(chunk_list)
        for c in c_d_list:
            if c[1] != -1:
                d = c_d_list[c[1]]
                print "{}\t{}".format(c[0],d[0])
        print ''

"""
$ python 42.py<koneko.txt.cabocha

　	猫である
吾輩は	猫である

名前は	無い
まだ	無い


　どこで	生れたか
生れたか	つかぬ
とんと	つかぬ
見当が	つかぬ

"""

# 空白も記号、cabochaの解析結果"記号"を使って除去できる
#
