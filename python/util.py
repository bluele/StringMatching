#!/usr/bin/env python
#-*- coding:utf-8 -*-

import re

# 除外文字列の集合
exclude_words = set()

def split_space(text):
    '''
    指定したテキストから単語を抽出します
    
    @param text: unicode
    @return: iter
    '''
    words = re.split(u"\s+", text.strip())
    for word in words:
        if word not in exclude_words:
            yield word
            
def ngram(text, n=2):
    '''
    指定したテキストをNgramで分解します
    
    @param text: unicode
    '''
    cur = 0
    while(len(text) >= cur + n):
        yield text[cur:n+cur]
        cur += 1
    