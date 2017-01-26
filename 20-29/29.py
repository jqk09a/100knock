# -*- coding: utf-8 -*-
"""29"""

import sys, urllib, json
	
def main():
	info_dic = dict()							# 28.pyの出力を受け取って辞書へ
	for line in sys.stdin:
		key = line.split(' : ')[0]
		value = line.split(' : ')[1]
		info_dic[unicode(key)] = unicode(value)

	params = urllib.urlencode({					# 各値を設定
			'action':'query',
			'format':'json',
			'titles':'File:'+info_dic[u'国旗画像'],
			'prop':'imageinfo',
			'iiprop':'url'
	})
	url = urllib.urlopen("http://ja.wikipedia.org/w/api.php?"+params)
	data = json.loads(url.read())
	print data
	print data["query"]["pages"]["-1"]["imageinfo"][0]["url"]	# 該当箇所を出力
	
if __name__ == "__main__":
	main()

"""
API叩く
urlencode:マップ型
"""	
"""
$ python 25.py <uk.txt | python 26.py | python 27.py | python 28.py | python 29.py
result:
https://upload.wikimedia.org/wikipedia/commons/a/ae/Flag_of_the_United_Kingdom.svg
"""