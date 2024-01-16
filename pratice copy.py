# https://www.acmicpc.net/submit/14502

"""
4 6
0 0 0 0 0 0
1 0 0 0 0 2
1 1 1 0 0 2
0 0 0 0 0 2


"""
import sys
from collections import deque
import copy
from itertools import combinations

input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
virus = []
safe_zone = []
dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]
result = 0;

for y in range(N):
    for x in range(M):
        if board[y][x] == 0:
            safe_zone.append([y, x])
        if board[y][x] == 2:
            virus.append([y, x])

def bfs():
    global result
    ch_virus = deque([])
    cnt = len(safe_zone) - 3
    for y, x in virus:
        ch_virus.append([y, x])
    while ch_virus:
        yy, xx = ch_virus.popleft()
        for i in range(len(dy)):
            ny = yy + dy[i]
            nx = xx + dx[i]
            if 0 <= ny < N and 0 <= nx < M:
                if ch_board[ny][nx] == 0:
                    cnt -= 1
                    ch_board[ny][nx] = 2
                    ch_virus.append([ny, nx])
    result = max(result, cnt)

for comb in combinations(safe_zone, 3):
    ch_board = copy.deepcopy(board)
    for y, x in comb:
        ch_board[y][x] = 1
    bfs()
print(result)
