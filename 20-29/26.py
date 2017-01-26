# -*- coding: utf-8 -*-
"""26"""

import sys, re, collections

def main():							# pathにより辞書を入力として受け取る
	info_dic = collections.OrderedDict()
	m = re.compile(r'\'\'+')				# 強調マークアップ ' x複数個 を探したい
	for line in sys.stdin:
		key = line.split(' : ')[0]
		value = line.split(' : ')[1]
		info_dic[key] = m.sub('',value)	# valueに該当箇所があれば除去し、辞書に登録
					
	for k,v in info_dic.iteritems():
		print '{} : {}'.format(k,v),
	
if __name__ == "__main__":
	main()

"""
$ python 25.py <uk.txt | python 26.py
result:
...
確立年月日3 : [[1801年]]
確立形態4 : 現在の国号「グレートブリテン及び北アイルランド連合王国」に変更
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
