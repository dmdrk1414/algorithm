# https://school.programmers.co.kr/learn/courses/30/lessons/81301


def solution(s):
    dic = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7',
           'eight': '8', 'nine': '9'}

    for i, j in dic.items():
        s = s.replace(i, j)

    answer = int(s)
    return answer
