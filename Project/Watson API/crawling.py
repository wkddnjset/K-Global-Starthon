# -*- coding: utf-8 -*-

import requests
import nltk.data
import numpy as np
from bs4 import BeautifulSoup

for i in range(1, 13):
    pg_num = str(i)
    pg_url = 'http://www.dbpia.co.kr/SearchResult/Search?q=%28%5B%EB%94%A5%EB%9F%AC%EB%8B%9D%C2%A7coldb%C2%A72%C2%A751%C2%A73%5D%29&searchWord=%EC%A0%84%EC%B2%B4%3D%5E%24%EB%94%A5%EB%9F%AC%EB%8B%9D%5E*&Collection=0&nSort=1&nSorttype=desc&Page='+pg_num+'&nPagesize=20&searchAll=%EB%94%A5%EB%9F%AC%EB%8B%9D&Multimedia=0&specificParam=0&isFullText=0'
    pg_html = requests.get(pg_url).text
    pg_soup = BeautifulSoup(pg_html, 'html.parser')
    a = pg_soup.select('.result_list_info .value')
    node_all=[]
    for b in a:
        c = b.get('onclick').encode('utf8')
        node_all.append(c[99:-3])

    node_id = np.unique(node_all)
    print(node_id)
    for i in range(0, len(node_id)):

        url = 'http://www.dbpia.co.kr/Journal/ArticleDetail/'+node_id[i]+'?TotalCount=251&Seq=1&q=%5B%EB%94%A5%EB%9F%AC%EB%8B%9D%C2%A7coldb%C2%A72%C2%A751%C2%A73%5D&searchWord=%EC%A0%84%EC%B2%B4%3D%5E%24%EB%94%A5%EB%9F%AC%EB%8B%9D%5E*&Multimedia=0&isIdentifyAuthor=0&Collection=0&SearchAll=%EB%94%A5%EB%9F%AC%EB%8B%9D&isFullText=0&specificParam=0&SearchMethod=0&Sort=1&SortType=desc&Page=1&PageSize=20'
        html = requests.get(url).text
        soup = BeautifulSoup(html, 'html.parser')
        li_data = soup.select('#detail_tab_panel .con_txt', limit=1)


        try:
            for data in li_data:
                all = data.text
                ko = all.split('\r')[1]
                en = all.split('\r')[2]
                tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
                ko_sentence =  '\n\n'.join(tokenizer.tokenize(ko))
                en_sentence = '\n\n'.join(tokenizer.tokenize(en))
            print (li_data)
            korean = ko_sentence.encode('utf8')
            english = en_sentence.encode('utf8')

            f = open("C:/jangwon/project/K-Global project/Project/Watson API/tmx/test_ko.txt", 'a')
            data = korean
            f.write(data)
            f.write("\n")
            f.close()

            f = open("C:/jangwon/project/K-Global project/Project/Watson API/tmx/test_en.txt", 'a')
            data = en_sentence
            f.write(data)
            f.write('\n')
            f.close()
        except:
            continue
