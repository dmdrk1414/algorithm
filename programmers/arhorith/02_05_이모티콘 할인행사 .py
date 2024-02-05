# 1. n명의 카카오톡 사용자들에게 이모티콘 m개를 할인하여 판매합니다.
# 2. 이모티콘마다 할인율은 다를 수 있으며, 할인율은 10%, 20%, 30%, 40% 중 하나로 설정됩니다.
def solution(users, emoticons):
    answer = []
    users.sort(key=lambda x: x[-1])
    result = 0
    states = list(user[0] for user in users)
    states.sort(reverse=True)
    print(states)

    for state in states:
        for user_state, max_money in users:
            apply = 0
            sell_money = 0

            if user_state

    return answer


# 이모티콘 플러스 서비스 가입 수와 이모티콘 매출액

print(solution([[40, 10000], [25, 10000]], [7000, 9000]))
