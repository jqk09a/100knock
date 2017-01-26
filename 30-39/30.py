# -*- coding: utf-8 -*-
"""30"""

import sys

def mecab_reader(data):
	morph_list = []						# 各行ごと
	for line in data:
		if line.startswith('EOS'):
			yield morph_list				# yield よく分かってないが使用
			morph_list = []				# yieldに到達→morph_listの内容をif__name__...のmorph_listに渡す
		else:
			surface, other = line.split('\t')
			o = other.split(',')
			morph_list.append({			# 各語ごとに辞書を作ったものを1要素としてmorph_list へ追加
				'surface':surface,
				'base':o[6],
				'pos':o[0],
				'pos1':o[1]
			})	

if __name__ == "__main__":
	print '-'*40
	print '表層形\t基本形\t品詞\t品詞分類1'
	print '-'*40
	for morph_list in mecab_reader(sys.stdin):
		print ''
		for word in morph_list:
			print '{surface}\t{base}\t{pos}\t{pos1}'.format(**word)	#キーワード引数にdict型、**でアンパックして使用

"""
$ python 30.py <neko.txt.mecab

----------------------------------------
表層形	基本形	品詞	品詞分類1
----------------------------------------

一	一	名詞	数


　	　	記号	空白
吾輩	吾輩	名詞	代名詞
は	は	助詞	係助詞
猫	猫	名詞	一般
で	だ	助動詞	*
ある	ある	助動詞	*
。	。	記号	句点

名前	名前	名詞	一般
は	は	助詞	係助詞
まだ	まだ	副詞	助詞類接続
無い	無い	形容詞	自立
。	。	記号	句点
...
"""