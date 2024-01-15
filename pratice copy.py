from collections import deque
import sys

input = sys.stdin.readline
def bfs(start):
    que = deque([start])
    visited[start]  = True
    while que:
        value = que.popleft()
        print(value, end=" ")
        for idx in graph[value]:
            if not visited[idx]:
                visited[idx] = True
                que.append(idx)

def dfs(start):
    visited[start]
    print(start, end=" ")
    for value in graph[start]:
        if not visited[value]:
            dfs(value)

N, M, V = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


visited = [False for _ in range(N + 1)]
bfs(V)
print()

visited = [False for _ in range(N + 1)]
bfs(V)
