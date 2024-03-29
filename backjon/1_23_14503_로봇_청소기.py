# https://www.acmicpc.net/problem/14503

"""
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