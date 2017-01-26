# -*- coding: utf-8 -*-
"""64"""

import sys
import json
import pymongo

def main():
    client = pymongo.MongoClient()
    db = client.monDB
    col = db.artist_data
    for artist in sys.stdin:
        col.insert(json.loads(artist.strip()))

    col.create_index([(u'name', pymongo.ASCENDING),
                      (u'aliases.name', pymongo.ASCENDING),
                      (u'tag.value', pymongo.ASCENDING),
                      (u'rating.value', pymongo.ASCENDING)])

if __name__ == '__main__':
    main()

"""
$ python 64.py < artist.json

▶ 使い方 (自信なし、""とりあえず""動いてる模様)
$ mongod --config /usr/local/etc/mongod.conf
$ mongo (別シェルで)

▶ 使い方 (教えてもらった)
$ mongod -dbpath data #homeの下のdataに入ってる
$ mongo (別シェル)

https://api.mongodb.com/python/current/
"""
