# -*- coding: utf-8 -*-
"""97"""

import sys
import cPickle
from collections import defaultdict
from itertools import groupby
from sklearn.cluster import KMeans

def main():
    names, vecs = cPickle.load(open('country_vec.pkl', 'r'))
    kmeans = KMeans(n_clusters=5).fit(vecs)
    labels = kmeans.labels_
    cPickle.dump((names,vecs,labels),open('country_vec_label.kmeans.pkl', 'w'))
    country_label = zip(labels,names)
    for k,v in groupby(sorted(country_label), lambda x: x[0]):
        print 'cluster {}:'.format(k)
        for vi in v:
            print '  {}'.format(vi[1])

if __name__ == '__main__':
    main()

"""
cluster 0:
  Australia
  Bangladesh
  Canada
  China
  Ghana
  India
  Indonesia
  Japan
  Kenya
  Malaysia
  Nepal
  New_Zealand
  Nigeria
  Pakistan
  Saudi_Arabia
  Singapore
  South_Africa
  South_Korea
  Sri_Lanka
  Tanzania
  Thailand
  Uganda
  Zimbabwe
cluster 1:
  Albania
  Armenia
  Austria
  Belarus
  Belgium
  Bulgaria
  Croatia
  Cyprus
  Czech_Republic
  Denmark
  Estonia
  Finland
  France
  Germany
  Greece
  Hungary
  Iceland
  Ireland
  Italy
  Latvia
  Lithuania
  Luxembourg
  Malta
  Monaco
  Montenegro
  Netherlands
  Norway
  Poland
  Portugal
  Romania
  Russia
  Serbia
  Slovakia
  Slovenia
  Spain
  Sweden
  Switzerland
  Turkey
  Ukraine
  United_Kingdom
cluster 2:
  Argentina
  Bolivia
  Brazil
  Chile
  Colombia
  Costa_Rica
  Cuba
  Dominican_Republic
  Ecuador
  El_Salvador
  Guatemala
  Haiti
  Honduras
  Jamaica
  Mexico
  Nicaragua
  Panama
  Paraguay
  Peru
  Philippines
  Puerto_Rico
  United_States
  Uruguay
  Venezuela
cluster 3:
  Afghanistan
  Algeria
  Angola
  Cambodia
  Egypt
  Ethiopia
  Fiji
  Iran
  Iraq
  Israel
  Kosovo
  Laos
  Lebanon
  Libya
  Macedonia
  North_Korea
  Somalia
  Sudan
  Syria
  Taiwan
  Vietnam
cluster 4:
  American_Samoa
  Andorra
  Antarctica
  Azerbaijan
  Bahamas
  Bahrain
  Barbados
  Belize
  Benin
  Bermuda
  Bhutan
  Botswana
  British_Virgin_Islands
  Brunei
  Burkina_Faso
  Burundi
  Cameroon
  Canary_Islands
  Cape_Verde
  Cayman_Islands
  Central_African_Republic
  Chad
  Christmas_Island
  Comoros
  Cook_Islands
  Curaçao
  Diego_Garcia
  Djibouti
  Dominica
  Equatorial_Guinea
  Eritrea
  Falkland_Islands
  Faroe_Islands
  French_Guiana
  French_Polynesia
  Gabon
  Gambia
  Georgia
  Gibraltar
  Greenland
  Grenada
  Guadeloupe
  Guam
  Guernsey
  Guinea
  Guinea-Bissau
  Guyana
  Isle_of_Man
  Jersey
  Jordan
  Kazakhstan
  Kiribati
  Kuwait
  Kyrgyzstan
  Lesotho
  Liberia
  Liechtenstein
  Madagascar
  Malawi
  Maldives
  Mali
  Marshall_Islands
  Martinique
  Mauritania
  Mauritius
  Mayotte
  Micronesia
  Moldova
  Mongolia
  Morocco
  Mozambique
  Namibia
  Nauru
  New_Caledonia
  Niger
  Niue
  Norfolk_Island
  Northern_Mariana_Islands
  Oman
  Palau
  Palestinian_Territories
  Papua_New_Guinea
  Qatar
  Rwanda
  Réunion
  Samoa
  San_Marino
  Senegal
  Seychelles
  Sierra_Leone
  Solomon_Islands
  South_Sudan
  Suriname
  Swaziland
  Tajikistan
  Timor-Leste
  Togo
  Tokelau
  Tonga
  Tunisia
  Turkmenistan
  Tuvalu
  United_Arab_Emirates
  Uzbekistan
  Vanuatu
  Vatican_City
  Western_Sahara
  Yemen
  Zambia
"""
