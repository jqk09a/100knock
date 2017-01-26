# -*- coding: utf-8 -*-
"""28"""

import sys, re, collections

def main():					# フィールド名に対して値を一言でばしっと。簡潔に整形。
	info_dic = collections.OrderedDict()
	m1 = re.compile(r'<.*|\(.*|\（.*')		# 追加情報 <...>, (...) を探したい
	m2 = re.compile(r'(\{)*.*\||\}')			# 記事名|表示文字 の場合、表示文字 だけを表示
	for line in sys.stdin:
		key = line.split(' : ')[0]
		tmp_value = line.split(' : ')[1]
		value = m1.sub('',tmp_value)	# まずvalue内に追加情報があれば除去
		info_dic[key] = m2.sub('',value)	# 次に記事名があれば除去して、辞書に登録
					
	for k,v in info_dic.iteritems():
		print '{} : {}'.format(k,v),
	
if __name__ == "__main__":
	main()

"""
$ python 25.py <uk.txt | python 26.py | python 27.py | python 28.py
result:
略名 : イギリス
日本語国名 : グレートブリテン及び北アイルランド連合王国
公式国名 : {{lang|en|United Kingdom of Great Britain and Northern Ireland}}<ref>英語以外での正式国名:<br/>
国旗画像 : Flag of the United Kingdom.svg
国章画像 : ファイル:Royal Coat of Arms of the United Kingdom.svg|85px|イギリスの国章
国章リンク : イギリスの国章|国章
標語 : {{lang|fr|Dieu et mon droit}}<br/>フランス語:神と私の権利）
国歌 : 女王陛下万歳|神よ女王陛下を守り給え
位置画像 : Location_UK_EU_Europe_001.svg
公用語 : 英語（事実上）
首都 : ロンドン
最大都市 : ロンドン
元首等肩書 : イギリスの君主|女王
元首等氏名 : エリザベス2世
首相等肩書 : イギリスの首相|首相
首相等氏名 : デーヴィッド・キャメロン
面積順位 : 76
面積大きさ : 1 E11
面積値 : 244,820
水面積率 : 1.3%
...
"""