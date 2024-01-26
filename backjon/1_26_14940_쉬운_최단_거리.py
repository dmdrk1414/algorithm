import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * (m) for _ in range(n)]
start = ()
distance = [[-1] * (m) for _ in range(n)]

for y in range(n):
    for x in range(m):
        if graph[y][x] == 2:
            start = (y, x)
            break

dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]


def bfs(target):
    distance[target[0]][target[1]] = 0
    # visited[target[0]][target[1]] = True
    que = deque([target])
    while que:
        yy, xx = que.popleft()

        for i in range(4):
            ny = yy + dy[i]
            nx = xx + dx[i]
            if 0 > ny or ny >= n or 0 > nx or nx >= m:
                continue
            if 0 <= ny < n and 0 <= nx < m:
                if graph[ny][nx] == 1 and distance[ny][nx] == -1:
                    que.append([ny, nx])
                    distance[ny][nx] = distance[yy][xx] + 1
                if graph[ny][nx] == 0:
                    distance[ny][nx] = 0


bfs(start)

# for i in range(n):
#     for k in range(m):
#         if graph[i][k] == 0:
#             print(0, end=" ")
#         else:
#             print(distance[i][k], end=" ")
#     print()

for li in distance:
    print(*li)
