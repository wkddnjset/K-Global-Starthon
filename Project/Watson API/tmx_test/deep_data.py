# -*- coding: utf-8 -*-
import json
import io, sys
import nltk

file_ko = 'test_ko.txt'
file_en = 'test_en.txt'
ko = open(file_ko).readlines()
en = open(file_en).readlines()
data_ko = []
for t in ko:
    if t.replace("\n",'') == '':
        continue
    else:
        data_ko.append(t.replace("\n",''))

data_en = []
for i in en:
    if i.replace("\n",'') == '':
        continue
    else:
        data_en.append(i.replace("\n",''))

print(data_en[1])

