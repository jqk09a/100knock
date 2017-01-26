# -*- coding: utf-8 -*-
"""23"""

import sys, re

def main():
	m = re.compile(r'=(=+)\s*(.*?)(==+)')
	for line in sys.stdin:
		if m.match(line):
			level = len(m.match(line).group(1))
			section = m.match(line).group(2)
			print '{} : level {}'.format(section,level)
	
if __name__ == "__main__":
	main()
	
"""
path:
$ python 20.py <jawiki-country.json | python 23.py
file:
$ python 23.py <uk.txt
result:
国名 : level 1
歴史 : level 1
地理 : level 1
気候 : level 2
政治 : level 1
外交と軍事 : level 1
地方行政区分 : level 1
主要都市 : level 2
科学技術 : level 1
経済 : level 1
鉱業 : level 2
...
"""