from collections import deque
# https://www.acmicpc.net/problem/2644


def bfs(target_1):
    que = deque([target_1])
    visited[target_1] = True

    while que:
        value = que.popleft()

        for i in graph[value]:
            if not visited[i]:
                visited[i] = True
                result[i] = result[value] + 1
                que.append(i)


N = int(input())
target_1, target_2 = map(int, input().split())
M = int(input())
graph = [[] for _ in range(N + 1)]
result = [0 for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (N + 1)
bfs(target_1)

if result[target_2] != 0:
    print(result[target_2])
else:
    print(-1)

"""
9
7 3
7
1 2
1 3
2 7
2 8
2 9
4 5
4 6


"""
