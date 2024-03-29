# https://www.acmicpc.net/problem/12761

"""
동규와 주미는 일직선 상의 돌 다리 위에있다. 돌의 번호는 0 부터 100,000 까지 존재하고
동규는 (N)번 돌 위에, 주미는 (M)번 돌 위에 위치하고 있다. 동규는 주미가 너무 보고싶기 때문에 최대한 빨리 주미에게 가기 위해

(A, B) 만큼의 힘을 가진 스카이 콩콩을 가져왔다. 동규가 정한 다리를 건너는 규칙은 턴 방식인데, 한 턴에 이동할 수 있는 거리는 이러하다.
1. 현 위치에서 +1칸, -1칸을 이동할 수 있고,
2. 스카이 콩콩을 이용해 현 위치에서 (A)나 (B)만큼 좌우로 점프할 수 있으며,
3. 순간적으로 힘을 모아 현 위치의 (A)배나 (B)배의 위치로 이동을 할 수 있다.
예를 들어 지금 동규가 7번 돌 위에 있고 스카이 콩콩의 힘이 8이면 그냥 점프를 해서 15번 돌에 갈 수도 있고,
순간적으로 힘을 모아 56번 돌에 갈 수도 있다는 것이다.
주어진 8가지의 방법 중 적절한 방법을 골라서 최대한 빨리 동규가 주미를 만날 수 있게 도와주자.
단, 이동 과정에서 100,000보다 크거나 0보다 작은 번호의 돌은 존재하지 않으므로 갈 수 없고,
같은 방법을 계속 사용해도 되며 항상 도달할 수 있는 케이스만 주어진다.

입력의 첫 줄에 스카이 콩콩의 힘 (A)와 (B), 그리고 동규의 현재위치 (N), 주미의 현재 위치 (M)이 주어진다
2 3 1 20


"""
import sys
from collections import deque
input = sys.stdin.readline
MAX = 100000
A, B, N, M = map(int, input().split())
distance = [9999 for _ in range(MAX + 1)]
visited = [False for _ in range(MAX + 1)]
nomal = [-1, 1, A, B, -A, -B]
power = [A, B]
def bfs(start):
    que = deque([start])
    visited[start] = True
    distance[start] = 0;

    while que:
        stand = que.popleft()

        for i in range(len(nomal)):
            nstand = stand + nomal[i]

            if( 0 <= nstand <= MAX) and not visited[nstand]:
                visited[nstand] = True
                que.append(nstand)
                distance[nstand] = distance[stand] + 1
        # if(nstand == M):
        #     break
        for i in range(len(power)):
            nstand = stand * power[i]

            if( 0 <= nstand <= MAX) and not visited[nstand]:
                visited[nstand] = True
                que.append(nstand)
                distance[nstand] = distance[stand] + 1
        # if(nstand == M):
        #     break

bfs(N)
print(distance[M])