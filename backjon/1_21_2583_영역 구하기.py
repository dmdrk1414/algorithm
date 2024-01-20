# https://www.acmicpc.net/problem/2583

"""
첫째 줄에 M과 N, 그리고 K가 빈칸을 사이에 두고 차례로 주어진다.

M, N, K는 모두 100 이하의 자연수이다.

둘째 줄부터 K개의 줄에는 한 줄에 하나씩 직사각형의 왼쪽 아래

꼭짓점의 x, y좌표값과 오른쪽 위 꼭짓점의 x, y좌표값이 빈칸을 사이에 두고 차례로 주어진다.

모눈종이의 왼쪽 아래 꼭짓점의 좌표는 (0,0)이고, 오른쪽 위 꼭짓점의 좌표는(N,M)이다.

입력되는 K개의 직사각형들이 모눈종이 전체를 채우는 경우는 없다

y,x,갯수
5 7 3
왼쪽아래, 오른쪽 위
x y x y
0 2 4 4
1 1 2 5
4 0 6 2
(0,4) . . . . . (4,4)2
      . . . . .
(0,2) . . . . . (4.2)
1
5 7 3
0 2 4 4
1 1 2 5
4 0 6 2


"""
import sys
from collections import deque

M, N, K = map(int, input().split())
visited = [[False]*N for _ in range(M)]

for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            visited[i][j] = True
result = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(start):
    que = deque([start])
    y, x = start
    visited[y][x] = True
    count = 1
    while que:
        yy, xx = que.popleft()
        for i in range(len(dy)):
            ny = yy + dy[i]
            nx = xx + dx[i]
            if (0 <= ny < M) and (0 <= nx < N):
                if not visited[ny][nx]:
                    que.append([ny, nx])
                    count += 1
                    visited[ny][nx] = True
    result.append(count)

# for li in visited:
#     print(li)
for y in range(M):
    for x in range(N):
        if not visited[y][x]:
            bfs([y, x])
result.sort()
print(len(result))
for i in range(len(result)):
    print(result[i], end=" ")