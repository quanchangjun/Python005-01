#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:My
@file:answer_zhihu2.py
@time:2020/12/06
"""

import requests
from lxml import etree


def getAnswer(myurl, header):
    response = requests.get(myurl, headers=header)
    selector = etree.HTML(response.text)
    match_answer = '//div[@class="RichContent RichContent--unescapable"]/div/span/p/text()'
    answer_chunk = selector.xpath(match_answer)
    return answer_chunk, response.status_code


def writeFile(filename, answerList):
    with open(filename, 'w+', encoding='utf-8') as f:
        for line in answerList:
            f.write(line)


if __name__ == '__main__':
    myurl = 'https://www.zhihu.com/question/300985609/answer/1289872051'
    ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 ' \
         'Safari/537.36 '
    header = {'user-agent': ua}
    answer, repStatus = getAnswer(myurl, header)
    if repStatus != 200:
        print('not success')
    writeFile('answer.results2', answerList=answer)
