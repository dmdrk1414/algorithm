# https://school.programmers.co.kr/learn/courses/30/lessons/67256

location_dict = {
    "1": (0, 0),
    "2": (1, 0),
    "3": (2, 0),
    "4": (0, 1),
    "5": (1, 1),
    "6": (2, 1),
    "7": (0, 2),
    "8": (1, 2),
    "9": (2, 2),
    "*": (0, 3),
    "0": (1, 3),
    "#": (2, 3),
}


def solution(numbers, hand):
    answer = ''
    l_location = (0, 3)
    r_location = (2, 3)

    for num in numbers:
        # 원소가 1,4,7 이면 L / 3,6,9이면 R / 그렇지 않으면 위치 계산 조건문 작성
        if num in [1, 4, 7]:
            answer += "L"
            l_location = location_dict[str(num)]
        elif num in [3, 6, 9]:
            answer += "R"
            r_location = location_dict[str(num)]
        else:
            # 현재 숫자 좌표 구하기
            num_location = location_dict[str(num)]

            # 왼손 거리 구하기
            l_distance = abs(num_location[0] - l_location[0]) + abs(num_location[1] - l_location[1])
            # 오른손 거리 구하기
            r_distance = abs(num_location[0] - r_location[0]) + abs(num_location[1] - r_location[1])
            # 거리가 가까운 손으로 번호 입력!
            if l_distance < r_distance:  # l 거리가 작을경우
                answer += "L"
                l_location = location_dict[str(num)]
            elif r_distance < l_distance:  # r 거리가 작을경우
                answer += "R"
                r_location = location_dict[str(num)]
            else:
                if hand == 'left':
                    answer += "L"
                    l_location = location_dict[str(num)]
                if hand == 'right':
                    answer += "R"
                    r_location = location_dict[str(num)]

    return answer
