# -*- coding: utf-8 -*-
"""45"""

# だめでした。　->できました！！！

import sys, collections
from q40 import Morph, Chunk, cabocha_reader02, src_dst

def v_a(data):
    v_a_dic = collections.defaultdict(set)
    for chunk in data:
        d_chunk = data[int(chunk.dst)]
        a_list = []

        a = False
        for morph in chunk.morphs:
            if morph.pos == '助詞':
                a = True
                a_list.append(morph.base)

        if a:
            for morph in d_chunk.morphs:
                if morph.pos == '動詞':
                    for a in a_list:
                        v_a_dic[morph.base].add(a)
                    break
    return v_a_dic


if __name__=="__main__":
    for chunk_list in cabocha_reader02(sys.stdin):
        for v,a in v_a(chunk_list).iteritems():
            a = ' '.join(sorted(a))
            print '{}\t{}'.format(v,a)


"""
$ python 45.py <koneko.txt.cabocha
生れる	で
つく	か が
泣く	で
する	だけ て は
始める	で
見る	は を
聞く	で
食う	て
捕える	を
煮る	て
思う	から
ある	が ばかり
持ち上げる	て と
載せる	に
落ちつく	で
見る	て の を

↓ 小林さんの神コマンドを使ってみる
$ cat 45.txt | grep -E "^(する|見る|与える)\s" | sort | uniq -c | sort -k 2,2 -k 1,1nr | less
    265 する    を
    116 する    に
     81 する    に を
     72 する    と
     67 する    が
     ・
     ・
     ・
    177 見る    て
     84 見る    を
     20 見る    て を
     17 見る    から
     15 見る    から て
     ・
     ・
     ・
      3 与える  に を
      2 与える  て に は を
      1 与える  が を
      1 与える  け に を
      1 与える  て に を
"""
