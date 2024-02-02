# https://school.programmers.co.kr/learn/courses/30/lessons/92334

# 숫자 비교하기
def solution_1(num1, num2):
    return 1 if num1 == num2 else -1


# 몫 구하기
def solution_1_1(num1, num2):
    return int(num1 / num2)


def solution_1_2(num1, num2):
    return num1 // num2


def solution_1_3(num1, num2):
    return divmod(num1, num2)[0]


# 나머지 구하기
solution2 = lambda num1, num2: num1 % num2


# 두수의 합
def solution_3(num1, num2):
    # return num1 + num2
    return sum([num1, num2])


# 짝수의 합
def solution_4(n):
    return sum([i for i in range(2, n + 1, 2)])


def solution_4(n):
    return sum([i for i in range(n + 1) if (i % 2) == 0])


# 머쓱이보다 키 큰사람
def solution_5(array, height):
    return len([i for i in array if height < i])
    return sum(1 for a in array if a > height)


def solution_5(array, height):
    array.append(height)
    array.sort(reverse=True)
    return array.index(height)


# 배열 reverse
def solution_6(num_list):
    return num_list[::-1]


def solution_6(num_list):
    num_list.reverse()
    return num_list


num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(num_list[::-1])
print(num_list[::3])
print(num_list[::-1])
print(num_list[1::])
print(num_list[2::-1])


# 배열 원소의 길이
def solution7(strlist):
    return list(map(len, strlist))


def solution7(strlist):
    return [len(str) for str in strlist]
