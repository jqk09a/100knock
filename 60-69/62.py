# -*- coding: utf-8 -*-
"""62"""

import collections
import plyvel

def main():
    db = plyvel.DB('./db/')
    cnt = collections.Counter(v for k,v in db)
    #print cnt.most_common(5)
    print cnt["Japan"]

if __name__ == '__main__':
    main()

"""
$ python 62.py
21946
"""
