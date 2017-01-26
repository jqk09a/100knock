# 05
# -*- coding: utf-8 -*-

#terminal入力
#s = raw_input('Please input string > ')
#n = input('Please input n > ')

s = 'I am an NLPer'
n = 2

def w_n_gram(s,n):
	w_list = s.split( )
	w_gram = []
	for i in range(len(w_list)):
		w_gram.append(w_list[i:i+n])
	return w_gram
	
def c_n_gram(s,n):
	c_gram = []
	for i in range(len(s)):
		c_gram.append(s[i:i+n])
	return c_gram
	
print 'word_' + str(n) +'-gram:' 
print w_n_gram(s,n)
print 'character_' + str(n) +'-gram:' 
print c_n_gram(s,n)