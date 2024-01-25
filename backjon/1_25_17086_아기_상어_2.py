# https://www.acmicpc.net/problem/17086
"""
N×M 크기의 공간에 아기 상어 여러 마리가 있다.
공간은 1×1 크기의 정사각형 칸으로 나누어져 있다.
한 칸에는 아기 상어가 최대 1마리 존재한다.

어떤 칸의 안전 거리는 그 칸과 가장 거리가 가까운 아기 상어와의 거리이다.
두 칸의 거리는 하나의 칸에서 다른 칸으로 가기 위해서 지나야 하는 칸의 수이고,
이동은 인접한 8방향(대각선 포함)이 가능하다.

안전 거리가 가장 큰 칸을 구해보자.

5 4
0 0 1 0
0 0 0 0
1 0 0 0
0 0 0 0
0 0 0 1


"""
from collections import deque
import sys

input = sys.stdin.readline
d = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]
# y, x
N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
shark = deque()
for y in range(N):
    for x in range(M):
        if graph[y][x] == 1:
            shark.append([y, x])
result = 0
while shark:
    yy, xx = shark.popleft()

    for y, x in d:
        ny = yy + y
        nx = xx + x
        if (ny < 0) or (ny >= N) or (nx < 0) or (nx >= M):
            continue
        if graph[ny][nx] == 1:
            continue
        if graph[ny][nx] == 0:
            graph[ny][nx] = graph[yy][xx] + 1
            shark.append([ny, nx])
            result = max(result, graph[ny][nx])
print(result - 1)
