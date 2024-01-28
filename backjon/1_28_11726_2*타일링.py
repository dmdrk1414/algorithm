# https://www.acmicpc.net/problem/11659

"""
9



"""
import sys

input = sys.stdin.readline
n = int(input())
dp = [0] * (1000 + 1)
dp[1] = 1
dp[2] = 2
dp[3] = 3

for i in range(4, n + 1):
    if 1 <= n <= 3:
        break
    dp[i] = sum(dp[i - 2:i])

print(dp[n] % 10_007)
