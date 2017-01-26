# -*- coding: utf-8 -*-
"""50"""

import sys, re

def main():
    for para in sys.stdin:
        for line in re.finditer(r'(.+?[.;:?!])\s+(?=[A-Z])?', para):    #(?= )肯定先読み
            print line.group(1)

if __name__ == "__main__":
    main()


"""
$ python 50.py < nlp.txt
Natural language processing (NLP) is a field of computer science, artificial intelligence, and linguistics concerned with the interactions between computers and human (natural) languages.
As such, NLP is related to the area of humani-computer interaction.
Many challenges in NLP involve natural language understanding, that is, enabling computers to derive meaning from human or natural language input, and others involve natural language generation.
The history of NLP generally starts in the 1950s, although work can be found from earlier periods.In 1950, Alan Turing published an article titled "Computing Machinery and Intelligence" which proposed what is now called the Turing test as a criterion
of intelligence.
"""
