# https://www.acmicpc.net/problem/2589

from collections import deque

"""
5 7
WLLWWWL
LLLWLLL
LWLWLWW
LWLWLLL
WLLWLWW


"""
H, W = map(int, input().split())
graph = [[] for _ in range(H + 1)]

for _ in range(H):
    input_ = input()
    graph_one = []

    for idx in range(W):
        if input_[idx] == 'L':
            graph_one.append(1)
        elif input_[idx] == 'W':
            graph_one.append(0)
    graph.append(graph_one)


