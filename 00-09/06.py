# 06
# -*- coding: utf-8 -*-

x = 'paraparaparadise'
y = 'paragraph'

def c_bigram(s):
	c_gram = []
	for i in range(len(s)):
		c_gram.append(s[i:i+2])
	return c_gram

X = set(c_bigram(x))
Y = set(c_bigram(y))

print 'X = ' + str(X)
print 'Y = ' + str(Y)
print 'X∪Y = ' +  str(X|Y)
print 'X∩Y = ' +  str(X&Y)
print 'X\Y = ' +  str(X-Y)
print "'se'∈X => " + str('se' in X)
print "'se'∈Y => " + str('se' in Y)
