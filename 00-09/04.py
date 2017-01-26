# 04
# -*- coding: utf-8 -*-

es = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'
es_list = es.split()
es_dict = {}
i = 1
for es in es_list:
	if i in [1, 5, 6, 7, 8, 9, 15, 16, 19]:
		es_dict[es[:1]] = i
	else:
		es_dict[es[:2]] = i
	i += 1
print es_dict

#連想
#print es_dict['K']

#原子番号順
#for key,value in sorted(es_dict.items(),key=lambda x:x[1]):
#	print key,value