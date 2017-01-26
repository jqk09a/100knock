# -*- coding: utf-8 -*-
"""91"""

#fi="work/100/questions-words

import sys

def main():
    section_name= ''
    for line in sys.stdin:
        line = line.strip()
        if line[0]==':':
            section_name = line[2:]
        elif section_name=='family':
            print line
            
if __name__ == '__main__':
    main()
