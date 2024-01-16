# https://www.acmicpc.net/problem/16953


"""
정수 A를 B로 바꾸려고 한다. 가능한 연산은 다음과 같은 두 가지이다.

2를 곱한다.
1을 수의 가장 오른쪽에 추가한다.
A를 B로 바꾸는데 필요한 연산의 최솟값을 구해보자.

2 162
2 → 4 → 8 → 81 → 162

5
"""
import sys
from collections import deque
input = sys.stdin.readline

A, B = map(int, input().split())
count = 1;
while B != A:
    count += 1
    temp = B
    if (B % 10) == 1:
        B //=10
    elif (B % 2) == 0:
        B //= 2
    if temp == B:
        print(-1)
        break
else:
    print(count)

