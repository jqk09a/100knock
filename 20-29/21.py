# -*- coding: utf-8 -*-
"""21"""

import sys, re

def main():
	m = re.compile(r'\[\[Category:.*\]\]')
	for line in sys.stdin:
		if m.match(line):
			print line,

if __name__ == "__main__":
	main()

"""
path:
$ python 20.py <jawiki-country.json | python 21.py
file:
$ python 21.py <uk.txt
result:
[[Category:イギリス|*]]
[[Category:英連邦王国|*]]
[[Category:G8加盟国]]
[[Category:欧州連合加盟国]]
[[Category:海洋国家]]
[[Category:君主国]]
[[Category:島国|くれいとふりてん]]
[[Category:1801年に設立された州・地域]]
"""