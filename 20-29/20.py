# -*- coding: utf-8 -*-
"""20"""

import sys, json

def main():
	for line in sys.stdin:
		data = json.loads(line)
		if data["title"] == u'イギリス':
			print data["title"]
			print data["text"]	

# 21~のためにtxtファイルへ書き出し			
#			with open ('uk.txt', 'w') as f:
#				f.write(data["text"]+'\n') 
	
if __name__ == "__main__":
	main()
	
"""
$ python 20.py <jawiki-country.json
"""