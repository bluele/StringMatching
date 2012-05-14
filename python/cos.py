#!/usr/bin/env python
#-*- coding:utf-8 -*-
from __future__ import division
from util import ngram, split_space
import math

def cosine_similarity(vector_a, vector_b):
    '''
    指定した２つのベクトルのコサイン類似度を算出します
    
    @param vector_a: dict    対象の特徴ベクトル
    @param vector_b: dict    対象の特徴ベクトル
    @return: float
    '''
    return inner_product(vector_a, vector_b) / (vector_abs(vector_a) * vector_abs(vector_b))
    
def inner_product(vector_a, vector_b):
    '''
    指定した２つのベクトルの内積を計算します
    
    @param vector_a: dict    対象の特徴ベクトル
    @param vector_b: dict    対象の特徴ベクトル
    @return: float
    '''
    val = 0
    for word in vector_a.iterkeys():
        if word in vector_a and word in vector_b:
            val += vector_a[word] * vector_b[word]
    return val
    
def vector_abs(vector):
    '''
    指定したベクトルの大きさを計算します
    
    @param vector: dict    対象の特徴ベクトル
    @return: sqrt
    '''
    size = 0
    for val in vector.itervalues():
        size += val * val
    return math.sqrt(size)


class Recommend():
    
    def __init__(self, get_features=ngram):
        self.terms = dict()
        self.get_features = get_features
        
    def make_vector(self, value):
        '''
        指定したテキストから特徴ベクトルを生成します
        
        @param value: unicode
        @return: dict
        '''
        terms = dict()
        for word in self.get_features(value):
            terms.setdefault(word, 0)
            terms[word] += 1
        return terms
    
    def add(self, key, value):
        '''
        指定したテキストを追加します
        
        @param key: unicode
        @param value: unicode
        '''
        if not isinstance(value, unicode):
            value = unicode(value)
        for word in self.get_features(value):
            self.terms.setdefault(key, dict()).setdefault(word, 0)
            self.terms[key][word] += 1
        
    def search(self, text, max_num=10):
        '''
        指定したテキストに類似するテキストを取得します
        
        @param text: unicode
        @param max_num: int
        @return: list
        '''
        if not isinstance(text, unicode):
            text = unicode(text)
        results = list()
        terms = self.make_vector(text)
        # 各ベクトルについて算出し、上位N件取得
        for key, vector in self.terms.iteritems():
            score = cosine_similarity(terms, vector)
            results.append((key, score))
        return sorted(results, cmp=lambda x,y:cmp(y[1], x[1]))[:max_num]
    

def main():
    rec = Recommend(get_features=lambda x:ngram(x, n=1))
    rec.add("one", u"数値文字列を数値としての大小で並び替えるには")
    rec.add("two", u"数値なら値の小さい順に並び替えます")
    print rec.search(u"文字列を数値にしたいという話")

if __name__ == "__main__":
    main()
    