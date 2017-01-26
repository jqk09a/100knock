# -*- coding: utf-8 -*-
"""46"""

import sys, collections,operator
from q40 import Morph, Chunk, cabocha_reader02, src_dst

def v_a(data):
    v_a_dic = collections.defaultdict(list)
    for chunk in data:
        d_chunk = data[int(chunk.dst)]
        a_ac_list = []

        a = False
        for morph in chunk.morphs:
            if morph.pos == '助詞':
                a = True
                ac = "".join(morph.surface for morph in chunk.morphs \
                    if morph.pos != "記号")
                a_ac_list.append([morph.base, ac])

        if a:
            for morph in d_chunk.morphs:
                if morph.pos == '動詞':
                    for a_ac in a_ac_list:
                        v_a_dic[morph.base].append(a_ac)
                    break
    return v_a_dic


if __name__=="__main__":
    for chunk_list in cabocha_reader02(sys.stdin):
        for v,a_ac in v_a(chunk_list).iteritems():
            a_ac = sorted(a_ac, key=operator.itemgetter(0))
            a=''
            ac=''
            for i in a_ac:
                a += ' '+i[0]
                ac += ' '+i[1]
            print '{}\t{}\t{}'.format(v,a,ac)

"""
$ python 46.py <neko.txt.cabocha
生れる	 で	 どこで
つく	 か が	 生れたか 見当が
泣く	 で	 所で
する	 だけ て て は	 いた事だけは 泣いて 記憶している いた事だけは
始める	 で	 ここで
見る	 は を	 吾輩は ものを
聞く	 で	 あとで
食う	 て	 煮て
捕える	 を	 我々を
煮る	 て	 捕えて
思う	 から	 なかったから
ある	 が ばかり	 感じが あったばかりである
持ち上げる	 て と	 載せられて スーと
載せる	 に	 掌に
落ちつく	 で	 上で
見る	 て の を	 落ちついて ものの 顔を
"""
