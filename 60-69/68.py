# -*- coding: utf-8 -*-
"""68"""

import pymongo

def main():
    client = pymongo.MongoClient()
    db = client.monDB
    col = db.artist_data

    artists = col.find({u'tags.value':"dance"}).sort('rating.count',pymongo.DESCENDING).limit(10)
    for i,artist in enumerate(artists, start=1):
        print '{}\t{}\t{}'.format(i, artist.get('rating').get('count'), artist.get('name'))
        # 順位，投票数，アーティスト名 をタブ区切りで表示

if __name__ == '__main__':
    main()

"""
$ python 68.py
1       26      Madonna
2       23      Björk
3       23      The Prodigy
4       15      Rihanna
5       13      Britney Spears
6       11      Maroon 5
7       7       Adam Lambert
8       7       Fatboy Slim
9       6       Basement Jaxx
10      5       Cornershop
"""
