# https://school.programmers.co.kr/learn/courses/30/lessons/17681

def solution(N, stages):
    dic = {sta: 0 for sta in range(N + 1)}
    for sta in stages:
        if sta <= N:
            dic[sta] += 1

    result = {}
    total_player = len(stages)
    for stage in range(1, N + 1):
        if total_player != 0:
            count = dic[stage]
            result[stage] = count / total_player
            total_player -= count
        else:
            result[stage] = 0
    return sorted(result, key=lambda x: result[x], reverse=True)
