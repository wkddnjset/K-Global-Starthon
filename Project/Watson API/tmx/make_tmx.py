from xml.etree.ElementTree import Element, SubElement, dump, ElementTree

for i in range(0,2):
    tu = Element("tu")


    tuv_ko = SubElement(tu, "tuv")
    tuv_ko.attrib["xml:lang"] = "ko"
    seg_ko = SubElement(tuv_ko, "seg").text = '12'

    tuv_en = SubElement(tu, "tuv")
    tuv_en.attrib["xml:lang"] = "en"
    seg_en = SubElement(tuv_en, "seg").text = '23'


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