# https://www.acmicpc.net/problem/11659

"""
ISTJ, ISFJ, INFJ, INTJ, ISTP, ISFP, INFP, INTP, ESTP, ESFP, ENFP, ENTP, ESTJ, ESFJ, ENFJ, ENTJ


3
3
ENTJ INTP ESFJ
4
ESFP ESFP ESFP ESFP
5
INFP INFP ESTP ESTJ ISTJ


"""
# 비둘기집 원리
from itertools import combinations
import sys
input = sys.stdin.readline

mbtis = ['ISTJ', 'ISFJ', 'INFJ', 'INTJ',
         'ISTP', 'ISFP', 'INFP', 'INTP',
         'ESTP', 'ESFP', 'ENFP', 'ENTP',
         'ESTJ', 'ESFJ', 'ENFJ', 'ENTJ']

t = int(input())
for i in range(t):
    table = {mbti : 0 for mbti in mbtis}
    n = int(input())
    temp = input().split()
    if n>32 :
        print(0)
        continue
    else :
        for mbti in temp :
            table[mbti] += 1
            if table[mbti] == 3:
                print(0)
                break
        else :
            temp = list(combinations(temp,3))
            score_list = []
            for comb in temp :
                score = 0
                for i in range(4):
                    if (comb[0][i] == comb[1][i] and
                            comb[0][i] == comb[2][i] and
                            comb[1][i] == comb[2][i]) :
                        score += 0
                    else :
                        score += 2
                score_list.append(score)
            print(min(score_list))