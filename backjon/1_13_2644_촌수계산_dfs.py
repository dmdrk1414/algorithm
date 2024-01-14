# https://www.acmicpc.net/problem/2644


def dfs(start):
    visited[start] = True

    for value in graph[start]:
        if not visited[value]:
            result[value] = result[start] + 1
            dfs(value)


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
dfs(target_1)

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
