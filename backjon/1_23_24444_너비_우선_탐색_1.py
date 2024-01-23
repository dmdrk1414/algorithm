# https://www.acmicpc.net/problem/24444
"""
오늘도 서준이는 너비 우선 탐색(BFS) 수업 조교를 하고 있다. 아빠가 수업한 내용을 학생들이 잘 이해했는지 문제를 통해서 확인해보자.

N개의 정점과 M개의 간선으로 구성된 무방향 그래프(undirected graph)가 주어진다. 정점 번호는 1번부터 N번이고 모든 간선의 가중치는 1이다.

정점 R에서 시작하여 너비 우선 탐색으로 노드를 방문할 경우 노드의 방문 순서를 출력하자.

너비 우선 탐색 의사 코드는 다음과 같다. 인접 정점은 오름차순으로 방문한다.

5 5 1
1 4
1 2
2 3
2 4
3 4


"""
import sys
from collections import deque

input = sys.stdin.readline

N, M, V = map(int, input().split())
graph = [[] for _ in range(N + 1)]
vsited = [0]  * (N + 1)

for _ in range(M):
    y, x = map(int, input().split())
    graph[y].append(x)
    graph[x].append(y)

def bfs(start):
    que = deque([start])
    vsited[start] = 1
    count = 1

    while que:
        value = que.popleft()

        for i in graph[value]:
            if not vsited[i]:
                que.append(i)
                count += 1
                vsited[i] = count
for li in graph:
    li.sort()
bfs(V)
for i in (vsited[1::]):
    print(i)