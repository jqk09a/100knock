# 03
# -*- coding: utf-8 -*-

pi = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'
word_list = (pi.replace(',', '').replace('.', '')).split()
count_list = [len(word) for word in word_list]
print count_list
