# https://www.acmicpc.net/problem/14503

"""
문제
청소기는 바라보는 방향이 있으며, 이 방향은 동, 서, 남, 북 중 하나이다.

1. 현재 칸이 아직 청소되지 않은 경우, 현재 칸을 청소한다. // 0이 청소안함.
2. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우,
1. 바라보는 방향을 유지한 채로 한 칸 후진할 수 있다면 한 칸 후진하고 1번으로 돌아간다.
2. 바라보는 방향의 뒤쪽 칸이 벽이라 후진할 수 없다면 작동을 멈춘다.
3. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우,
1. 반시계 방향으로 90^ 회전한다.
2. 바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 빈 칸인 경우 한 칸 전진한다.
3. 1번으로 돌아간다.

3 3
1 1 0
1 1 1
1 0 1
1 1 1


"""
import sys
from collections import deque
input = sys.stdin.readline
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

n, m = map(int, input().split())
r, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
count = 1;
visited = [[False]*m for _ in range(n)]
visited[r][c] = True

while True:
    flag = False
    # 동, 서, 남, 북으로 이동
    for _ in range(4):
        d = (d + 3) % 4
        nr = r + dr[d]
        nc = c + dc[d]

        if 0<= nr < n and 0 <= nc < m and arr[nr][nc] == 0:
            if not visited[nr][nc]:
                visited[nr][nc] = True
                count += 1
                r = nr
                c = nc
                flag = True
                break
    # 동, 서, 남, 북으로 돌렸는데 청소하는 곳이 없으면
    if flag == False:
        # 벽이있으면 stop
        if arr[r - dr[d]][c - dc[d]] ==1:
            print(count)
            break
        else:
            # 벽이 없으면 후진
            r, c = r-dr[d], c-dc[d]