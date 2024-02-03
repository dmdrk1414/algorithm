# https://school.programmers.co.kr/learn/courses/30/lessons/17681

def tenFromtwo(arr):
    result = []
    for num in arr:
        binaryNum = str(bin(num))
        result.append(binaryNum)
    return result


def solution(n, arr1, arr2):
    answer = []

    result_1 = tenFromtwo(arr1)
    result_2 = tenFromtwo(arr2)
    result = []
    for i in range(n):
        binary = str(bin(arr1[i] | arr2[i])[2:])
        binary = binary.rjust(n, '0')
        binary = binary.replace("0", " ").replace("1", "#")
        result.append(binary)
    answer = result
    return answer


dic = {2: 10, 9: 15, 10: 5}
andage = [5, 1, 5]
if 5 in andage:
    print(5)
