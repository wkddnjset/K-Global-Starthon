# -*- coding: utf-8 -*-

import requests
import nltk.data
import numpy as np
from bs4 import BeautifulSoup

for i in range(1, 100):
    print(i,'time')
    pg_num = str(i)
    pg_url = 'http://endic.naver.com/search_example.nhn?sLn=kr&m=example&query=&tab=2&fieldType=3&themeId=1&degreeType=0&levelId=1&sortType=1&pageNo='+pg_num
    pg_html = requests.get(pg_url).text
    pg_soup = BeautifulSoup(pg_html, 'html.parser')
    en = pg_soup.select('.fnt_e09 span')
    ko = pg_soup.select('.mar_top1')
    for en_li in en:
        result_en = en_li.text.encode('utf8')
        f = open("C:/jangwon/project/K-Global project/Project/Watson API/tmx_test/test_en.txt", 'a')
        data = result_en
        f.write(data)
        f.write("\r\n")
        f.close()
        print(result_en)

    for ko_li in ko:
        result_ko = ko_li.text.encode('utf8')
        print(result_ko)
        f = open("C:/jangwon/project/K-Global project/Project/Watson API/tmx_test/test_ko.txt", 'a')
        data = result_ko
        f.write(data)
        f.write('\r\n')
        f.close()




