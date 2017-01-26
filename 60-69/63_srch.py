# -*- coding: utf-8 -*-
"""63_srch"""

import pickle
import plyvel

def main():
    db2 = plyvel.DB('./db2/')
    name = input('artist name > ')
    tags = pickle.loads(db2.get(name))
    if len(tags)>0:
        for tag in tags:
            print '{} ({})'.format(tag["value"], tag["count"])  # タグ名(被タグ数)
    else:
        print 'NO TAGS'

if __name__ == '__main__':
    main()

"""
$ python 63_srch.py
artist name > "西川貴教"
NO TAGS

$ python 63_srch.py
artist name > "Green Day"
pop-punk (1)
alternative rock (1)
american (3)
punk rock (3)
rock (3)
pop and chart (1)
pop punk (4)
pop/rock (1)
américain (1)
usa (2)
punk (2)
punk pop (1)
united states (1)
ska punk (1)
california (1)
california punk (1)
classic pop punk (1)
classic punk (1)
bay area (1)
bay area punk (1)
pop (2)
"""
