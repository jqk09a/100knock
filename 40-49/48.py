# -*- coding: utf-8 -*-
"""48"""

import sys
from q40 import Morph, Chunk, cabocha_reader02, search_noun, make_chunk

def n_pass(data):
    for chunk in data:
        if search_noun(chunk):
            p_list = []
            c = make_chunk(chunk)
            p_list.append(c)
            dst = int(chunk.dst)
            while dst>-1:
                next_chunk = data[dst]
                c = make_chunk(next_chunk)
                p_list.append(c)
                dst = int(next_chunk.dst)
            if len(p_list)>1:
                print '->'.join(p_list)



if __name__ == "__main__":
    for chunk_list in cabocha_reader02(sys.stdin):
        n_pass(chunk_list)
        print ''


"""
$ python 48.py <koneko.txt.cabocha


吾輩は->猫である

名前は->無い


どこで->生れたか->つかぬ
見当が->つかぬ

何でも->薄暗い->所で->泣いて->記憶している
所で->泣いて->記憶している
ニャーニャー->泣いて->記憶している
いた事だけは->記憶している

吾輩は->見た
ここで->始めて->人間という->ものを->見た
人間という->ものを->見た
ものを->見た

あとで->聞くと->種族であったそうだ
それは->種族であったそうだ
書生という->人間中で->種族であったそうだ
人間中で->種族であったそうだ
一番->獰悪な->種族であったそうだ
獰悪な->種族であったそうだ

"""
