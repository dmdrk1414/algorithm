from collections import deque


"""
https://www.acmicpc.net/problem/1260

입력
4 5 1
1 2
1 3
1 4
2 4
3 4


출력
dfs: 1 2 4 3
bfs: 1 2 3 4
"""


def dfs(start):
    visited[start] = True
    print(start, end=" ")

    for i in graph[start]:  # 정점의 간선으로 연결된 정점 탐색
        if not visited[i]:  # 간선으로 연결된 정점중 방문이 안되면
            dfs(i)  # dfs을 한다.


def bfs(start):
    queue = deque([start])  # 방문한 기록이 있는 queue을 생성
    visited[start] = True  # 처음 방문한 곳을 true을 한다.

    while queue:  # queue가 없을때 까지 반복
        value = queue.popleft()  # queue을 뽑아서
        print(value, end=" ")  # 출력한다.
        for i in graph[value]:  # 정점과 연결된 다른 정점들을 탐색한다.
            if not visited[i]:
                visited[i] = True
                queue.append(i)


# 입력
# 점정의 갯수(N), 간선의 갯수(M), 탐색을 시작하는 정점(V).
# 4 5 1
N, M, V = map(int, input().split())

# N이 5라면
# graph = [[], [], [], [], [], []]의 그래프를 만든다
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    # append는 리스트의 끝에 추가를 한다는 의미이다.
    # 그래프의 정점과 연결간 정점을 표시하는 것이다.
    graph[a].append(b)
    graph[b].append(a)

# 정렬
for i in graph:
    i.sort()

# dfs
visited = [False] * (N + 1)  # 방문한 것을 표기하는 visited리스트 생성
dfs(V)
print()

# bfs
visited = [False] * (N + 1)  # 방문한 것을 표기하는 visited리스트 생성
bfs(V)
