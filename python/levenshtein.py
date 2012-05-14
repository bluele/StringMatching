#!/usr/bin/env python
#-*- coding:utf-8 -*-

def levenshtein_distance(a, b):
    '''
    レーベンシュタイン距離を計算します
    
    @param a: unicode    対象文字列
    @param b: unicode    比較文字列
    @return: int
    '''
    m = [ [0] * (len(b) + 1) for i in range(len(a) + 1) ]

    for i in xrange(len(a) + 1):
        m[i][0] = i

    for j in xrange(len(b) + 1):
        m[0][j] = j

    for i in xrange(1, len(a) + 1):
        for j in xrange(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                x = 0
            else:
                x = 1
            m[i][j] = min(m[i - 1][j] + 1, m[i][ j - 1] + 1, m[i - 1][j - 1] + x)
            
    return m[-1][-1]

def main():
    print levenshtein_distance("pythonista", "jython")
    
if __name__ == "__main__":
    main()
    