# https://school.programmers.co.kr/learn/courses/30/lessons/92334

# 1. 각 유저는 한명의 유저를 신고 가능
# 2. 신고 횟수 제한 없음
# 2.1	한 유저를 여러 번 신고 가능하나
# 2.2 	동일한 유저에 대한 신고 회수는 1회로 처리
# 3. k번 이상 신고된 유저는 정지
# 4. 정지된 유저를 신고한 유저들은 메일을 받는다.
# 출력
# 각유저의 이메일을 보내는 숫자 출력
# 1 유저에 해당하는 index만들기 dic
def solution(id_list, report, k):
    # id을 인덱스화
    dic = {id: i for i, id in enumerate(id_list)}
    # 유저의 사이즈
    userSize = len(id_list)
    # 신고 당한 갯수
    target_cout = [0] * userSize
    # 밴당한 유저의 리스트
    van_list = []
    graph = [[0] * (userSize) for _ in range(userSize)]

    # 그래프와 , 신고당한 횟수 카운트
    for two_user in report:
        start, target = two_user.split()
        graph[dic[start]][dic[target]] = 1

    for startIndex in range(userSize):
        for targetIndex in range(userSize):
            if graph[startIndex][targetIndex] == 1:
                target_cout[targetIndex] += 1

    # 밴먹은 사람의 리스트
    for i in range(userSize):
        if target_cout[i] >= k:
            van_list.append(i)

    # 정답 만약에 밴먹은 사람을 신고한 사람의 메일 수 새기
    answer = [0] * userSize
    for startIndex in range(userSize):
        for van in van_list:
            if graph[startIndex][van] == 1:
                answer[startIndex] += 1
    return answer


# id_list = ["muzi", "frodo", "apeach", "neo"]
id_list = ["con", "ryan"]
# report = ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"]
report = ["ryan con", "ryan con", "ryan con", "ryan con"]
# k = 2
k = 3


def solution(id_list, report, k):
    # 정답을 위한 리스트
    answer = [0] * len(id_list)
    # 유저을 index한다.
    targetcounts = {x: 0 for x in id_list}
    print(report)
    print(set(report))
    # 신고한 유저의 중복을 제거한다.
    for two_user in set(report):
        targetUser = two_user.split()[1]
        targetcounts[targetUser] += 1

    for two_user in set(report):
        startUser = two_user.split()[0]
        targetUser = two_user.split()[1]
        startIndex = id_list.index(startUser)

        if targetcounts[targetUser] >= k:
            answer[startIndex] += 1

    return answer


print(solution(id_list, report, k))
