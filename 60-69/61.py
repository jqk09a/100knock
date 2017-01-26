# -*- coding: utf-8 -*-
"""61"""

import plyvel

def main():
    db = plyvel.DB('./db/')
    name = input('artist name > ')
    print db.get(name)

if __name__ == '__main__':
    main()

"""
$ python 61.py
artist name > "西川貴教"
Japan

$ python 61.py
artist name > "ＮＨＫみんなのうた"
Japan

$ python 61.py
artist name > "Green Day"
United States

$ python 61.py
artist name > "Gustav Ruppke"
NO DATA
"""
