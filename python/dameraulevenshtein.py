#!/usr/bin/env python
#-*- coding:utf-8 -*-

def damerau_levenshtein_distance(a, b):
    '''
    2つの文字列間のDamerau-Levenshtein距離を計算します
    
    @param a: unicode    対象文字列
    @param b: unicode    比較文字列
    @return: int
    '''
    m = [[0] * (len(b) + 1) for i in range(len(a) + 1)]

    for i in xrange(len(a) + 1):
        m[i][0] = i

    for j in xrange(len(b) + 1):
        m[0][j] = j

    for i in xrange(1, len(a) + 1):
        for j in xrange(1, len(b) + 1):
            if a[i-1] == b[j-1]:
                x = 0
            else:
                x = 1
            m[i][j] = min(m[i-1][j] + 1, m[i][j-1] + 1, m[i-1][j-1] + x)
            if i > 1 and j > 1 and a[i-1] == b[j-2] and [i-2] == b[j-1]:
                m[i][j] = min(m[i][j], m[i-2][j-2] + x)
            
    return m[-1][-1]

def main():
    print damerau_levenshtein_distance("abc", "cba")
    
if __name__ == "__main__":
    main()
    