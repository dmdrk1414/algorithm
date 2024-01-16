

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

for y in range(N):
    for x in range(M):
        if board[y][x] == 0:
            safe_zone.append([y, x])
        if board[y][x] == 2:
            virus.append([y, x])

def bfs():
    ch_virus = deque([])
    cnt = len()
    for y, x in virus:
        ch_virus.append([y, x])

for comb in combinations(virus, 3):
    ch_board = copy.deepcopy(board)
    for y, x in comb:
        ch_board[y][x] = 1
    bfs()
