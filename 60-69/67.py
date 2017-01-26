# -*- coding: utf-8 -*-
"""67"""

import pymongo

def main():
    client = pymongo.MongoClient()
    db = client.monDB
    col = db.artist_data

    alias = input('alias > ')
    print col.find_one({u'aliases.name':alias}).get("name")
    #print col.find_one({u'aliases.name':alias})

if __name__ == '__main__':
    main()

"""
$ python 67.py
alias > "3MT"
Three Men and a Tenor
"""
