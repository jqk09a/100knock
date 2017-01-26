# 08
# -*- coding: utf-8 -*-

s = raw_input('Please input string > ')

def cipher(s):
	cip = ''
	for i in s:
		if 97 <= ord(i) <= 122:
			cip += chr(219-ord(i))
		else:
			cip += i
	return cip
	
print 'encryption : ' + cipher(s)
print 'decryption : ' + cipher(cipher(s))