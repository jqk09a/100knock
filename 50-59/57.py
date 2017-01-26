# -*- coding: utf-8 -*-
"""57"""

import sys
from graphviz import Digraph
from lxml import etree

def make_list(data):
    root = etree.parse(data)
    dependencies = root.xpath('//dependencies[@type="collapsed-dependencies"]')
    a_list = []
    for dependency in dependencies:
        d_list = []
        for dep in dependency.xpath('./dep'):
            d_list.append([dep.find('governor').text, dep.find('dependent').text])
        a_list.append(d_list)
    return a_list

def make_fig(d_list):
    G = Digraph('graph', filename='57.gv')
    G.attr('node', shape='circle')
    for d in d_list:
        G.edge(d[0],d[1])
    G.view()

if __name__ == "__main__":
    for i,d_list in enumerate(make_list(sys.stdin), start=1):
        if i == 50:             # 最後の行
            make_fig(d_list)


"""
$ python 57.py < nlp.txt.out
http://www.cl.ecei.tohoku.ac.jp/~reina.a/nlp100/57.gv.pdf

## idを指定しましょう．
"""
