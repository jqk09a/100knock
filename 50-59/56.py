# -*- coding: utf-8 -*-
"""56"""

import sys, re
from lxml import etree

def main():
    root = etree.parse(sys.stdin)
    coref_list = make_coref_list(root)          #共参照の情報
    sentence_list = make_sentence_list(root)    #文
    for i in coref_list:
        #print '{}：{}：{}'.format(i[0],i[1],i[2])
        sentence_list[int(i[0])-1] = re.sub(i[2], '「{}({})」'.format(i[2],i[1]), sentence_list[int(i[0])-1])
    for s in sentence_list:
        print s

def make_coref_list(root):
    coref_list = []
    for coreference in root.xpath('.//coreference/coreference'):
        rep = coreference.xpath('./mention[@representative="true"]/text')[0].text
        for mention in coreference.xpath('./mention[not(@representative="true")]'):
            snt = mention.find('sentence').text
            txt = mention.find('text').text
            coref_list.append([snt, txt, rep])   #[sentence番号, 参照表現, 代表参照表現]
    return coref_list

def make_sentence_list(root):
    sentence_list = []
    for sentence in root.xpath('//sentences/sentence'):
        words = sentence.xpath('.//word')
        s = ' '.join(word.text for word in words)
        sentence_list.append(s)
    return sentence_list


if __name__ == "__main__":
    main()

"""
共参照：↗↖(こういうやつ by塙)

$ python 56.py < nlp.txt.out
Natural language processing From Wikipedia , 「the free encyclopedia Natural language processing -
LRB- NLP -RRB-(a field of computer science)」 isa field of computer science , artificial intellig
ence , and linguistics concerned with the interactions between computers and human -LRB- natural -
RRB- languages .
As such , NLP is related to the area of humani-computer interaction .
Many challenges in NLP involve natural language understanding , that is , enabling 「computers(com
puters)」 to derive meaning from human or natural language input , and others involve natural lang
uage generation .
History The history of NLP generally starts in the 1950s , although work can be found from earlier
 periods .
In 1950 , 「Alan Turing(Turing)」 published an article titled `` Computing Machinery and Intellige
nce '' which proposed what is now called the Turing test as a criterion of intelligence .
"""
