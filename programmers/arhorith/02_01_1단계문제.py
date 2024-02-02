# https://school.programmers.co.kr/learn/courses/30/lessons/92334

# 숫자 비교하기
def solution_1(num1, num2):
    return 1 if num1 == num2 else -1


# 몫 구하기
def solution_1_1(num1, num2):
    return int(num1 / num2)


def solution_1_2(num1, num2):
    return int(num1 // num2)


def solution_1_3(num1, num2):
    return divmod(num1, num2)[0]


# 나머지 구하기
solution2 = lambda num1, num2: num1 % num2
