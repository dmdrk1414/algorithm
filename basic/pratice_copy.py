"""
https://www.acmicpc.net/problem/1260

입력
4 5 1
1 2
1 3
1 4
2 4
3 4


출력
dfs: 1 2 4 3
bfs: 1 2 3 4
"""
import sys
from collections import deque

input = sys.stdin.readline

N, M, V = map(int, input().split())
graph = [[] * (N + 1) for _ in range(N + 1)]

for _ in range(N + 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
def dfs(start):
    visited[start] = True
    print( start, end=" ")

    for value in graph[start]:
        if not visited[value]:
            dfs(value)

def bfs(start):
    que = deque([start])
    visited[start] = True
    while que:
        value = que.popleft()
        print(value, end=" ")

        for i in graph[value]:
            if not visited[i]:
                que.append(i)
                visited[i] = True

visited= [False for _ in range(N + 1)]
dfs(V)
print()

visited= [False for _ in range(N + 1)]
bfs(V)
