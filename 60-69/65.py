# -*- coding: utf-8 -*-
"""65"""

import pymongo

def main():
    client = pymongo.MongoClient()
    db = client.monDB
    col = db.artist_data

    print col.find_one({u'name':"Queen"})

if __name__ == '__main__':
    main()

"""
$ python 65.py
{u'name': u'Queen', u'sort_name': u'Queen', u'ended': True, u'gid': u'5eecaf18-02ec-47af-a4f2-7831db373419', u'_id': ObjectId('576391a767780fe940d62568'), u'id': 992994}

MongoDBインタラクティブシェル
> use monDB
> db.artist_data.findOne({"name":"Queen"})
{
	"_id" : ObjectId("576391a767780fe940d62568"),
	"name" : "Queen",
	"sort_name" : "Queen",
	"ended" : true,
	"gid" : "5eecaf18-02ec-47af-a4f2-7831db373419",
	"id" : 992994
}
"""
