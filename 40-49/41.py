# -*- coding: utf-8 -*-
"""41"""

import sys, collections
from q40 import Morph

class Chunk:
#    def __init__(self, morphs, dst, srcs):                             <-できなかった
#       self.morphs = morphs
#       self.chunk = "".join([morph.surface for morph in self.morphs])
#       self.dst = dst
#       self.srcs = srcs

    def __init__(self):
        self.morphs = []
#        self.chunk = "".join([morph.surface for morph in self.morphs])  <-できなかった
        self.dst = None
        self.srcs = []

    def __str__(self):
        return "[chunk:{}, dst:{}, srcs:{}]" \
                .format("".join([morph.surface for morph in self.morphs]), \
                        self.dst, \
                        self.srcs)

def cabocha_reader02(data):
    chunk = Chunk()
    chunk_list = []     # 1文分のchunkをいれとく
    morph_list = []     #吾輩,は,猫,で,ある,。
    srcs_dic = collections.defaultdict(set)
    for line in data:
        if line.startswith('*'):
            chunk.morphs = morph_list
            morph_list = []
            if chunk:
                chunk_list.append(chunk)    #次のchunkに行く前にlistに入れる
            chunk = Chunk()                 #新しくChunk
            l = line.split(' ')
            chunk.dst = l[2].strip('D')     #dstに係り受け先を入れる
            srcs_dic[l[2].strip('D')].add(int(l[1]))      #srcs_dic[chunk]=係り受け元
        elif line.startswith('EOS'):
            chunk.morphs = morph_list
            morph_list = []
            chunk_list.append(chunk)
            del chunk_list[0]
            for i in xrange(len(chunk_list)):           # 係り元をclassに入れたい
                chunk_list[i].srcs = list(srcs_dic[str(i)])
            yield chunk_list                            # 1文出来上がり
            srcs_dic = collections.defaultdict(set)     # 次に備える
            chunk = Chunk()
            chunk_list = []
        else:
            sur, other = line.split('\t')
            o = other.split(',')
            morph_list.append(Morph(sur, o[6], o[0], o[1]))


if __name__ == "__main__":
    for i, chunk_list in enumerate(cabocha_reader02(sys.stdin), start=1):
        #if i==13:
            for j, chunk in enumerate(chunk_list):
                print '[{}]:{}'.format(j,chunk)
            print ''



# chunk = Chunk → 取れたところからchunk.morph.append=~みたいにすればいいのか？

#係り受けのところdefaultdict使える？使える！！！！
#>>> s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
#>>> d = defaultdict(list)
#>>> for k, v in s:
#...     d[k].append(v)
#...
#>>> d.items()
#[('blue', [2, 4]), ('red', [1]), ('yellow', [1, 3])]

#分からん〜〜〜〜〜
#morphに入ってるのはわかってるんだ、さあ出てこい
# →Chunk作った時点で各self出来上がってる(Morph空のまま)

"""
$ python 41.py < neko.txt.cabocha
[0]:[chunk:吾輩は, dst:5, srcs:[]]
[1]:[chunk:ここで, dst:2, srcs:[]]
[2]:[chunk:始めて, dst:3, srcs:[1]]
[3]:[chunk:人間という, dst:4, srcs:[2]]
[4]:[chunk:ものを, dst:5, srcs:[3]]
[5]:[chunk:見た。, dst:-1, srcs:[0, 4]]
"""
