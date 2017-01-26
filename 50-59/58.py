# -*- coding: utf-8 -*-
"""58"""

import sys
from lxml import etree

def main():
    root = etree.parse(sys.stdin)
    dependencies = root.xpath('//dependencies[@type="collapsed-dependencies"]')
    for dependency in dependencies:
        for nsubj in dependency.xpath('./dep[@type="nsubj"]'):
            s_text = nsubj.find('dependent').text
            v_text = nsubj.find('governor').text
            v_idx = nsubj.find('governor').get('idx')
            dobj = dependency.xpath('./dep[@type="dobj"][./governor[@idx="{}"]]'.format(v_idx))
            for o in dobj:
                o_text = o.find('dependent').text
                print '{}\t{}\t{}'.format(s_text, v_text, o_text)

if __name__ == "__main__":
    main()


"""
$ python 57.py < nlp.txt.out
understanding   enabling        computers
others  involve generation
Turing  published       article
experiment      involved        translation
ELIZA   provided        interaction
patient exceeded        base
ELIZA   provide response
which   structured      information
underpinnings   discouraged     sort
that    underlies       approach
Some    produced        systems
which   make    decisions
systems rely    which
that    contains        errors
implementations involved        coding
algorithms      take    set
Some    produced        systems
which   make    decisions
models  have    advantage
they    express certainty
Systems have    advantages
Automatic       make    use
that    make    decisions
"""
