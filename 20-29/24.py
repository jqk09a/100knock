# -*- coding: utf-8 -*-
"""24"""

import sys, re

def main():
	m = re.compile(r'.*(ファイル|File):(.*?)\|')		# [[Category:(ほにゃらら) ] or | の
	for line in sys.stdin:
		if m.match(line):
			print m.match(line).group(2)		# (ほにゃらら)の部分を出力
	
if __name__ ==  "__main__":
	main()

"""
path:
$ python 20.py <jawiki-country.json | python 24.py
file:
$ python 22.py <uk.txt
result:
Royal Coat of Arms of the United Kingdom.svg
Battle of Waterloo 1815.PNG
The British Empire.png
Uk topo en.jpg
BenNevis2005.jpg
Elizabeth II greets NASA GSFC employees, May 8, 2007 edit.jpg
Palace of Westminster, London - Feb 2007.jpg
David Cameron and Barack Obama at the G20 Summit in Toronto.jpg
Soldiers Trooping the Colour, 16th June 2007.jpg
Scotland Parliament Holyrood.jpg
London.bankofengland.arp.jpg
...
"""
