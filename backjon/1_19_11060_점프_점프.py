"""
https://www.acmicpc.net/submit/11060

10
1 2 0 1 3 2 1 5 4 2


"""
import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
graph = list(map(int, input().split()))

if N == 1:
    print(0)
else:
    # bfs
    distance = [0] * (N + 1)
    queue = deque([1])

    while queue:
        x = queue.popleft()
        if x + graph[x-1] >= N:
            print(distance[x] + 1)
            break
        for i in range(1, graph[x-1]+1):
            nx = x+i
            if distance[nx] == 0:
                queue.append(nx)
                distance[nx] = distance[x] + 1
                if(nx >= N):
                    print(distance[x])
    else:
        print(-1)
