# -*- coding: utf-8 -*-
"""25"""

import sys, re, collections

def main():
	info_dic = collections.OrderedDict()	# 登録したkeyの順を保つ辞書
	m = re.compile(r'\|(.*?) = (.*)')		# テンプレート |(フィールド名) = (値) を探したい
	for line in sys.stdin:
		if line.startswith(u'{{基礎情報'):	# 基礎情報内のみを検索
			for info_line in sys.stdin:
				if info_line.startswith(u'}}'):
					break
				else:
					if m.match(info_line):
						key = m.match(info_line).group(1)	# フィールド名→key
						value = m.match(info_line).group(2)	# 値→value
						info_dic[key] = value				# として辞書に登録
			break
					
	for k,v in info_dic.iteritems():
		print '{} : {}'.format(k,v)
	
if __name__ == "__main__":
	main()

"""
$ python 25.py <uk.txt
result:
...
確立年月日3 : [[1801年]]
確立形態4 : 現在の国号「'''グレートブリテン及び北アイルランド連合王国'''」に変更
確立年月日4 : [[1927年]]
通貨 : [[スターリング・ポンド|UKポンド]] (&pound;)
通貨コード : GBP
時間帯 : ±0
夏時間 : +1
ISO 3166-1 : GB / GBR
ccTLD : [[.uk]] / [[.gb]]<ref>使用は.ukに比べ圧倒的少数。</ref>
国際電話番号 : 44
注記 : <references />
"""