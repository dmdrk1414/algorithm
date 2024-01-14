import sys
from collections import deque

def dfs(start):
    visited[start] = True
    print(start, end=" ")
    for value in graph[start]:
        if not visited[value]:
             dfs(value)

def bfs(start):
    visited[start] = True
    que = deque([start])

    while que:
        value = que.popleft()
        print(value, end=" ")

        for idx in graph[value]:
            if not visited[idx]:
                que.append(idx)
                visited[idx] = True

N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(N+1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False for _ in range(N+1)]
dfs(V)
print()

visited = [False for _ in range(N+1)]
bfs(V)
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
