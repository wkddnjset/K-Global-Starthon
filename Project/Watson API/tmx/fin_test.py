# -*- coding: utf-8 -*-
import json
import io, sys
import nltk
import xml.etree.cElementTree as ET
from xml.etree.ElementTree import Element, SubElement, dump, ElementTree

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


print(data_ko[1])
for i in range(1, len(data_ko)):
    tu = Element("tu")


    tuv_ko = SubElement(tu, "tuv")
    tuv_ko.attrib["xml:lang"] = "ko"
    seg_ko = SubElement(tuv_ko, "seg")
    # ko_val = map(str,data_ko[i])
    ko_val = (data_ko[i])
    seg_ko.text = ko_val

    tuv_en = SubElement(tu, "tuv")
    tuv_en.attrib["xml:lang"] = "en"
    seg_en = SubElement(tuv_en, "seg")
    # en_val = map(str, data_en[i])
    seg_en.text = data_en[i].decode("utf8")

    def indent(elem, level=0):
        i = "\n" + level*"  "
        if len(elem):
            if not elem.text or not elem.text.strip():
                elem.text = i + "  "
            if not elem.tail or not elem.tail.strip():
                elem.tail = i
            for elem in elem:
                indent(elem, level+1)
            if not elem.tail or not elem.tail.strip():
                elem.tail = i
        else:
            if level and (not elem.tail or not elem.tail.strip()):
                elem.tail = i

    indent(tu)
    dump(tu)
