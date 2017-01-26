# -*- coding: utf-8 -*-
"""49"""

"""
だめです
"""

import sys
from q40 import Morph, Chunk, cabocha_reader02, search_noun, make_chunk

def xy(data):
    for x,xchunk in enumerate(data):
        if search_noun(xchunk):
            xc = make_chunk(xchunk)
            #print '{}:{}'.format(x,xc)

            for y,ychunk in enumerate(data[x+1:], start=x+1):
                if search_noun(ychunk):
                    yc = make_chunk(ychunk)
                    #print '{}:{}'.format(y,yc)

                    if xc and yc:
                        print "X:[{}]{} -> Y:[{}]{}".format(x,xc,y,yc)

"""
                        x_list = []
                        y_list = []
                        jct = int()
                        i = xchunk.dst
                        while i:
                            if int(i) == int(y):
                                print 1
                                x_list.append(1)
                                i = False
                            elif data[int(i)].srcs:
                                print 2
                                jct = int(i)
                                if s_jct(data, y, jct):
                                    print 21
                                    y_list = make_y_list(data, y, jct)
                                    i = False
                                else:
                                    print 22
                                    i = data[int(i)].dst
                            else:
                                print 3
                                ic = make_chunk(data[int(i)])
                                x_list.append(ic)
                                i = data[int(i)].dst

                            print '{},{},{}'.format(x_list,y_list,jct)


def s_jct(data, y, jct):
    while int(y) != -1:
        y = data[int(y)].dst
        if y == jct:
            return True
        else:
            continue

def make_y_list(data, y, jct):
    y_list = []
    while y != jct:
        y_pass = make_chunk(data[int(y)])
        y_list.append(y_pass)
        y = data[int(y)].dst
    return y_list
"""



if __name__ == "__main__":
    for chunk_list in cabocha_reader02(sys.stdin):
        xy(chunk_list)
        print ''


"""
清野案：
パスの集合の一致をみる(包含関係、インターセクションおしゃれ！)

"""


"""
$ python 49.py <koneko.txt.cabocha
X:[1]吾輩は -> Y:[2]猫である

X:[0]どこで -> Y:[3]見当が

X:[0]何でも -> Y:[3]所で
X:[0]何でも -> Y:[4]ニャーニャー
X:[0]何でも -> Y:[6]いた事だけは
X:[0]何でも -> Y:[7]記憶している
X:[3]所で -> Y:[4]ニャーニャー
X:[3]所で -> Y:[6]いた事だけは
X:[3]所で -> Y:[7]記憶している
X:[4]ニャーニャー -> Y:[6]いた事だけは
X:[4]ニャーニャー -> Y:[7]記憶している
X:[6]いた事だけは -> Y:[7]記憶している

X:[0]吾輩は -> Y:[1]ここで
X:[0]吾輩は -> Y:[3]人間という
X:[0]吾輩は -> Y:[4]ものを
X:[1]ここで -> Y:[3]人間という
X:[1]ここで -> Y:[4]ものを
X:[3]人間という -> Y:[4]ものを

X:[1]あとで -> Y:[3]それは
X:[1]あとで -> Y:[4]書生という
X:[1]あとで -> Y:[5]人間中で
X:[1]あとで -> Y:[6]一番
"""
