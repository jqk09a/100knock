# -*- coding: utf-8 -*-
"""22"""

import sys, re

def main():
	m = re.compile(r'\[\[Category:(.*?)[]|]')		# [[Category:(ほにゃらら) ] or | の
	for line in sys.stdin:
		if m.match(line):
			print m.match(line).group(1)		# (ほにゃらら)の部分を出力
	
if __name__ ==  "__main__":
	main()

"""
path:
$ python 20.py <jawiki-country.json | python 22.py
file:
$ python 22.py <uk.txt
result:
イギリス
英連邦王国
G8加盟国
欧州連合加盟国
海洋国家
君主国
島国
1801年に設立された州・地域
"""
