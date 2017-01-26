# -*- coding: utf-8 -*-
"""40"""

import sys

# class Morphを定義
class Morph:
	def __init__(self, surface, base, pos, pos1):
	    self.surface = surface
	    self.base = base
	    self.pos = pos
	    self.pos1 = pos1

	# [表層形,基本形,品詞,品詞細分類1]のリストを返す
	def __str__(self):
	    return "[surface:{}, base:{}, pos:{}, pos1:{}]".format(self.surface, self.base, self.pos, self.pos1)

# 係り受け解析結果(cabocha)の形態素を読み込む関数
def cabocha_reader01(data):
    morph_list = []
    for line in data:
        if line.startswith('*'):
            continue
        elif line.startswith('EOS'):
            yield morph_list
            morph_list = []
        else:
            sur, other = line.split('\t')
            o = other.split(',')
            morph_list.append(Morph(sur, o[6], o[0], o[1]))

if __name__ == "__main__":
       for i,morph_list in enumerate(cabocha_reader01(sys.stdin), start=1):
        if i == 3:                      # i:何文目か. 3文目を出力
            for morph in morph_list:
                print morph


"""
$ python 40.py < neko.txt.cabocha

[surface:　, base:　, pos:記号, pos1:空白]
[surface:吾輩, base:吾輩, pos:名詞, pos1:代名詞]
[surface:は, base:は, pos:助詞, pos1:係助詞]
[surface:猫, base:猫, pos:名詞, pos1:一般]
[surface:で, base:だ, pos:助動詞, pos1:*]
[surface:ある, base:ある, pos:助動詞, pos1:*]
[surface:。, base:。, pos:記号, pos1:句点]
"""
