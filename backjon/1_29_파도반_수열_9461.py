# https://www.acmicpc.net/problem/9461

"""
2
6
12


"""
import sys

input = sys.stdin.readline

max = 100
dp = [0] * (max + 1)
dp[0] = 0
dp[1] = 1
dp[2] = 1
dp[3] = 1

for i in range(4, max + 1):
    dp[i] = dp[i -3] + dp[i -2]
T = int(input())
for _ in range(T):
    value = int(input())
    print(dp[value])