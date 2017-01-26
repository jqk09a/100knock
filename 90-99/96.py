# -*- coding: utf-8 -*-
"""96"""

import sys
import json
import cPickle
import numpy as np
from gensim.models import word2vec

def country_name():
    countries = []
    with open('country.json', 'r') as fi:
        for v in json.load(fi).values():
            v = v.replace(' ', '_')
            countries.append(v)
    return countries

def main(countries):
    model = word2vec.Word2Vec.load('w2v.model')
    countries_D = dict()
    for c in countries:
        try:
            countries_D[c] = model[c]
            # fo.write('{}: {}\n'.format(c,model[c])) -> country.vec
        except:
            continue
    cPickle.dump((countries_D.keys(), np.array(countries_D.values())), open('country_vec.pkl','w'))

if __name__ == '__main__':
    countries = country_name()
    main(countries)
