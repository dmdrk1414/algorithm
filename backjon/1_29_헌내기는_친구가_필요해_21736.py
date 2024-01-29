# https://www.acmicpc.net/problem/11659

"""
3 5
OOOPO
OIOOX
OOOXP


"""
import sys
from collections import deque

input = sys.stdin.readline
N, M = map(int, input().split())
graph_str = [  list(input().rstrip()) for _ in range(N) ]
graph = [ [] for _ in range(N) ]
visited = [[False] * (M) for _ in range(N)]
start = ()
for y in range(N):
    for x in range(M):
        if graph_str[y][x] == 'O':
            graph[y].append(0)
        if graph_str[y][x] == 'P':
            graph[y].append(1)
        if graph_str[y][x] == 'I':
            graph[y].append(2)
            start = (y, x)
        if graph_str[y][x] == 'X':
            graph[y].append(-1)

result = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(start):
    que = deque([start])
    visited[start[0]][start[1]] = True

    while que:
        yy, xx = que.popleft()

        for i in range(4):
            ny = yy + dy[i]
            nx = xx + dx[i]

            if (0 <= ny < N) and (0 <= nx < M):
                if not visited[ny][nx] and graph[ny][nx] != -1:
                    visited[ny][nx] = True
                    que.append([ny, nx])

                    if graph[ny][nx] == 1:
                        result.append([ny, nx])

bfs(start)
if len(result) == 0:
    print("TT")
else:
    print(len(result))
