import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
INF = 1001
# L은 길이다.
L = [[0] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    L[a][b] = 1
    L[b][a] = 1
t = int(input())

# 1부터 시작해서 각 value까지 BFS를 도는데,
# path에 0부터 시작해서 다음 value를 호출할 때마다 1씩 더한값을 queue에 넣는다.
# 이때 path와 distance array를 비교하면서 더 작은 값(짧은 거리)으로 distance array를 갱신시킨다.

# line 19 ~ 20 : 이때 매 테스트 케이스마다 최단거리가 바뀔 수 있기 때문에 (도로가 사라진 경우),
# 도로가 항상 추가되어 최단거리가 항상 짧아지는 경우만 있었던
# 이전 문제와 다르게 distance array를 초기화 시켜주는 작업이 필요했다.
# * 이때 전역변수 처리를 주의하자


def bfs(target):
    distance = [INF for _ in range(n + 1)]
    distance[1] = 0
    visited = [False for _ in range(n + 1)]

    queue = deque()
    queue.append(target)
    while (queue):

        value, path = queue.popleft()  # 1, 0
        if (distance[value] > path):
            distance[value] = path
        visited[value] = True

        for i in range(len(L[value])):
            if (L[value][i] == 1 and visited[i] == False):
                queue.append([i, path + 1])
                visited[i] = True
    return distance


for _ in range(t):
    check, a, b = map(int, input().split())
    if (check == 1):
        L[a][b] = 1
        L[b][a] = 1
    else:
        L[a][b] = 0
        L[b][a] = 0

    distance = bfs([1, 0])  # node, path

    for i in range(1, n + 1):
        if (distance[i] == INF):
            print(-1, end=" ")
        else:
            print(distance[i], end=" ")
    print()
