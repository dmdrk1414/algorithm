# https://www.acmicpc.net/problem/2589

from collections import deque

"""
5 7
WLLWWWL
LLLWLLL
LWLWLWW
LWLWLLL
WLLWLWW

보물섬 지도를 발견한 후크 선장은 보물을 찾아나섰다. 
보물섬 지도는 아래 그림과 같이 직사각형 모양이며 여러 칸으로 나뉘어져 있다. 
각 칸은 육지(L)나 바다(W)로 표시되어 있다. 
이 지도에서 이동은 상하좌우로 이웃한 육지로만 가능하며, 
한 칸 이동하는데 한 시간이 걸린다. 
보물은 서로 간에 최단 거리로 이동하는데 있어 가장 긴 시간이 걸리는 육지 두 곳에 나뉘어 묻혀있다. 
육지를 나타내는 두 곳 사이를 최단 거리로 이동하려면 같은 곳을 두 번 이상 지나가거나, 멀리 돌아가서는 안 된다.

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


