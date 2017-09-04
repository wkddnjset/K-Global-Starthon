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
for b in en:
    if b.replace("\n",'') == '':
        continue
    else:
        data_en.append(b.replace("\n",''))


print(data_ko[0])
print(data_en[0])
for a in range(1, len(data_ko)):
    tu = Element("tu")

    tuv_ko = SubElement(tu, "tuv")
    tuv_ko.attrib["xml:lang"] = "ko"
    val_ko = data_ko[0]
    seg_ko = SubElement(tuv_ko, "seg").text = val_ko
    tuv_en = SubElement(tu, "tuv")
    tuv_en.attrib["xml:lang"] = "en"
    val_en = data_en[0]
    seg_en = SubElement(tuv_en, "seg").text = val_en

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
