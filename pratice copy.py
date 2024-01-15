import sys
from collections import deque

input = sys.stdin.readline

def bfs(start):
    que = deque([start])
    visited[start] = True

    while que:
        value = que.popleft()
        print(value, end=" ")

        for idx in (graph[value]):
            if not visited[idx]:
                visited[idx] = True
                que.append(idx)

def dfs(start):
    visited[start] = True
    print(start, end=" ")

    for value in (graph[start]):
        if not visited[value]:
            dfs(value)

n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False for _ in range(n+1)]
bfs(v)
print()

visited = [False for _ in range(n+1)]
dfs(v)

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
