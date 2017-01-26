# -*- coding: utf-8 -*-
"""60"""

import sys
import json
import plyvel

def main():
    db = plyvel.DB('./db/', create_if_missing=True)
    for line in sys.stdin:
        artist = json.loads(line.strip())
        if "name" in artist:
            name = artist["name"]
            if "area" in artist:
                area = artist["area"]
            else:
                area = 'NO DATA'    #nameはあるがareaに関するデータが記述されてないもの
            db.put(name.encode('utf-8'), area.encode('utf-8'))

if __name__ == '__main__':
    main()

"""
$ python 60.py < artist.json
"""
