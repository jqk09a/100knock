# -*- coding: utf-8 -*-
"""47"""

import sys, collections,operator
from q40 import Morph, Chunk, cabocha_reader02, src_dst

def v_a(data):
    v_a_dic = collections.defaultdict(list)
    for chunk in data:
        d_chunk = data[int(chunk.dst)]
        if int(chunk.dst)<0:
            break
        pd_chunk = data[int(chunk.dst)-1]
        a_ac_list = []

        for morph in chunk.morphs:
            if morph.pos == '助詞':
                ac = ''.join(morph.surface for morph in chunk.morphs if morph.pos != "記号")
                a_ac_list.append([morph.base, ac])

        if len(pd_chunk.morphs)>1 and pd_chunk.morphs[0].pos1=='サ変接続' and pd_chunk.morphs[1].surface=='を':
            sc = ''.join(morph.surface for morph in pd_chunk.morphs)
            for morph in d_chunk.morphs:
                if morph.pos == '動詞':
                    for a_ac in a_ac_list:
                        v_a_dic[sc + morph.base].append(a_ac)
                    break

    return v_a_dic


if __name__=="__main__":
    for chunk_list in cabocha_reader02(sys.stdin):
        v_a_dic = v_a(chunk_list)
        for v,a_ac in v_a_dic.iteritems():
            a_ac = sorted(a_ac, key=operator.itemgetter(0))
            a=''
            ac=''
            for i in a_ac:
                a += ' '+i[0]
                ac += ' '+i[1]
            print '{}\t{}\t{}'.format(v,a,ac)

"""
memo:

最後の+=は効率悪い ↓みたいにする
ac_list = [("a","b"),("c","d")]
al,cl = zip(*ac_list)
print "".join(al)
print "".join(cl)

unixコマンド awk
"""

"""
$ python 47.py <neko.txt.cabocha
決心をする	 と を	 こうと 決心を
返報をする	 を んで	 返報を 偸んで
昼寝をする	 を	 昼寝を
昼寝をする	 が を	 彼が 昼寝を
迫害を加える	 て を	 追い廻して 迫害を
話をする	 を	 話を
投書をする	 て へ を	 やって ほととぎすへ 投書を
話をする	 に を	 時に 話を
写生をする	 を	 写生を
昼寝をする	 て を	 出て 昼寝を
彩色を見る	 を	 彩色を
欠伸をする	 から て て を	 なったから して 押し出して 欠伸を
挨拶をする	 を	 挨拶を
御馳走を食う	 と を	 見ると 御馳走を
問答をする	 を	 問答を
雑談をする	 ながら は を	 寝転びながら 黒は 雑談を
自慢をする	 を	 自慢を
思案を定める	 と は は を	 若くはないと 吾輩は 若くはないと 思案を
呼吸を飲み込む	 から て を	 なってから なってから 呼吸を
御馳走を食う	 を	 御馳走を
"""
