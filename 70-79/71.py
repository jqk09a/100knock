# -*- coding: utf-8 -*-
"""71"""

import sys

# stop word list に含まれているか否かを判定する関数
def main():
    tar = raw_input('> ').lower()
    with open('stoplist.txt', 'r') as f:
        stoplist = [word.rstrip() for word in f]
        print tar in stoplist

if __name__ == '__main__':
    main()


"""
今回のstop word listとして，これを利用(引用)．571語．
SMART stop list [G. Salton: The SMART retrieval system. Prentice-Hall, 1971]
http://jmlr.csail.mit.edu/papers/volume5/lewis04a/a11-smart-stop-list/english.stop

$  python 71.py
> he
True
$  python 71.py
> and
True
$  python 71.py
> game
False
$  python 71.py
> girl
False
"""
