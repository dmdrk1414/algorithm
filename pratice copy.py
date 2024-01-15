import sys
from collections import deque

"""
5 3
1 2
1 3
2 4
5
2 3
4 5
3 4
1 4
1 5


"""
def bfs(start):
    que = deque([start])
    visited = [False for _ in range(N + 1)]
    visited[start[0]] = True

    while que:
        value, path = que.popleft()
        if(distanse[value] > path):
            distanse[value] = path

        for idx in range(len(L[value])):
            if not visited[idx] and L[value][idx] == 1:
                visited[idx] = True
                que.append([idx, distanse[value] + 1])

N, M = map(int, input().split())
L = [[0] * (N + 1) for _ in range(N + 1)]
INF = 9999
distanse = [INF for _ in range(N + 1)]
distanse[1] = 0
for _ in range(M):
    a, b = map(int, input().split())
    L[a][b] = 1
    L[b][a] = 1
q = int(input())

for _ in range(q):
    target_1, target_2 = map(int, input().split())
    L[target_1][target_2] = 1
    L[target_2][target_1] = 1

    bfs([1, 0])

    for idx in range(1, N + 1):
        if distanse[idx] == INF:
            print(-1, end=" ")
        else:
            print(distanse[idx], end=" ")
    print()


