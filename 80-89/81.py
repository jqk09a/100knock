# -*- coding: utf-8 -*-
"""
81
rerefer to https://github.com/umpirsky/country-list
"""

import sys, json, re

def main():
    with open('country.json', 'r') as f:
        countries = [v for v in json.load(f).values() if ' ' in v]
        count_names = re.compile('|'.join(countries))
    for line in sys.stdin:
        for m in count_names.finditer(line):
            count_name = m.group(0)
            line = line.replace(count_name, count_name.replace(' ', '_'))
        print line,

if __name__ == '__main__':
    main()
