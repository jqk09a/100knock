# -*- coding: utf-8 -*-
"""53"""

import sys
from lxml import etree

def main():
    root = etree.parse(sys.stdin)
    words = root.xpath('//word')
    for word in words:
        print word.text

if __name__ == "__main__":
    main()


"""
▶ xmlファイルの作成
$ java -cp "*" -Xmx2g edu.stanford.nlp.pipeline.StanfordCoreNLP -annotators tokenize,ssplit,pos,lemma,ner,parse,dcoref -file ~/Desktop/100/nlp.txt
$ less nlp.txt.out
<?xml version="1.0" encoding="UTF-8"?>
<?xml-stylesheet href="CoreNLP-to-HTML.xsl" type="text/xsl"?>
<root>
  <document>
    <sentences>
      <sentence id="1">
        <tokens>
        ...

▶ 1行1単語
$ python 53.py < nlp.txt.out
Natural
language
processing
From
Wikipedia
,
the
free
encyclopedia
Natural
language
processing
-LRB-
NLP
-RRB-
is
a
...
"""
