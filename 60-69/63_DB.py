# -*- coding: utf-8 -*-
"""63_dB"""

import sys
import json, pickle
import plyvel

def main():
    db2 = plyvel.DB('./db2/', create_if_missing=True)
    for line in sys.stdin:
        artist = json.loads(line.strip())
        if "name" in artist:
            name = artist["name"]
            if "tags" in artist:
                tags = artist["tags"]
            else:
                tags = []
            db2.put(name.encode('utf-8'), pickle.dumps(tags))

if __name__ == '__main__':
    main()

"""
$ python 63_DB.py < artist.json
"""

"""
mongoDBは上書きされない，インスタンスが単純に増えてく
insertしまくるとidが違うだけの同じ情報がいっぱいに！注意
find_oneで持ってきて，あれば書き換え，なければ作成，にするのがよろしい
"""
