from collections import deque


# numbers의 숫자를 더하거나 뺀 경우를 수평적으로 추가해준다.
# 결국 leaves리스트에 모든 계산 결과가 담기게 된다. 이후 target값과 비교해서 결과 출력.
def solution(numbers, target):
    answer = 0
    leaves = [0]
    # [1, 1, 1, 1, 1]
    for num in numbers:
        tmp = []
        for parent in leaves:
            tmp.append(parent + num)
            tmp.append(parent - num)
        leaves = tmp

    for leaf in leaves:
        if leaf == target:
            answer += 1

    return answer


print(solution([1, 1, 1, 1, 1], 3))
