# https://school.programmers.co.kr/learn/courses/30/lessons/77484

# 최고 순위, 최저 순위 구하기
# 0은 알수 없는 번호
# return 최고 순위와 최저 순위
state = {
    6: 1,
    5: 2,
    4: 3,
    3: 4,
    2: 5,
    1: 6,
    0: 6
}


def solution(lottos, win_nums):
    answer = []
    zero = lottos.count(0)
    count = 0

    for win in win_nums:
        count += lottos.count(win)
    if zero == 0:
        answer.append(state[count])
        answer.append(state[count])
    else:
        answer.append(state[count + zero])
        answer.append(state[count])

    return answer


def solution(lottos, win_nums):
    rank = [6, 6, 5, 4, 3, 2, 1]

    cnt_0 = lottos.count(0)
    ans = 0
    for x in win_nums:
        ans += lottos.count(x)
    return rank[cnt_0 + ans], rank[ans]


def solution(lottos, win_nums):
    state = [6, 6, 5, 4, 3, 2, 1]
    count = 0
    zero = lottos.count(0)

    for win in win_nums:
        count += lottos.count(win)

    return state[count + zero], state[count]
